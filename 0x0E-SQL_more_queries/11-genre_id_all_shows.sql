-- right join
SELECT title, genre_id 
FROM tv_show_genres 
RIGHT JOIN tv_shows 
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY title, tv_show_genres.genre_id ASC;
