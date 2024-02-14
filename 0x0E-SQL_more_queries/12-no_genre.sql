-- no genre
SELECT title, genre_id 
FROM tv_shows LEFT JOIN tv_show_genre
ON tv_shows.id = tv_show_genre.genre_id 
WHERE tv_show_genre.genre_id IS NULL;
