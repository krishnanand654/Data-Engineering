
--DECLARE DATABASE name
DECLARE @DatabaseName VARCHAR(128) = 'practise_db';

IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name = @DatabaseName)
BEGIN
	DECLARE @SQL NVARCHAR(MAX) = 'CREATE DATABASE '+ @DatabaseName;
	EXEC sp_executesql @SQL;
END

USE practise_db;

SELECT *
FROM INFORMATION_SCHEMA.TABLES ;

IF NOT EXISTS (SELECT 1
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME = 'fmcg')
BEGIN
	DECLARE @CREATE_TABLE NVARCHAR(MAX) = 
	'CREATE TABLE [dbo].fmcg (
    Ware_house_ID VARCHAR(10) PRIMARY KEY,
    WH_Manager_ID VARCHAR(10),
    Location_type VARCHAR(10),
    WH_capacity_size VARCHAR(10),
    zone VARCHAR(10),
    WH_regional_zone VARCHAR(10),
    num_refill_req_l3m INT,
    transport_issue_l1y INT,
    Competitor_in_mkt INT,
    retail_shop_num INT,
    wh_owner_type VARCHAR(15),
    distributor_num INT,
    flood_impacted INT,
    flood_proof INT,
    electric_supply INT,
    dist_from_hub INT,
    workers_num INT,
    wh_est_year INT,
    storage_issue_reported_l3m INT,
    temp_reg_mach INT,
    approved_wh_govt_certificate VARCHAR(20),
    wh_breakdown_l3m INT,
    govt_check_l3m INT,
    product_wg_ton INT
);'

EXEC sp_executesql @CREATE_TABLE;

END

--load data to table 
BULK INSERT fmcg 
FROM 'D:/CSV/FMCG_data.csv'
--Options
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

SELECT * FROM fmcg;

--GET OWNER TYPES and ITS FREQUENCY
SELECT wh_owner_type, count(wh_owner_type)
FROM fmcg
GROUP BY wh_owner_type;


SELECT TOP(5)  [dbo].fmcg.Ware_house_ID, [dbo].fmcg.product_wg_ton
FROM fmcg ORDER BY product_wg_ton DESC;

--max, min, avg, median from distance_from_hub
SELECT 
	TOP(1)
	MIN([dbo].fmcg.dist_from_hub) OVER() AS 'MIN',
	MAX([dbo].fmcg.dist_from_hub) OVER() AS 'MAX',
	AVG([dbo].fmcg.dist_from_hub) OVER() AS 'AVG',
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dist_from_hub ASC) OVER () AS 'MEDIAN'
FROM
	fmcg
WHERE 
	product_wg_ton > 10000 AND Location_type = 'Urban';

-- using CTE
WITH PERCENTILE AS(
	SELECT
		dist_from_hub as distance,
		PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dist_from_hub ASC) OVER() AS Median
	FROM
		fmcg
	 WHERE product_wg_ton > 10000 AND Location_type = 'Urban'
)

SELECT 
	MIN(distance),
	MAX(distance),
	AVG(distance),
	MAX(Median)
FROM PERCENTILE;


--subquery
SELECT 
	MIN(distance),
	MAX(distance),
	AVG(distance),
	MAX(Median)
FROM 
	(SELECT
		dist_from_hub as distance,
		PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dist_from_hub ASC) OVER() AS Median
	FROM
		fmcg
	WHERE 
		product_wg_ton > 10000 AND Location_type = 'Urban')
	AS 
		PERCENTILE;

SELECT 
	WH_regional_zone, workers_num 
FROM 
	fmcg 
WHERE workers_num = (SELECT MAX(workers_num) from fmcg);


SELECT * FROM fmcg;

-- Total Capacity and Average Capacity by Warehouse Location Type:
SELECT 
	Location_Type, 
	SUM(product_wg_ton) AS Total_Capacity, 
	AVG(product_wg_ton) AS Avg_Capacity
FROM
	fmcg
GROUP BY Location_Type;

--Number of Refills Requested in the Last 3 Months by Regional Zone:
SELECT
	[dbo].fmcg.WH_regional_zone,
	SUM([dbo].fmcg.num_refill_req_l3m) AS No_of_refills
FROM
	fmcg
GROUP BY
	WH_regional_zone;

--Count of Warehouses Impacted by Floods and Those with Flood-Proof Measures:
SELECT 
	SUM(flood_impacted) AS flood_impacted,
	SUM(flood_proof) AS flood_proof
FROM
	fmcg;

-- What percentage of warehouses have flood-proof measures?
WITH total AS(
	SELECT 
		flood_proof AS flood_proof
FROM
	fmcg
)
SELECT 
	(SUM(flood_proof) * 100/count(*)) AS flood_proof
FROM
	total;

select count(*) from fmcg

