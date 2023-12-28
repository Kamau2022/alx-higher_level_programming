-- this script is creating a table called first_table in the current database in your MySQL server.

CREATE TABLE IF NOT EXISTS first_table (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (Id)
);