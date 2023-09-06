-- Create tha database and the user
-- Grant all privileges to the user in the new databse
-- Grant SELECT privileges to the user in the performance_schema database 

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
