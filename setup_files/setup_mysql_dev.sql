-- This script will prepare a MySQL development server for TheNextPage app
-- Create a database named 'tnp_dev_db'
CREATE DATABASE IF NOT EXISTS tnp_dev_db;

-- Create a database user named 'tnp_dev' with password 'tnp_dev_pwd'
CREATE USER IF NOT EXISTS 'tnp_dev'@'localhost' IDENTIFIED BY 'tnp_dev_pwd';

-- Grant all privileges on database 'tnp_dev_db' to user 'tnp_dev'
GRANT ALL ON tnp_dev_db.* TO 'tnp_dev'@'localhost';
 
-- Grant SELECT privilege on database 'performance_schema' to user 'tnp_dev'
GRANT SELECT ON performance_schema.* TO 'tnp_dev'@'localhost';
