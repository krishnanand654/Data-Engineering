-- T-SQL or Transact SQL which is extension of SQL(Structured Query Language).
-- Developed for T-SQL syntax by Microsoft for use of SQL server, Azure SQl DB.
-- Key Features of T-SQL: 
-- Variable, Control Flow Statements (IF), LOOPS
-- TRY CATCH, CREATE FUNCTIONS, STORED PROCEDURES

-- 1. Show databases
SELECT name FROM sys.databases;

-- 2. Show list of schemas
SELECT name as SchemaName from sys.schemas;

-- 3. Creating new database
CREATE DATABASE sales;

-- 4. Declare variable with name DatabaseName
DECLARE @DatabaseName VARCHAR(128) = 'sales';

-- 5. Test condition to check is database exist
IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name = @DatabaseName) 

-- If the database doesn't exist
BEGIN
	DECLARE @SQL NVARCHAR(MAX) = 'CREATE DATABASE '+ QUOTENAME(@DatabaseName);
	EXEC sp_executesql @SQL;
END

-- 6. Use the database
USE sales;

-- 7. Create table
CREATE TABLE [dbo].products (productid VARCHAR(20) NOT NULL, name VARCHAR(50), 
price float, quantity int, store_name VARCHAR(50), city VARCHAR(50));

-- 8. Insert records into products table
INSERT INTO [dbo].products (productid, name, price, quantity, store_name, city) VALUES
('P001', 'Samsung Galaxy S21', 69999.99, 50, 'TechWorld', 'Mumbai'),
('P002', 'Apple iPhone 14', 79999.99, 30, 'GadgetHub', 'Delhi'),
('P003', 'Sony WH-1000XM4', 24999.99, 100, 'AudioMart', 'Bengaluru'),
('P004', 'Dell Inspiron 15', 54999.99, 20, 'CompuCentre', 'Chennai'),
('P005', 'Nike Air Max 270', 8999.99, 75, 'Sporty Shoes', 'Hyderabad'),
('P006', 'OnePlus 11', 56999.99, 40, 'PhoneArena', 'Pune'),
('P007', 'Sony Bravia 4K TV', 99999.99, 10, 'ElectroStore', 'Kolkata'),
('P008', 'HP Pavilion 14', 45999.99, 25, 'Laptop Zone', 'Ahmedabad'),
('P009', 'Bose QuietComfort 35', 29999.99, 15, 'AudioMart', 'Gurgaon'),
('P010', 'Canon EOS 1500D', 32999.99, 12, 'CameraHouse', 'Jaipur');

-- 9. Run query on products table to show all records
SELECT * FROM products;

-- 10. Show the schema description of table
SELECT
	TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM 
	INFORMATION_SCHEMA.COLUMNS
WHERE 
	TABLE_NAME = 'products';

-- 11. DROP TABLE products;

-- 12. Alter table
ALTER TABLE products ADD total_amount FLOAT ; -- DECIMAL(18,2)  

-- Dummy column
ALTER TABLE products ADD DateOfDelivery DATE ;

-- 13. Drop column
ALTER TABLE products DROP COLUMN DateOfDelivery;

-- 14. Update column datatype
ALTER TABLE products ALTER COLUMN DateOfDelivery VARCHAR(20);

-- 15. Update the Value of Column Total Amount = Price * Quantity
UPDATE 
	products
SET 
	total_amount = price * quantity;

-- 16. Query to show first 5 records
SELECT TOP (5) [productid]
      ,[name]
      ,[price]
      ,[quantity]
      ,[store_name]
      ,[city]
      ,[total_amount]
FROM [sales].[dbo].[products]
