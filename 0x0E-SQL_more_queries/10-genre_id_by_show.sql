-- left join
select title, tv_show_genres.genre_id as genre_id
from tv_show_genres left join tv_shows 
on show_id = tv_shows.id 
order by title, tv_show_genres.genre_id ASC;
