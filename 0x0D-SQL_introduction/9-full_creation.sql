-- this script is creating a table called second_table in the current database in your MySQL server.

CREATE TABLE IF NOT EXISTS second_table (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
score INT,
PRIMARY KEY (Id)
);

INSERT INTO second_table
(name, score)
VALUES ( 'John', 10), ('Alex', 3), ('Bob', 14), ('George', 8);
