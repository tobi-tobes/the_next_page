-- This script will prepare a MySQL test server for TheNextPage app
-- Create a database named 'tnp_test_db'
CREATE DATABASE IF NOT EXISTS tnp_test_db;

-- Create a database user named 'tnp_test' with password 'tnp_test_pwd'
CREATE USER IF NOT EXISTS 'tnp_test'@'localhost' IDENTIFIED BY 'tnp_test_pwd';

-- Grant all privileges on database 'tnp_test_db' to user 'tnp_test'
GRANT ALL ON tnp_test_db.* TO 'tnp_test'@'localhost';

-- Grant SELECT privilege on database 'performance_schema' to user 'tnp_test'
GRANT SELECT ON performance_schema.* TO 'tnp_test'@'localhost';
