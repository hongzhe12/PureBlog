#!/bin/sh

# 运行 Django 的迁移
python manage.py migrate

# 收集静态文件
python manage.py collectstatic --noinput

# 启动 Django 开发服务器
python manage.py runserver 0.0.0.0:8000