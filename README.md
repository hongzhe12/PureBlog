## Python 3.9.13
```bash
docker exec -it -uroot mysite-django pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple #安装依赖 
docker exec -it -uroot mysite-django python manage.py makemigrations # 升级应用 
docker exec -it -uroot mysite-django python manage.py migrate # 升级应用 
docker exec -it -uroot mysite-django python manage.py createsuperuser # 创建超级用户

# 代理
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890

# 取消全局代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 导入镜像
```bash
docker load -i mysite-django.tar.gz
docker load -i mysite-nginx.tar.gz
docker load -i minio.tar.gz
docker load -i mysite-postgres.tar.gz
```

# 常用命令
```bash
docker exec -it -uroot mysite-django python manage.py collectstatic # 收集静态文件
docker exec -it -uroot mysite-django ls /code/static/img # 检查静态文件是否存在
docker logs mysite-django # 查看容器日志
docker exec -it -uroot mysite-django cat logs/django.log  # 查看django日志
cat logs/django.log
docker compose up --build web -d # 构建镜像并启动容器
docker compose down # 停止并删除容器
docker compose up -d # 启动容器
docker compose restart # 重启容器
docker compose logs # 查看容器日志
docker compose exec web bash # 进入容器
docker compose exec postgres psql -U dev -d dev # 进入postgres容器
docker compose exec minio mc config host add myminio http://127.0.0.1:9000 minioadmin minioadmin # 配置minio
docker compose exec minio mc ls myminio # 查看minio文件
```

# 拉取更新并重启
```bash
git checkout origin/master -- PureBlog/settings.py && git pull origin master # 放弃本地修改，并同步
vim $(find ./ -name .env) 
sed -i 's/DEBUG = True/DEBUG = False/g' $(find ./ -name settings.py) # 修改为生产环境
docker compose down web
docker compose up -d web

docker compose down
docker compose up -d

docker compose restart web # 重启容器
docker logs mysite-django # 查看容器日志

```

# 导入样例数据
```bash
docker cp article_article.sql mysite-postgres:/
docker exec -it mysite-postgres psql -U dev -d dev -f /article_article.sql
```