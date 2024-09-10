#!/bin/bash

# 仓库地址
REPO_URL="https://github.com/hongzhe12/PureBlog.git"
# 本地存放仓库的目录
LOCAL_DIR="/home/PureBlog/"

# 克隆或更新仓库
if [ ! -d "$LOCAL_DIR/.git" ]; then
    echo "Cloning repository..."
    git clone $REPO_URL $LOCAL_DIR
else
    echo "Updating repository..."
    cd $LOCAL_DIR
    git fetch --all
    git reset --hard origin/master
    git clean -fd
fi

# 检查环境配置文件
ENV_FILE="$LOCAL_DIR/postgres/.env"
if [ -f "$ENV_FILE" ]; then
    echo "Environment file found:"
    cat $ENV_FILE
else
    echo "Environment file not found."
fi

# 修改为生产环境
SETTINGS_FILE=$(find $LOCAL_DIR -name settings.py)
if [ -f "$SETTINGS_FILE" ]; then
    echo "更新设置为生产环境..."
    sed -i 's/DEBUG = True/DEBUG = False/g' "$SETTINGS_FILE"
else
    echo "配置文件未找到"
fi

# 重启 Docker Compose 服务
echo "重启 Docker Compose 服务..."
cd $LOCAL_DIR
docker compose down
docker compose up -d

echo "部署完成。"
