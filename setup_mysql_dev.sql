-- This script prepares a new MySQL server for the project to be used for development

-- Create the database `hbnb_dev_db` if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user in `localhost` and set the password
-- Only action this step if the user does not already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the user (whether just created or existing) on hbnb_dev_db
-- Flush the privileges when done
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant the SELECT privilege on the `performance_schema` db to user `hbnb_dev`
-- Flush the privileges when done
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
