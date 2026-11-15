import { useState } from 'react'
import { Link, Route, Routes } from 'react-router-dom'

import Overview from './views/Overview'
import DriverView from './views/driver'
import SourceView from './views/source'
import MapperView from './views/mapper'
import ExtractView from './views/extract'
import ConvertView from './views/convert'
import FormatView from './views/format'
import DeltaView from './views/delta'
import RateView from './views/rate'
import ValidateView from './views/validate'
import RetryView from './views/retry'
import EncryptView from './views/encrypt'
import RouteView from './views/route'
import LogView from './views/log'
import ScheduleView from './views/schedule'
import MonitorView from './views/monitor'
import CleanseView from './views/cleanse'
import ExportView from './views/export'
import AuthView from './views/auth'

const navItems = [{ label: "运营概览", path: "/" }, { label: "驱动管理", path: "/driver" }, { label: "数据源注册", path: "/source" }, { label: "字段映射", path: "/mapper" }, { label: "分批抽取", path: "/extract" }, { label: "类型转换", path: "/convert" }, { label: "格式解析", path: "/format" }, { label: "增量同步", path: "/delta" }, { label: "速率控制", path: "/rate" }, { label: "接入校验", path: "/validate" }, { label: "失败恢复", path: "/retry" }, { label: "数据脱敏", path: "/encrypt" }, { label: "数据路由", path: "/route" }, { label: "接入日志", path: "/log" }, { label: "定时调度", path: "/schedule" }, { label: "源端监控", path: "/monitor" }, { label: "接入清洗", path: "/cleanse" }, { label: "数据转储", path: "/export" }, { label: "认证配置", path: "/auth" }]

export default function App() {
  const [operator] = useState('值班管理员')

  return (
    <div className="app-shell">
      <aside className="app-side">
        <h1 className="app-title">异构数据源接入网关</h1>
        <nav className="nav-list">
          {navItems.map((item) => (
            <Link key={item.path} to={item.path} className="nav-item">
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="app-main">
        <header className="app-head">
          <span className="head-desc">面向结构化数据库、半结构化文件、消息队列等多类异构数据源的统一接入、字段映射、类型转换、分批抽取与接入日志追溯的网关平台。</span>
          <span className="head-user">当前值班：{operator}</span>
        </header>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/driver" element={<DriverView />} />
          <Route path="/source" element={<SourceView />} />
          <Route path="/mapper" element={<MapperView />} />
          <Route path="/extract" element={<ExtractView />} />
          <Route path="/convert" element={<ConvertView />} />
          <Route path="/format" element={<FormatView />} />
          <Route path="/delta" element={<DeltaView />} />
          <Route path="/rate" element={<RateView />} />
          <Route path="/validate" element={<ValidateView />} />
          <Route path="/retry" element={<RetryView />} />
          <Route path="/encrypt" element={<EncryptView />} />
          <Route path="/route" element={<RouteView />} />
          <Route path="/log" element={<LogView />} />
          <Route path="/schedule" element={<ScheduleView />} />
          <Route path="/monitor" element={<MonitorView />} />
          <Route path="/cleanse" element={<CleanseView />} />
          <Route path="/export" element={<ExportView />} />
          <Route path="/auth" element={<AuthView />} />
        </Routes>
      </main>
    </div>
  )
}
