-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities
WHERE (
SELECT id
FROM states 
WHERE name = 'California') = cities.state_id
ORDER BY cities.id;