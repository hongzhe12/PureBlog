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
docker exec -it -uroot mysite-django python manage.py collectstatic
docker exec -it -uroot mysite-django ls /home/app/django/media
```

# 拉取更新并重启
```bash
git pull origin master
docker compose down
docker compose up -d
```

# 导入样例数据
```bash
docker cp article_article.sql mysite-postgres:/
docker exec -it mysite-postgres psql -U dev -d dev -f /article_article.sql
```