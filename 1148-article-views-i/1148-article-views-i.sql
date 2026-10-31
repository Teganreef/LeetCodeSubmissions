Select DISTINCT author_id AS id
from views 
where author_id = viewer_id
ORDER BY id;