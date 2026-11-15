# 异构数据源接入网关

面向结构化数据库、半结构化文件、消息队列等多类异构数据源的统一接入、字段映射、类型转换、分批抽取与接入日志追溯的网关平台。

这是一个前后端分离的管理平台：前端 React + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 React + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 驱动管理 | `driver` | 连接驱动 | 驱动编号、数据源类型、驱动版本 |
| 数据源注册 | `source` | 数据源实例 | 实例编号、驱动类型、连接地址 |
| 字段映射 | `mapper` | 映射配置 | 配置编号、源表名、源字段名 |
| 分批抽取 | `extract` | 抽取任务 | 任务编号、数据源实例、抽取表名 |
| 类型转换 | `convert` | 转换规则 | 规则编号、源类型、目标类型 |
| 格式解析 | `format` | 解析模板 | 模板编号、文件格式、分隔符 |
| 增量同步 | `delta` | 增量策略 | 策略编号、数据源实例、增量字段 |
| 速率控制 | `rate` | 限速配置 | 配置编号、数据源实例、每秒行数 |
| 接入校验 | `validate` | 校验规则 | 规则编号、数据源实例、校验字段 |
| 失败恢复 | `retry` | 恢复策略 | 策略编号、数据源实例、最大重试 |
| 数据脱敏 | `encrypt` | 脱敏规则 | 规则编号、目标字段、脱敏算法 |
| 数据路由 | `route` | 路由规则 | 规则编号、源表名、目标通道 |
| 接入日志 | `log` | 日志记录 | 记录编号、数据源实例、操作表名 |
| 定时调度 | `schedule` | 调度计划 | 计划编号、关联任务、调度表达式 |
| 源端监控 | `monitor` | 监控指标 | 指标编号、数据源实例、延迟阈值 |
| 接入清洗 | `cleanse` | 清洗规则 | 规则编号、目标字段、空值策略 |
| 数据转储 | `export` | 转储通道 | 通道编号、数据来源、目标系统 |
| 认证配置 | `auth` | 凭证管理 | 凭证编号、数据源实例、认证类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

领域：数据工程
子方向：数据采集、爬虫与RPA
