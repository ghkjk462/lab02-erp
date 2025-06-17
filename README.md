# ERP 仓储管理系统

一个基于 Django + Vue.js 的现代化仓储管理系统，提供完整的进销存管理和财务管理功能。

## 项目简介

本系统是一个功能完善的ERP管理系统，采用前后端分离的架构设计，支持多企业团队的独立数据管理。系统涵盖了企业日常经营所需的核心业务流程，包括采购管理、销售管理、库存管理、财务管理等模块。

## 技术栈

### 后端
- **框架**: Django 3.2 + Django REST Framework
- **数据库**: MySQL
- **任务队列**: Celery + Redis

### 前端
- **框架**: Vue.js 2.6
- **路由**: Vue Router
- **状态管理**: Vuex
- **图表**: ECharts + Viser-Vue

## 核心功能

### 📦 库存管理
- 库存查询：实时查看所有产品的库存状态
- 入库管理：记录产品入库信息，准确跟踪库存增加
- 出库管理：记录产品出库信息，确保库存数据准确
- 库存预警：库存不足时自动提醒

### 💰 采购管理
- 采购开单：创建采购订单，记录供应商采购信息
- 采购记录查询：查询历史采购记录
- 供应商管理：维护供应商信息和联系方式

### 🛒 销售管理
- 销售开单：创建销售订单，记录客户购买信息
- 销售记录查询：查询历史销售记录
- 客户管理：维护客户信息和交易记录

### 📊 基础数据管理
- 产品信息管理：维护产品基本信息和属性
- 数据报表：库存报表、销售报表、采购报表分析

### 🏢 系统管理
- 员工账号管理：管理系统用户账号
- 数据看板：重要业务数据的可视化展示

## 环境要求

- **Python**: 3.8+
- **Node.js**: 12.13.1
- **MySQL**: 5.7+
- **Redis**: 6.0+ (用于Celery任务队列)

## 快速开始

### 数据库配置

1. 设置数据库字符集为 `utf8mb4`
2. 创建数据库：
   ```sql
   CREATE DATABASE erp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. 修改 `./django/configs/django.py` 中的数据库连接配置

### 后端运行

```bash
cd django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runscript create_user      # 创建管理员用户
python manage.py runscript create_test_data # 初始化测试数据
python manage.py runserver
```

### 前端运行

```bash
cd frontend
yarn install
yarn serve
```

## 项目结构

```
erp/
├── django/              # Django后端项目
│   ├── apps/           # 业务应用模块
│   ├── configs/        # 配置文件
│   ├── extensions/     # 扩展组件
│   └── scripts/        # 管理脚本
├── frontend/           # Vue.js前端项目
│   ├── src/           # 源代码
│   └── public/        # 静态资源
└── README.md          # 项目说明
```

