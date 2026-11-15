"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class DriverEntry(BaseModel):
    """连接驱动明细结构。"""

    field_0: str | None = None  # 驱动编号
    field_1: str | None = None  # 数据源类型
    field_2: str | None = None  # 驱动版本
    field_3: str | None = None  # 连接字符串
    field_4: str | None = None  # 驱动参数
    field_5: str | None = None  # 字符集
    field_6: str | None = None  # 连接池上限
    field_7: str | None = None  # 超时毫秒

class SourceEntry(BaseModel):
    """数据源实例明细结构。"""

    field_0: str | None = None  # 实例编号
    field_1: str | None = None  # 驱动类型
    field_2: str | None = None  # 连接地址
    field_3: str | None = None  # 认证凭证
    field_4: str | None = None  # 读取模式
    field_5: str | None = None  # 批次大小
    field_6: str | None = None  # 心跳间隔秒
    field_7: str | None = None  # 负责人

class MapperEntry(BaseModel):
    """映射配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 源表名
    field_2: str | None = None  # 源字段名
    field_3: str | None = None  # 目标字段名
    field_4: str | None = None  # 类型转换
    field_5: str | None = None  # 空值默认
    field_6: str | None = None  # 截断长度
    field_7: str | None = None  # 校验表达式

class ExtractEntry(BaseModel):
    """抽取任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 抽取表名
    field_3: str | None = None  # 起始游标
    field_4: str | None = None  # 批次行数
    field_5: str | None = None  # 过滤条件
    field_6: str | None = None  # 排序字段
    field_7: str | None = None  # 超时终止秒

class ConvertEntry(BaseModel):
    """转换规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 源类型
    field_2: str | None = None  # 目标类型
    field_3: str | None = None  # 转换函数
    field_4: str | None = None  # 精度舍入
    field_5: str | None = None  # 异常处理
    field_6: str | None = None  # 默认取值
    field_7: str | None = None  # 规则版本

class FormatEntry(BaseModel):
    """解析模板明细结构。"""

    field_0: str | None = None  # 模板编号
    field_1: str | None = None  # 文件格式
    field_2: str | None = None  # 分隔符
    field_3: str | None = None  # 逃逸字符
    field_4: str | None = None  # 表头行数
    field_5: str | None = None  # 日期格式
    field_6: str | None = None  # 数字格式
    field_7: str | None = None  # 编码类型

class DeltaEntry(BaseModel):
    """增量策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 增量字段
    field_3: str | None = None  # 当前水位
    field_4: str | None = None  # 回退步数
    field_5: str | None = None  # 去重窗口
    field_6: str | None = None  # 补偿重跑
    field_7: str | None = None  # 增量频率

class RateEntry(BaseModel):
    """限速配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 每秒行数
    field_3: str | None = None  # 并发查询
    field_4: str | None = None  # 批间隔毫秒
    field_5: str | None = None  # 背压水位
    field_6: str | None = None  # 降速系数
    field_7: str | None = None  # 加速阈值

class ValidateEntry(BaseModel):
    """校验规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 校验字段
    field_3: str | None = None  # 校验表达式
    field_4: str | None = None  # 采样比例
    field_5: str | None = None  # 阻断级别
    field_6: str | None = None  # 异常计数
    field_7: str | None = None  # 告警阈值

class RetryEntry(BaseModel):
    """恢复策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 最大重试
    field_3: str | None = None  # 退避因子
    field_4: str | None = None  # 初始间隔
    field_5: str | None = None  # 最大间隔
    field_6: str | None = None  # 可恢复码
    field_7: str | None = None  # 死信通道

class EncryptEntry(BaseModel):
    """脱敏规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # 脱敏算法
    field_3: str | None = None  # 掩码字符
    field_4: str | None = None  # 保留前缀
    field_5: str | None = None  # 保留后缀
    field_6: str | None = None  # 盐值
    field_7: str | None = None  # 规则版本

class RouteEntry(BaseModel):
    """路由规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 源表名
    field_2: str | None = None  # 目标通道
    field_3: str | None = None  # 分流条件
    field_4: str | None = None  # 优先级
    field_5: str | None = None  # 缓冲区大小
    field_6: str | None = None  # 批量提交
    field_7: str | None = None  # 超时秒数

class LogEntry(BaseModel):
    """日志记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 操作表名
    field_3: str | None = None  # 开始时间
    field_4: str | None = None  # 结束时间
    field_5: str | None = None  # 行数
    field_6: str | None = None  # 字节数
    field_7: str | None = None  # 状态码

class ScheduleEntry(BaseModel):
    """调度计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 调度表达式
    field_3: str | None = None  # 时区
    field_4: str | None = None  # 最大并行
    field_5: str | None = None  # 超时终止
    field_6: str | None = None  # 依赖检查
    field_7: str | None = None  # 通知策略

class MonitorEntry(BaseModel):
    """监控指标明细结构。"""

    field_0: str | None = None  # 指标编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 延迟阈值
    field_3: str | None = None  # 吞吐阈值
    field_4: str | None = None  # 错误率阈值
    field_5: str | None = None  # 检测频率
    field_6: str | None = None  # 告警级别
    field_7: str | None = None  # 通知渠道

class CleanseEntry(BaseModel):
    """清洗规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # 空值策略
    field_3: str | None = None  # 格式校验
    field_4: str | None = None  # 异常剔除
    field_5: str | None = None  # 去重键
    field_6: str | None = None  # 规则版本
    field_7: str | None = None  # 生效日期

class ExportEntry(BaseModel):
    """转储通道明细结构。"""

    field_0: str | None = None  # 通道编号
    field_1: str | None = None  # 数据来源
    field_2: str | None = None  # 目标系统
    field_3: str | None = None  # 导出格式
    field_4: str | None = None  # 传输协议
    field_5: str | None = None  # 分割大小
    field_6: str | None = None  # 压缩方式
    field_7: str | None = None  # 加密开关

class AuthEntry(BaseModel):
    """凭证管理明细结构。"""

    field_0: str | None = None  # 凭证编号
    field_1: str | None = None  # 数据源实例
    field_2: str | None = None  # 认证类型
    field_3: str | None = None  # 密钥标识
    field_4: str | None = None  # 轮换周期天
    field_5: str | None = None  # 过期告警
    field_6: str | None = None  # 自动续期
    field_7: str | None = None  # 备份凭证
