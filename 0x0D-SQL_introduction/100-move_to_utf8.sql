-- a script that converts hbtn_0c_0 database to UTF8 in your MySQL server.
ALTER DATABASE hbtn_0c_0 COLLATE =utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `first_table`  CHANGE `name` `name` VARCHAR(256);
