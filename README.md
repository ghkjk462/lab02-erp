## 本地运行流程

### 前端

~~~
yarn serve
~~~

### 后端运行
~~~
python manage.py runserver
~~~

### 数据库设置

1. 数据库字符集设置为 utf8mb4
2. 创建 erp-db 数据库(先设置字符集, 再创建数据库)
    CREATE DATABASE erp_db;
3. ./django/configs/django.py里修改password,user,host，port字段
4. 数据库初始化
    * python manage.py makemigrations
    * python manage.py migrate
5. 创建管理员用户
    * python manage.py runscript create_user
6. 初始化简单数据
    * python manage.py runscript create_test_data
