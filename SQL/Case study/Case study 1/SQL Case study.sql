-- Case study - Supply chain management
USE warehouse_db;


SELECT 
	* 
FROM 
	fmcg;

-- 1) Find the Shape of the FMCG Table. 
-- How would you determine the total number of rows and columns in the FMCG dataset?

-- rows
SELECT 
	count(*)  AS No_of_rows
FROM
	fmcg;

-- Columns
SELECT 
	count(*)  AS No_of_columns
FROM
	INFORMATION_SCHEMA.columns
WHERE
	TABLE_NAME = 'fmcg';

-- 2) Evaluate the Impact of Warehouse Age on Performance. 
-- Question: How does the age of a warehouse impact its operational performance, 
-- specifically in terms of storage issues reported in the last years?

SELECT
	(YEAR(GETDATE()) - wh_est_year) AS AGE, AVG(storage_issue_reported_l3m) AS Average_storage_issues
FROM
	fmcg
WHERE
	wh_est_year IS NOT NULL
GROUP BY 
	(YEAR(GETDATE()) - wh_est_year)
ORDER BY 
	AGE;

-- Studying the query response we can say there is direct correlation (positive corr) or 
-- direct linearity between warehouse age and average_storage_issue

-- 3) Analyze the Relationship Between Flood-Proof Status and Transport Issues. 
-- Question: Is there a significant relationship between flood-proof status and
-- the number of transport issues reported in the last year?
SELECT
	flood_proof,
	SUM(transport_issue_l1y) as Average_transport_issue
FROM
	fmcg
GROUP BY 
	flood_proof;

-- Insight: More transportation issue has been found for non-flood proof warehouses.

-- 4) Evaluate the Impact of Government Certification on Warehouse Performance. 
-- Question: How does having a government certification impact the performance of warehouses, 
-- particularly in terms of breakdowns and storage issues?
SELECT
	approved_wh_govt_certificate,
	AVG(storage_issue_reported_l3m) as avg_storage_issue_reported_l3m,
	AVG(wh_breakdown_l3m) as avg_wh_breakdown_l3m
FROM
	fmcg
GROUP BY 
	approved_wh_govt_certificate;

-- Insight: Comparing values of 

-- 5) Determine the Optimal Distance from Hub for Warehouses:
-- Question: What is the optimal distance from the hub for warehouses to minimize transport issues, based on the data provided?

SELECT
	transport_issue_l1y,
	AVG(dist_from_hub) as Optimal_distance
FROM
	fmcg
GROUP BY 
	transport_issue_l1y;

-- The optimum distance from hub must be less than equal to 162 for no transport issue

-- 6) Identify the Zones with the Most Operational Challenges.
-- Question: Which zones face the most operational challenges, considering factors like transport issues, storage problems, and breakdowns?


SELECT 
	zone,
	SUM(transport_issue_l1y) AS Total_transport_issues,
	SUM(storage_issue_reported_l3m) AS Total_storage_issues,
	SUM(wh_breakdown_l3m) AS Total_breakdown_issues,
	(SUM(transport_issue_l1y)+SUM(storage_issue_reported_l3m)+SUM(wh_breakdown_l3m)) AS Total_issues
FROM
	fmcg
GROUP BY zone;

-- Insight North most , east less

-- 7) Identify High-Risk Warehouses Based on Breakdown Incidents and Age. 
-- Question: Which warehouses are at high risk of breakdowns, especially considering their age and the number of breakdown incidents reported in the last 3 months?
-- Done

-- 8) Examine the Effectiveness of Warehouse Distribution Strategy. 
-- Question: How effective is the current distribution strategy in each zone, 
-- based on the number of distributors connected to warehouses and their respective product weights?

SELECT
	zone,
	SUM(distributor_num) As Total_distributor,
	SUM(product_wg_ton) AS weights,
	SUM(product_wg_ton) / SUM(distributor_num) as Effectiveness
FROM
	fmcg
GROUP BY zone;

-- Insight: The current distribution plan is best in east zone and worst in south and west

-- 9) Identify High-Risk Warehouses Based on Breakdown Incidents and Age. 
-- Question: Which warehouses are at high risk of breakdowns, especially considering their age and the number of breakdown incidents reported in the last 3 months?

SELECT
	Ware_house_ID,
	(YEAR(GETDATE()) - wh_est_year) as Warehouse_age,
	wh_breakdown_l3m,
	CASE
		WHEN wh_breakdown_l3m > 5 THEN 'HIGH_RISK'
		WHEN wh_breakdown_l3m > 3 THEN 'HIGH_RISK'
		ELSE 'LOW_RISK'
	END AS Risk_Level
FROM
	fmcg
WHERE
	(YEAR(GETDATE()) - wh_est_year) > 15
ORDER BY wh_breakdown_l3m DESC;

-- i) Correlation Between Worker Numbers and Warehouse Issues. 
-- Question: Is there a correlation between the number of workers in a warehouse and the number of storage or breakdown issues reported?
SELECT
	workers_num,
	AVG(wh_breakdown_l3m) as avg_break_down_issues,
	AVG(storage_issue_reported_l3m) as avg_storage_issue_reported
FROM 
	fmcg
GROUP BY workers_num
ORDER BY workers_num;

-- no relations

-- j) Assess the Zone-wise Distribution of Flood Impacted Warehouses.
-- Question: Which zones are most affected by flood impacts, and how does this affect their overall operational stability?

SELECT 
	zone, 
	COUNT(*) AS total_warehouse,
	SUM(flood_impacted) AS Flood_impacted_warehouse,
	SUM(flood_impacted)*100/COUNT(*) AS Flood_Impact_Percentage
FROM
	fmcg
GROUP BY zone
ORDER BY Flood_Impact_Percentage DESC;

-- Other ways using when
SELECT 
	zone, 
	COUNT(*) AS total_warehouse,
	SUM(CASE WHEN flood_impacted = 1 THEN 1 ELSE 0 END) AS Flood_impacted_warehouse,
	SUM(CASE WHEN flood_impacted = 1 THEN 1 ELSE 0 END)*100/COUNT(*) AS Flood_Impact_Percentage
FROM
	fmcg
GROUP BY zone
ORDER BY Flood_Impact_Percentage DESC;

-- INsight: Analysing all zones flood impacted warehouse percentage can be concluded that
-- North zone warehouse are high affected by flood


-- k) Calculate the Cumulative Sum of Total Work years for Each Zone. 
-- Question: How can you calculate the cumulative sum of total working years for each zone?

SELECT
	zone, 
	SUM(YEAR(GETDATE()) - wh_est_year)  OVER(ORDER BY zone ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cum_sum
FROM
	fmcg;

-- difference
SELECT
	zone,
	YEAR(GETDATE()) - wh_est_year from fmcg ORDER BY zone;

-- k) Calculate the Cumulative Sum of Total Workers for Warehouse Govt Rating, 
-- Question: How can you calculate the cumulative sum of total workers for each Warehouse Gvnt Rating?

SELECT
	approved_wh_govt_certificate, 
	workers_num,
	SUM(workers_num) OVER(PARTITION BY approved_wh_govt_certificate ORDER BY approved_wh_govt_certificate ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cum_sum
FROM
	fmcg;

SELECT
	zone,
	workers_num from fmcg ORDER BY approved_wh_govt_certificate;

--  Rank Warehouses Based on Distance from the Hub. 
-- Question: How would you rank warehouses based on their distance from the hub?
SELECT
	Ware_house_ID,
	dist_from_hub,
	DENSE_RANK() OVER( ORDER BY dist_from_hub ASC) AS WH_RANK
FROM
fmcg;

-- m) Calculate the Running AVG of Product Weight in Tons for Each Zone:
-- Question: How can you calculate the running/cummulative/moving avg of product weight in tons for each zone?

SELECT
	zone, 
	product_wg_ton,
	AVG(product_wg_ton) OVER(ORDER BY zone ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_sum
FROM
	fmcg;

-- n) Rank Warehouses Based on Total Number of Breakdown Incidents. 
-- Question: How can you rank warehouses based on the total number of breakdown incidents in the last 3 months?

SELECT
	Ware_house_ID,
	wh_breakdown_l3m,
	DENSE_RANK() OVER( ORDER BY wh_breakdown_l3m) AS WH_RANK
FROM
	fmcg;

-- o) Determine the Relation Between Transport Issues and Flood Impact.
-- Question: Is there any significant relationship between the number of transport issues and flood impact status of warehouses?
SELECT
	flood_impacted,
	SUM(transport_issue_l1y) as Total_transport_issue
FROM
	fmcg
GROUP BY 
	flood_impacted;

