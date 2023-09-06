-- Create tha database and the user
-- Grant all privileges to the user in the new databse
-- Grant SELECT privileges to the user in the performance_schema database 

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
