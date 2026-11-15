import { useEffect, useState } from 'react'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const fallbackCards = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
const fallbackModules = [{"name": "驱动管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据源注册", "created": 0, "pending": 0, "abnormal": 0}, {"name": "字段映射", "created": 0, "pending": 0, "abnormal": 0}, {"name": "分批抽取", "created": 0, "pending": 0, "abnormal": 0}, {"name": "类型转换", "created": 0, "pending": 0, "abnormal": 0}, {"name": "格式解析", "created": 0, "pending": 0, "abnormal": 0}, {"name": "增量同步", "created": 0, "pending": 0, "abnormal": 0}, {"name": "速率控制", "created": 0, "pending": 0, "abnormal": 0}, {"name": "接入校验", "created": 0, "pending": 0, "abnormal": 0}, {"name": "失败恢复", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据脱敏", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据路由", "created": 0, "pending": 0, "abnormal": 0}, {"name": "接入日志", "created": 0, "pending": 0, "abnormal": 0}, {"name": "定时调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "源端监控", "created": 0, "pending": 0, "abnormal": 0}, {"name": "接入清洗", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据转储", "created": 0, "pending": 0, "abnormal": 0}, {"name": "认证配置", "created": 0, "pending": 0, "abnormal": 0}]

export default function Overview() {
  const [cards, setCards] = useState<Overview['cards']>(fallbackCards)
  const [moduleRows, setModuleRows] = useState<Overview['modules']>(fallbackModules)

  useEffect(() => {
    fetchJson<Overview>('/api/overview')
      .then((payload) => {
        setCards(payload.cards)
        setModuleRows(payload.modules)
      })
      .catch(() => undefined)
  }, [])

  return (
    <section className="page">
      <header className="page-head">
        <div>
          <h2>运营概览</h2>
          <p className="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
        </div>
      </header>
      <div className="stat-row">
        {cards.map((card) => (
          <article key={card.label} className="stat-card">
            <span className="stat-label">{card.label}</span>
            <strong className="stat-value">{card.value}</strong>
          </article>
        ))}
      </div>
      <table className="data-table">
        <thead>
          <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
        </thead>
        <tbody>
          {moduleRows.map((row) => (
            <tr key={row.name}>
              <td>{row.name}</td>
              <td>{row.created}</td>
              <td>{row.pending}</td>
              <td>{row.abnormal}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
