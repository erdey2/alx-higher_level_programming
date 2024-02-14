-- left join
SELECT title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres LEFT JOIN tv_shows 
ON show_id = tv_shows.id 
ORDER BY title, tv_show_genres.genre_id ASC;
