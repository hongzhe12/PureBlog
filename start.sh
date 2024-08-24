#!/bin/sh

# 收集静态文件
python manage.py collectstatic --noinput

# 生成新的迁移文件
python manage.py makemigrations

# 创建数据库和应用迁移
python manage.py migrate

# 启动 Django 开发服务器
uvicorn PureBlog.asgi:application --host 0.0.0.0 --port 8000 --workers 10