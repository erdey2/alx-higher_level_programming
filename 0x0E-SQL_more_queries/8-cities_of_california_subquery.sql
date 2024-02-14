-- select 
SELECT cities.id, cities.name FROM states, cities WHERE states.id = cities.state_id AND cities.state_id = 1 ORDER BY cities.id;
