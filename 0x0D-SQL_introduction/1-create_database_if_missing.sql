-- this script is creating the database hbtn_0c_0 in your MySQL server.
-- database is dropped if it  exists

#!/bin/bash

# MySQL credentials
DB_USER="your_username"
DB_PASSWORD="your_password"

# Database name
DB_NAME="hbtn_0c_0"

# Attempt to create the database
mysql -u $DB_USER -p$DB_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DB_NAME" 2>/dev/null
