-- show all
SELECT title, name
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B.show_id
LEFT JOIN tv_genres C
ON B.genre_id = C.id
ORDER BY title,name ASC;
