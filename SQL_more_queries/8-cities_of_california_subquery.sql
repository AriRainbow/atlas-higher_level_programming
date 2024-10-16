-- 8-cities_of_california_subquery.sql

-- Select all cities where the state_id corresponds to California
SELECT * 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
