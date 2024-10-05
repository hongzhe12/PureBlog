#!/bin/bash

# 定义变量
SQL_FILE="article_article.sql"
CONTAINER_NAME="mysite-postgres"
DB_USER="dev"
DB_NAME="dev"

# 检查 SQL 文件是否存在
if [ ! -f "$SQL_FILE" ]; then
    echo "Error: SQL file $SQL_FILE does not exist."
    exit 1
fi

# 复制 SQL 文件到 Docker 容器
echo "Copying SQL file to Docker container..."
docker cp "$SQL_FILE" "$CONTAINER_NAME:/"

# 在 Docker 容器内执行 SQL 文件
echo "Importing data into PostgreSQL database..."
docker exec -it "$CONTAINER_NAME" psql -U "$DB_USER" -d "$DB_NAME" -f "/$SQL_FILE"

echo "Data import completed successfully."