# 使用官方 Python 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /code

# 安装必要的编译工具和库
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline6-dev \
    libmysqlclient-dev \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

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