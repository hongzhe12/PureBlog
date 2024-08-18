#!/bin/sh

# 收集静态文件
python manage.py collectstatic --noinput

# 启动 Django 开发服务器
uvicorn mysite.asgi:application --host 0.0.0.0 --port 8000 --workers 10