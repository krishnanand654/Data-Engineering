-- Declare variable with name DatabaseName
DECLARE @DatabaseName VARCHAR(128) = 'taxi_db';

-- Test condition to check is database exist
IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name = @DatabaseName) 

-- If the database doesn't exist
BEGIN
	DECLARE @SQL NVARCHAR(MAX) = 'CREATE DATABASE '+ QUOTENAME(@DatabaseName);
	EXEC sp_executesql @SQL;
END

USE taxi_db;

CREATE TABLE trip (
    VendorID INT,
    lpep_pickup_datetime VARCHAR(50) , -- Format: MM/DD/YYYY HH:MM:SS AM/PM
    lpep_dropoff_datetime VARCHAR(50), -- Format: MM/DD/YYYY HH:MM:SS AM/PM
    store_and_fwd_flag CHAR(1),
    RatecodeID INT,
    PULocationID INT,
    DOLocationID INT,
    passenger_count INT,
    trip_distance FLOAT,
    fare_amount DECIMAL(10,2),
    extra DECIMAL(10,2),
    mta_tax DECIMAL(10,2),
    tip_amount DECIMAL(10,2),
    tolls_amount DECIMAL(10,2),
    ehail_fee DECIMAL(10,2),
    improvement_surcharge DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_type INT,
    trip_type INT,
    congestion_surcharge DECIMAL(10,2)
);


-- DROP TABLE trip;

BULK INSERT trip FROM 'D:/CSV/2021_Green_Taxi_Trip_Data.csv'
WITH
(
	FIELDTERMINATOR = ',', -- '|', ';','\t',' '
	ROWTERMINATOR = '0x0a', --Carraige return & new line character - '\r\n', '\n', '\r', '0x0a':line feed
	FIRSTROW = 2 -- skip the header from records
);

-- 1) Shape of the Table (Number of Rows and Columns)
SELECT 
	COUNT(*) AS No_of_row
FROM
	trip;

SELECT
	COUNT(*) AS No_of_columns
FROM
	INFORMATION_SCHEMA.columns;

-- 2) Show Summary of Green Taxi Rides – Total Rides, Total Customers, Total Sales, 
SELECT
	SUM(
		CASE 
			WHEN trip_distance > 0 THEN 1
			ELSE 0 
		END) AS Total_Rides,
	SUM(passenger_count) AS Total_customers,
	SUM(total_amount) AS Total_amount
FROM
	trip;

-- 3) Total Rides with Surcharge and its percentage.
SELECT
	SUM(
		CASE 
			WHEN congestion_surcharge > 0 THEN 1
			ELSE 0 
		END) AS Total_Rides_with_surcharge,
	(SUM(
		CASE 
			WHEN congestion_surcharge > 0 THEN 1
			ELSE 0 
		END)) * 100/COUNT(*) AS _Percentage
FROM
	trip;

-- 4) Cumulative Sum of Total Fare Amount for Each Pickup Location
SELECT
	PULocationID AS pick_up_location,
	total_amount,
	SUM(total_amount)  OVER(ORDER BY PULocationID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cum_sum
FROM
	trip
ORDER BY PULocationID; 

-- 5) Which Payment Type is Most Common in Each Drop-off Location
SELECT
	DOLocationID,
	payment_type,
	payment_frequency
FROM 
	(SELECT
		DOLocationID,
		payment_type,
		COUNT(payment_type) AS payment_frequency,
		DENSE_RANK() OVER(PARTITION BY DOLocationID ORDER BY COUNT(payment_type) DESC) as Frequent_rank
	FROM
		trip
	WHERE 
		payment_type>=0
	GROUP BY 
		DOLocationID, payment_type
	) AS _
WHERE 
	Frequent_rank = 1
ORDER BY 
		DOLocationID,payment_type ASC;


-- 6) Create a New Column for Trip Distance Band and Show Distribution
SELECT
	trip_distance,
	trip_distribution
FROM(
	SELECT
		trip_distance,
		NTILE(4) OVER( ORDER BY trip_distance) AS trip_distribution
	FROM
		trip
	) AS _
WHERE
	trip_distribution <= 3
ORDER BY 
	trip_distance;




-- 7) Find the Most Frequent Pickup Location (Mode) with rides fare greater than average of ride fare.
SELECT 
    PULocationID,
	(SELECT AVG(fare_amount) FROM trip ) AS average,
    COUNT(*) AS frequency
FROM 
    trip
WHERE 
    fare_amount > (SELECT AVG(fare_amount) FROM trip)
GROUP BY 
    PULocationID
ORDER BY 
    frequency DESC;



-- 8 Show the Rate Code with the Highest Percentage of Usage

SELECT
	RateCodeID,
	COUNT(RateCodeID) AS Usage,
	(COUNT(RateCodeID) * 100.0 / (SELECT COUNT(RateCodeID) FROM trip)) AS Highest_Percentage
FROM
	trip
WHERE
	RateCodeID >= 0
GROUP BY 
	RateCodeID
ORDER BY
	Highest_Percentage DESC;



-- 9 Show Distribution of Tips, Find the Maximum Chances of Getting a Tip
SELECT
	tip_amount,
	
	COUNT(tip_amount)
	
FROM
	trip
GROUP BY tip_amount;
;

-- 10 Calculate the Rank of Trips Based on Fare Amount within Each Pickup Location
SELECT 
	PULocationID,
	fare_amount,
	DENSE_RANK() OVER(PARTITION BY PULocationID ORDER BY fare_amount DESC) AS fare_rank
FROM
	trip
ORDER BY PULocationID;
	
-- 11 Find Top 20 Most Frequent Rides Routes. 


SELECT 
    PULocationID,
    DOLocationID,
    COUNT(*) AS Frequency
FROM 
    trip
GROUP BY 
    PULocationID,
    DOLocationID
ORDER BY 
    Frequency DESC


 
-- 12) Calculate the Average Fare of Completed Trips vs. Cancelled Trips
SELECT
	TRIP_STATUS,
	AVG(fare_amount) AS Average_Fare
FROM
	(
SELECT
	fare_amount,
	CASE
		WHEN trip_distance >0 THEN 'Completed'
		ELSE 'Cancelled'
	END AS TRIP_STATUS
FROM
	trip) AS _
GROUP BY
	TRIP_STATUS;

	


