-- number of shows
SELECT name AS genre, count(genre_id) AS number_of_shows 
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre_id 
ORDER BY number_of_shows DESC;
