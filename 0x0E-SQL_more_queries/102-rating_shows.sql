-- sum by rating
SELECT title, SUM(rate) AS rating
FROM tv_shows, tv_show_ratings 
WHERE tv_shows.id = tv_show_ratings.show_id
GROUP BY show_id
ORDER BY rating DESC;
