# 使用官方 Python 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /code

# 更新APT源并安装必要的系统包
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-dev \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 复制 requirements.txt
COPY requirements.txt requirements.txt

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目源代码
COPY . .

# 设置环境变量
ENV DJANGO_SETTINGS_MODULE=PureBlog.settings

# 运行 Django 的迁移
RUN python manage.py migrate

# 收集静态文件
RUN python manage.py collectstatic --noinput
