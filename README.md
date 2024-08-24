# PureBlog: 简洁至上的个人博客系统
欢迎来到纯博客系统 (PureBlog)，这是一个基于 Django 框架构建的简洁、功能完备的博客平台。在这里，您可以轻松撰写、发布和分享您的文章。

[![Python Version](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-blue.svg)](https://www.djangoproject.com/)
<!-- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) -->

## 概述

PureBlog 是一个用 Django 框架开发的个人博客系统，它提供了一个简单、优雅的界面，让您可以轻松地撰写、发布和组织您的文章。

## 特性

- **Markdown 支持**：集成了 mdeditor，支持 Markdown 编辑器进行文章撰写。
- **响应式设计**：无论是在桌面还是移动设备上，都能提供良好的阅读体验。
- **文章管理**：CRUD 功能齐全，轻松管理您的文章。
- **自定义文章摘要**：为每篇文章设置摘要，自动生成或手动编写。

## 快速开始

### 环境要求

- Python 3.9 或更高版本
- Django 4.2 或更高版本
- PostgreSQL 数据库（推荐用于生产环境）

### 安装步骤

1. 克隆仓库到本地机器
   ```bash
   git clone https://github.com/yourusername/pureblog.git
   ```
2. 进入项目目录并创建虚拟环境（可选）
   ```bash
   cd pureblog
   python -m venv venv
   ```
3. 激活虚拟环境（Windows）
   ```bash
   .\venv\Scripts\activate
   ```
   或（macOS/Linux）
   ```bash
   source venv/bin/activate
   ```
4. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
5. 创建数据库和应用迁移
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. 创建超级用户
   ```bash
   python manage.py createsuperuser
   ```
7. 启动开发服务器
   ```bash
   python manage.py runserver
   ```

### 访问博客

打开浏览器并访问 `http://127.0.0.1:8000` 即可查看您的纯博客系统。

## 目录结构

```
pureblog/
│
├── PureBlog/           # 项目根目录
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
│
├── article/            # 文章应用目录
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/          # 模板文件
├── static/             # 静态文件
├── media/              # 媒体文件
├── logs/               # 日志文件
│
└── README.md
```

## 贡献

如果您有任何建议或想要贡献代码，请提交 Pull Request 或创建 Issue。

## 项目演示
在线项目：[博客首页](https://pythond.cn)
---

