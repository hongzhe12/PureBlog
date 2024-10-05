#!/bin/bash

cd /home/PureBlog
docker exec -it mysite-postgres psql -U dev -d dev -c "TRUNCATE TABLE article_article;"
docker cp article_article.sql mysite-postgres:/
docker exec -it mysite-postgres psql -U dev -d dev -f /article_article.sql