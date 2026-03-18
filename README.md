# 一人公司商业模式发现工具

帮助个人从"不知道做什么"走到"赚到第一块钱"。

通过结构化的自我探索问卷 + AI 深度分析，发现最适合你的一人公司商业模式，并生成可执行的 7 天行动计划。

## 项目背景

2025-2026 年，"一人公司"（OPC, One Person Company）正经历从概念到落地的爆发期。AI 工具的成熟让个人 IP 变现和轻量化创业成为真正可行的路径。

但对大多数人来说，最大的障碍不是"怎么做"，而是"做什么"——**找不到适合自己的商业模式，无法完成哪怕赚一块钱的小闭环。**

这个工具就是为了解决这个问题：

1. **自我探索** — 12 个问题挖掘你的技能、兴趣、痛点和资源约束
2. **AI 匹配分析** — 大模型理解你的自然语言回答，发现你没想到的商业机会
3. **行动计划** — 不是泛泛的建议，而是具体的 7 天行动清单

## 设计方案

### 架构

```
浏览器 (单页应用)
  │
  │  GET /           → 返回 index.html
  │  GET /api/questions → 问卷数据
  │  POST /api/analyze  → 提交答案，返回分析结果
  │
FastAPI 后端
  ├── 规则引擎: 关键词提取 → 标签匹配 → 模式评分
  └── LLM 引擎: Gemini / Claude → 个性化深度分析
```

### 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| 后端 | FastAPI + Uvicorn | 轻量、异步、适合单人项目 |
| 前端 | 原生 HTML/CSS/JS | 无构建步骤，嵌入单个 HTML 文件 |
| AI | Gemini / Claude | 通过环境变量切换，支持双 provider |
| 部署 | Railway | Procfile 一键部署 |

### 文件结构

```
├── app.py                  # FastAPI 后端（路由、评分逻辑）
├── data.py                 # 静态数据（7种商业模式、问卷、案例、计划）
├── llm.py                  # LLM 抽象层（Gemini/Claude 统一接口）
├── templates/
│   └── index.html          # 单页前端（暗色主题，多步骤问卷）
├── solo_biz_discovery.py   # CLI 版本（可独立使用）
├── requirements.txt
├── Procfile
└── README.md
```

### 分析流程

用户提交问卷后，系统执行两层分析：

**第一层：规则引擎（确定性）**

从用户回答中提取关键词 → 映射到能力标签（如"程序员" → `coding`, `automation`）→ 将标签与 7 种商业模式的 `fit_tags` 匹配打分 → 结合时间、预算、收入偏好加权 → 输出 Top 3 模式和对应的 7 天行动计划。

**第二层：LLM 引擎（个性化）**

将用户的完整回答 + 第一层匹配结果发送给 Gemini 或 Claude → LLM 交叉分析技能×兴趣×痛点，发现隐藏机会 → 输出个性化洞察、具体第一步、风险提示。

如果未配置 API Key，自动降级为仅使用第一层规则引擎，工具仍然可用。

### 7 种商业模式

| 模式 | 适合谁 | 首次收入速度 |
|------|--------|------------|
| 📚 知识产品型 | 有专业知识的人 | 1-2 周 |
| 💼 自由职业服务型 | 有具体技能的人 | 最快几天 |
| 🔧 SaaS 工具型 | 会编程的人 | 2-4 周 |
| 🎬 内容创作型 | 有表达欲的人 | 1-3 个月 |
| 🛒 电商/跨境型 | 对趋势敏感的人 | 1-2 周 |
| 👥 社群/会员型 | 善于连接人的人 | 2-4 周 |
| 🤖 AI 赋能服务型 | 会用 AI 工具的人 | 最快几天 |

## 部署步骤

### Railway 部署（推荐）

1. Fork 或 clone 本仓库到你的 GitHub

2. 登录 [Railway](https://railway.app)，点击 **New Project → Deploy from GitHub repo**

3. 选择本仓库，Railway 会自动检测 Procfile

4. 在 Railway 的 **Variables** 页面配置环境变量：

   ```
   # 选择 LLM 提供商（二选一）
   LLM_PROVIDER=gemini          # 或 claude

   # 对应的 API Key（配一个即可）
   GEMINI_API_KEY=your_key      # 使用 Gemini 时
   ANTHROPIC_API_KEY=your_key   # 使用 Claude 时
   ```

5. 部署完成后，Railway 会分配一个公网 URL，直接访问即可

### 本地开发

```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量（可选，不配置则使用规则匹配）
export LLM_PROVIDER=gemini
export GEMINI_API_KEY=your_key

# 启动
uvicorn app:app --reload --port 8000

# 访问 http://localhost:8000
```

### CLI 版本

不需要部署，直接在终端使用：

```bash
python solo_biz_discovery.py              # 完整交互流程
python solo_biz_discovery.py explore      # 仅自我探索
python solo_biz_discovery.py models       # 浏览商业模式库
python solo_biz_discovery.py examples     # 查看成功案例
python solo_biz_discovery.py plan         # 生成行动计划
```

CLI 版本使用纯规则匹配，不依赖 LLM API。

## 环境变量说明

| 变量 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `LLM_PROVIDER` | 否 | `gemini` | LLM 提供商，可选 `gemini` 或 `claude` |
| `GEMINI_API_KEY` | 否 | - | Google Gemini API Key |
| `ANTHROPIC_API_KEY` | 否 | - | Anthropic Claude API Key |
| `PORT` | 否 | `8000` | 服务端口（Railway 自动设置） |

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 前端页面 |
| GET | `/api/questions` | 获取问卷数据 |
| GET | `/api/models` | 获取商业模式库 |
| GET | `/api/examples` | 获取成功案例 |
| POST | `/api/analyze` | 提交答案，返回分析结果 |
| GET | `/api/status` | 检查 LLM 配置状态 |
