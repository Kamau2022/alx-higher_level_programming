--  a script that creates the table force_name on your MySQL server.

DROP TABLE IF EXISTS force_name; 
CREATE TABLE IF NOT EXISTS force_name (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
