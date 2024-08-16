
-- Declare variable with name DatabaseName
DECLARE @DatabaseName VARCHAR(128) = 'warehouse_db';

-- Test condition to check is database exist
IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name = @DatabaseName) 

-- If the database doesn't exist
BEGIN
	DECLARE @SQL NVARCHAR(MAX) = 'CREATE DATABASE '+ QUOTENAME(@DatabaseName);
	EXEC sp_executesql @SQL;
END

USE warehouse_db;

CREATE TABLE [dbo].fmcg (
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
);

--DROP TABLE [dbo].fmcg;

SELECT
	TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM 
	INFORMATION_SCHEMA.COLUMNS
WHERE 
	TABLE_NAME = 'fmcg';

-- 1. Way: Right click db >tasks >Import flat files
-- 2. BULK INSERT
BULK INSERT fmcg FROM 'D:/CSV/FMCG_data.csv'
WITH
(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2 -- skip the header from records
);

SELECT * FROM fmcg;



-- 1. show no.of records
SELECT count(*) as No_of_Records FROM fmcg;

-- 2. Write a query to find ware house with maximum capacity of storage (Top 5)
SELECT Top(5) Ware_house_ID, product_wg_ton
FROM fmcg 
ORDER BY product_wg_ton DESC;


-- 3. Write a query to find ware house with minimum capacity of storage (Bottom 5)
SELECT Top(5) Ware_house_ID, product_wg_ton
FROM fmcg 
ORDER BY product_wg_ton ASC;

-- 4. Total count of warehouse regional zone
SELECT  
	WH_regional_zone AS "zone", COUNT(WH_regional_zone) AS "count"
FROM 
	fmcg 
GROUP BY 
	WH_regional_zone 
ORDER BY 
	WH_regional_zone ASC;

-- 5. Find average, minimum, maximum, median distance from hub for Warehouse with minimum capacity 10000 and location type urban 
SELECT 
	MIN(dist_from_hub) AS 'Minimum',
	MAX(dist_from_hub) AS 'Maximum',
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dist_from_hub) AS 'Median'
FROM fmcg
WHERE product_wg_ton > 10000 and Location_type = 'Urban';

-- CTE
-- with creates a table whatever has been returned by a query

WITH Percentiles AS (
    SELECT 
        dist_from_hub,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY dist_from_hub) 
            OVER () AS Median
    FROM fmcg
    WHERE product_wg_ton > 10000 AND Location_type = 'Urban'
)

SELECT 
    MIN(dist_from_hub) AS 'Minimum',
    MAX(dist_from_hub) AS 'Maximum',
	AVG(dist_from_hub) AS 'Average',
    MAX(Median) AS 'Median'
FROM Percentiles;



