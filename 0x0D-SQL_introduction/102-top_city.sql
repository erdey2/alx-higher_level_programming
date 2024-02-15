-- average temprature
SELECT city, avg(value) AS avg_temp 
FROM temperatures 
GROUP BY city
WHERE ORDER BY avg_temp DESC LIMIT 3;
