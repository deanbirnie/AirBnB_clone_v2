-- This script prepares a new MySQL server for the project to be used for testing

-- Create the database `hbnb_test_db` if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user in `localhost` and set the password
-- Only action this step if the user does not already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to the user (whether just created or existing) on `hbnb_test_db`
-- Flush the privileges when done
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Grant the SELECT privilege on the `performance_schema` db to user `hbnb_test`
-- Flush the privileges when done
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
