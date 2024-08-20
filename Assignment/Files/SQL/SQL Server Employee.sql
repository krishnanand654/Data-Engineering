
-- Create db
DECLARE @DatabaseName VARCHAR(128) = 'employee_db';

-- Test condition to check is database exist
IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name = @DatabaseName) 

-- If the database doesn't exist
BEGIN
	DECLARE @SQL NVARCHAR(MAX) = 'CREATE DATABASE '+ QUOTENAME(@DatabaseName);
	EXEC sp_executesql @SQL;
END

USE employee_db;

CREATE TABLE EmployeeData (
    Attrition VARCHAR(3),
    Business_Travel VARCHAR(20),
    CF_age_band VARCHAR(10),
    CF_attrition_label VARCHAR(20),
    Department VARCHAR(20),
    Education_Field VARCHAR(20),
    emp_no VARCHAR(10),
    Employee_Number INT,
    Gender VARCHAR(6),
    Job_Role VARCHAR(30),
    Marital_Status VARCHAR(10),
    Over_Time VARCHAR(3),
    Over18 VARCHAR(1),
    Training_Times_Last_Year INT,
    Age INT,
    CF_current_Employee INT,
    Daily_Rate INT,
    Distance_From_Home INT,
    Education VARCHAR(20),
    Employee_Count INT,
    Environment_Satisfaction INT,
    Hourly_Rate INT,
    Job_Involvement INT,
    Job_Level INT,
    Job_Satisfaction INT,
    Monthly_Income INT,
    Monthly_Rate INT,
    Num_Companies_Worked INT,
    Percent_Salary_Hike INT,
    Performance_Rating INT,
    Relationship_Satisfaction INT,
    Standard_Hours INT,
    Stock_Option_Level INT,
    Total_Working_Years INT,
    Work_Life_Balance INT,
    Years_At_Company INT,
    Years_In_Current_Role INT,
    Years_Since_Last_Promotion INT,
    Years_With_Curr_Manager INT
);

-- DROP TABLE employeeData;

BULK INSERT employeeData FROM 'D:/CSV/HR_Employee.csv'
WITH
(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

SELECT * FROM employeeData;

-- a) Return the shape of the table
SELECT 
	COUNT(*) AS No_of_Rows
FROM
	employeeData;

SELECT 
	COUNT(*) AS No_of_Columns
FROM
	INFORMATION_SCHEMA.columns;

-- b) Calculate the cumulative sum of total working years for each department
SELECT
	Department,
	Total_Working_Years,
	SUM(Total_Working_Years) OVER(PARTITION BY Department ORDER BY Total_Working_Years ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_sum
FROM
	employeeData;

-- c) Which gender have higher strength as workforce in each department
WITH GenderStrength AS (
    SELECT 
        Department,
        Gender,
        COUNT(*) AS strength
    FROM
        EmployeeData
    GROUP BY
        Department,
        Gender
),
StrengthRankCTE AS(
	SELECT
		Department,
		Gender,
		strength,
		DENSE_RANK() OVER(PARTITION BY Department ORDER BY strength) AS gender_rank
	FROM GenderStrength
)
SELECT
	Department,
	Gender,
	strength
FROM
	StrengthRankCTE
WHERE 
	gender_rank = 2;

-- d) Create a new column AGE_BAND and Show Distribution of Employee's Age band group (Below 25, 25-34, 35-44, 45-55. ABOVE 55).
SELECT
	Age,
	CASE
		WHEN Age < 25 THEN 'Below 25'
		WHEN Age Between 25 AND 34 THEN '25-34'
		WHEN Age Between 35 AND 44 THEN '35-44'
		WHEN Age Between 45 AND 55 THEN '45-55'
		ELSE 'ABOVE 55'
	END AS AGE_BAND
FROM
	EmployeeData;

-- e) Compare all marital status of employee and find the most frequent marital status


SELECT
	Marital_Status,
	COUNT(Marital_Status) AS Most_Frequent
FROM
	EmployeeData
GROUP BY Marital_Status
ORDER BY COUNT(Marital_Status) DESC;

-- Insight: THe most frequent is Married 

-- f) Show the Job Role with Highest Attrition Rate (Percentage)
SELECT
	Job_Role,
	SUM(
	CASE
		WHEN Attrition = 'Yes' THEN 1 ELSE 0
	END) AS attrition_count_yes,
	SUM(
	CASE
		WHEN Attrition = 'Yes' THEN 1 ELSE 0
	END)*100/COUNT(Attrition) AS Attrition_Percentage
FROM
	EmployeeData
GROUP BY 
	Job_Role;

-- g) Show distribution of Employee's Promotion, Find the maximum chances of employee getting promoted.


-- h) Show the cumulative sum of total working years for each department.

SELECT
	Department,
	Total_Working_Years,
	SUM(Total_Working_Years) 
		OVER(PARTITION BY Department ORDER BY Total_Working_Years ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) 
	AS cum_sum
FROM
	employeeData;

-- i) Find the rank of employees within each department based on their monthly income
SELECT
	Department,
	Employee_Number,
	Monthly_Income,
	DENSE_RANK() OVER(PARTITION BY Department ORDER BY Monthly_Income DESC) as Income_Rank
FROM
	EmployeeData;

-- j) Calculate the running total of 'Total Working Years' for each employee within each department and age band.

SELECT
	Department,
	CF_age_band,
	Total_Working_Years,
	SUM(Total_Working_Years) 
		OVER(PARTITION BY Department, CF_age_band ORDER BY Total_Working_Years ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) 
	AS cum_sum
FROM
	employeeData;

-- k) Foreach employee who left, calculate the number of years they worked before leaving and compare it with the average years worked by employees in the same department.

SELECT
	e.Employee_Number,
	e.Department,
	e.Years_At_Company,
	-- Average years of employees worked at each department mapping to the main query department
	(SELECT
		AVG(Years_At_Company)
	FROM
		EmployeeData
	WHERE
		Department = e.Department) AS Avg_of_department,
	-- Find the difference between current working years and average working years in each department
	ABS(e.Years_At_Company - (SELECT
		AVG(Years_At_Company)
	FROM
		EmployeeData
	WHERE
		Department = e.Department)) AS Comparison
FROM
	EmployeeData as e
WHERE
	CF_current_Employee = 0
ORDER BY 
	Department;

-- l) Rank the departments by the average monthly income of employees who have left

SELECT
	Department,
	AVG(Monthly_Income) AS Average_Monthly_Income,
	DENSE_RANK() OVER(ORDER BY AVG(Monthly_Income)) AS EM_RANK
FROM
	EmployeeData
WHERE 
	CF_current_Employee = 0
GROUP BY Department;

-- m) Find the if there is any relation between Attrition Rate and Marital Status of Employee.

SELECT
    Marital_Status,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Yes,
    SUM(CASE WHEN Attrition = 'No' THEN 1 ELSE 0 END) AS Attrition_No
FROM
    EmployeeData
GROUP BY
    Marital_Status
ORDER BY Attrition_Yes;

-- n) Show the Department with Highest Attrition Rate (Percentage)
SELECT
	Department,
	SUM(
	CASE
		WHEN Attrition = 'Yes' THEN 1 ELSE 0
	END) AS attrition_count_yes,
	SUM(
	CASE
		WHEN Attrition = 'Yes' THEN 1 ELSE 0
	END)*100/COUNT(Attrition) AS Attrition_Percentage
FROM
	EmployeeData
GROUP BY 
	Department;

-- o) Calculate the moving average of monthly income over the past 3 employees for each job  role.
SELECT
    Job_Role,
    Employee_Number,
    Monthly_Income,
    AVG(Monthly_Income) OVER (PARTITION BY Job_Role ORDER BY Employee_Number ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS Moving_Avg_Income
FROM
    EmployeeData
ORDER BY
    Job_Role, Employee_Number;

-- p) Identify employees with outliers in monthly income within each job role. 
-- [ Condition : Monthly_Income < Q1 - (Q3 - Q1) * 1.5 OR Monthly_Income > Q3 + (Q3 - Q1) ]

WITH Quartiles AS (
    SELECT
        Job_Role,
        Monthly_Income,
        NTILE(4) OVER (PARTITION BY Job_Role ORDER BY Monthly_Income) AS Quartile
    FROM
        EmployeeData
),
Q1ANDQ3 AS (
    SELECT
        Job_Role,
        MIN(CASE WHEN Quartile = 1 THEN Monthly_Income END) AS Q1,
        MIN(CASE WHEN Quartile = 3 THEN Monthly_Income END) AS Q3
    FROM
        Quartiles
    GROUP BY
        Job_Role
)
SELECT
    e.Job_Role,
    e.Employee_Number,
    e.Monthly_Income,
    Q1,
    Q3,
    (Q3 - Q1) AS IQR,
    (Q1 - (Q3 - Q1) * 1.5) AS Left_Outlier,
    (Q3 + (Q3 - Q1)) AS Right_Outlier
FROM
    EmployeeData e
JOIN
    Q1ANDQ3  ON e.Job_Role = Q1ANDQ3.Job_Role
WHERE
    e.Monthly_Income < Q1 - (Q3 - Q1) * 1.5
    OR e.Monthly_Income > Q3 + (Q3 - Q1)
ORDER BY
    e.Job_Role, e.Employee_Number;

-- q) Gender distribution within each job role, show each job role with its gender domination.  [Male_Domination or Female_Domination] 
WITH GenderCTE AS(
	SELECT
		Job_Role,
		Gender,
		COUNT(Gender) AS Gender_count,
		DENSE_RANK() OVER(PARTITION BY Job_Role ORDER BY Gender) AS gender_rank
	FROM
		EmployeeData
	GROUP BY 
		Job_Role, Gender
)
SELECT 
	Job_Role,

	CASE
		WHEN gender_rank = 2 THEN 'Male_Domination'
		ELSE 'Female_Domination'
	END AS Domination
FROM 
	GenderCTE
WHERE 
	gender_rank = 2
ORDER BY 
	Job_Role, Gender ASC;

-- r) Percent rank of employees based on training times last year

SELECT
    Employee_Number,
    Training_Times_Last_Year,
    PERCENT_RANK() OVER (ORDER BY Training_Times_Last_Year) AS Percent_Rank
FROM
    EmployeeData
ORDER BY
    Percent_Rank;

-- s) Divide employees into 5 groups based on training times last year [Use NTILE ()]
WITH groupCTE AS(
	SELECT
		Employee_Number,
		Training_Times_Last_Year,
		NTILE(5) OVER(ORDER BY Training_Times_Last_Year) AS group_tile
	FROM
		EmployeeData
)
SELECT
	Employee_Number,
	Training_Times_Last_Year,
	CASE
		WHEN group_tile = 1 THEN 'group 1'
		WHEN group_tile = 2 THEN 'group 2'
		WHEN group_tile = 3 THEN 'group 3'
		WHEN group_tile = 4 THEN 'group 4'
		ELSE 'group 5'
	END AS Employee_Training_Group
FROM
	groupCTE;

--t) Categorize employees based on training times last year as - Frequent Trainee, Moderate  Trainee, Infrequent Trainee

WITH TrainingStats AS (
    SELECT
        Employee_Number,
        Training_Times_Last_Year,
        PERCENT_RANK() OVER (ORDER BY Training_Times_Last_Year ) AS Percent_Rank
    FROM
        EmployeeData
)
SELECT
    Employee_Number,
    Training_Times_Last_Year,
    CASE
        WHEN Percent_Rank >= 0.75 THEN 'Frequent Trainee'
        WHEN Percent_Rank >= 0.50 THEN 'Moderate Trainee'
        ELSE 'Infrequent Trainee'
    END AS Trainee_Category
FROM
    TrainingStats
ORDER BY
    Training_Times_Last_Year;

-- u) Categorize employees as 'High', 'Medium', or 'Low' performers based on their performance rating, using a CASE WHEN statement.

SELECT 	
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Performance_Rating) OVER () AS _
FROM	
	EmployeeData

SELECT
	Performance_Rating,
	CASE
		WHEN Performance_Rating >3 THEN 'High'
		WHEN Performance_Rating <3 THEN 'low'
		ELSE 'Medium'
	END AS Category
FROM
	EmployeeData

-- v) Use a CASE WHEN statement to categorize employees into 'Poor', 'Fair', 'Good', or 'Excellent'  work-life balance based on their work-life balance score.
SELECT
	DISTINCT
		Work_Life_Balance
FROM
	EmployeeData

SELECT
	Work_Life_Balance,
	CASE
		WHEN Work_Life_Balance > 4 THEN 'Excellent'
		WHEN Work_Life_Balance > 3 THEN 'Good'
		WHEN Work_Life_Balance > 2 THEN 'Fair'
		ELSE 'Poor'
	END AS wlb_Status
FROM
	EmployeeData;

-- w) Group employees into 3 groups based on their stock option level using the [NTILE] function.
SELECT
	Stock_Option_Level,
	CASE
		WHEN SOL_dist = 1 THEN 'group 1'
		WHEN SOL_dist = 2 THEN 'group 2'
		ELSE 'group 3'
	END As sol_groups
FROM(
SELECT
	Stock_Option_Level,
	NTILE(3) OVER(ORDER BY Stock_Option_Level) AS SOL_dist
FROM
	EmployeeData) AS _

-- x) Find key reasons for Attrition in Company
SELECT
	Department,
	Job_Role,
	AVG(Distance_From_Home) AS avg_distance,
	AVG(Job_Satisfaction) AS avg_job_satisfaction,
	AVG(Monthly_Income) AS avg_monthly_income,
	AVG(Environment_Satisfaction) AS avg_env_satisfaction,
	SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Yes_count,
	(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0/COUNT(Attrition)) AS Attrition_Yes_Percentage
FROM
	EmployeeData
GROUP BY Department, Job_Role