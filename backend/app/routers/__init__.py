"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import driver as router_driver
from app.routers import source as router_source
from app.routers import mapper as router_mapper
from app.routers import extract as router_extract
from app.routers import convert as router_convert
from app.routers import format as router_format
from app.routers import delta as router_delta
from app.routers import rate as router_rate
from app.routers import validate as router_validate
from app.routers import retry as router_retry
from app.routers import encrypt as router_encrypt
from app.routers import route as router_route
from app.routers import log as router_log
from app.routers import schedule as router_schedule
from app.routers import monitor as router_monitor
from app.routers import cleanse as router_cleanse
from app.routers import export as router_export
from app.routers import auth as router_auth

ROUTERS = [router_driver, router_source, router_mapper, router_extract, router_convert, router_format, router_delta, router_rate, router_validate, router_retry, router_encrypt, router_route, router_log, router_schedule, router_monitor, router_cleanse, router_export, router_auth]
