"""
Static data for Solo Business Model Discovery Tool.
Business models, exploration questions, success cases, and 7-day plans.
"""

BUSINESS_MODELS = [
    {
        "id": "knowledge_product",
        "name": "知识产品型",
        "icon": "📚",
        "description": "把你的专业知识打包成课程、电子书、模板等数字产品",
        "examples": [
            "在线课程（Udemy、自建平台）",
            "电子书 / PDF 指南",
            "Notion / Excel 模板",
            "付费 Newsletter",
        ],
        "first_dollar": "写一份解决具体问题的 PDF 指南，定价 9.9 元，在社交媒体推广",
        "fit_tags": ["writing", "teaching", "expertise"],
        "effort": "低启动成本，中等内容制作时间",
        "scalability": "高 — 一次制作，无限销售",
        "role_models": [
            "Justin Welsh — LinkedIn 个人品牌 + 数字产品，年入 $5M+",
            "Ali Abdaal — YouTube 教育内容 + 课程，年入 $4M+",
        ],
    },
    {
        "id": "freelance_service",
        "name": "自由职业服务型",
        "icon": "💼",
        "description": "用你的技能直接为客户提供服务，最快的变现路径",
        "examples": [
            "设计 / 开发外包",
            "咨询顾问",
            "翻译 / 写作",
            "AI 工具定制",
        ],
        "first_dollar": "在自由职业平台（Upwork/Fiverr/猪八戒）上接一单小项目",
        "fit_tags": ["coding", "design", "consulting", "language"],
        "effort": "零启动成本，立即开始",
        "scalability": "中 — 受限于你的时间，但可以逐步产品化",
        "role_models": [
            "众多自由开发者 — 从接单到建立长期客户关系",
            "税务/法律顾问 OPC — 用 AI 提效，客单价提升 3 倍",
        ],
    },
    {
        "id": "saas_tool",
        "name": "SaaS 工具型",
        "icon": "🔧",
        "description": "开发一个解决特定问题的小工具，按月订阅收费",
        "examples": [
            "Chrome 插件",
            "API 服务",
            "垂直领域小工具",
            "AI Wrapper 应用",
        ],
        "first_dollar": "找到一个你自己每天都在手动做的重复工作，把它自动化，然后卖给同行",
        "fit_tags": ["coding", "automation", "problem_solving"],
        "effort": "中等启动成本，需要开发时间",
        "scalability": "非常高 — 订阅收入，自动运行",
        "role_models": [
            "Pieter Levels — Nomad List / RemoteOK，一人运营",
            "杭州 95 后 — 5 个月上线 120+ 出海 APP，90% 有付费转化",
        ],
    },
    {
        "id": "content_creator",
        "name": "内容创作型",
        "icon": "🎬",
        "description": "通过持续输出内容建立影响力，用广告、赞助、带货变现",
        "examples": [
            "YouTube / B站 视频",
            "播客",
            "公众号 / 博客",
            "小红书种草",
        ],
        "first_dollar": "选一个你有话说的垂直领域，坚持发 30 条内容，开通创作者收益",
        "fit_tags": ["writing", "speaking", "creativity", "entertainment"],
        "effort": "零启动成本，但需要持续投入",
        "scalability": "高 — 内容资产累积，复利效应",
        "role_models": [
            "Dan Koe — 个人品牌内容矩阵，年入 $5M+，利润率 98%",
            "Ali Abdaal — 从医学生 YouTuber 到教育企业家",
        ],
    },
    {
        "id": "ecommerce",
        "name": "电商/跨境型",
        "icon": "🛒",
        "description": "发现产品需求，通过电商平台或独立站销售",
        "examples": [
            "Shopify 独立站",
            "亚马逊/速卖通",
            "POD（按需印刷）",
            "数字下载商品",
        ],
        "first_dollar": "用 POD 服务设计一款 T 恤/手机壳，零库存开卖",
        "fit_tags": ["design", "marketing", "trend_sense", "data_analysis"],
        "effort": "低启动成本（POD），有一定学习曲线",
        "scalability": "高 — 可以不断扩品类",
        "role_models": [
            "深圳 3C 配件 OPC — 用 AI 分析海外偏好，单款产品月销超 10 万件",
            "沪咪科技 — 跨境直播，入驻 4 个月卖毛毯到日本，季度销售额 500 万+",
        ],
    },
    {
        "id": "community",
        "name": "社群/会员型",
        "icon": "👥",
        "description": "围绕一个主题建立付费社群，提供持续价值",
        "examples": [
            "知识星球",
            "Discord / Telegram 付费群",
            "会员制 Newsletter",
            "Mastermind 小组",
        ],
        "first_dollar": "免费社群积累 100 人，提供一次付费分享（定价 19.9 元）",
        "fit_tags": ["networking", "teaching", "community_building"],
        "effort": "低启动成本，需要持续运营",
        "scalability": "中高 — 社群规模有天花板，但忠诚度高",
        "role_models": [
            "众多知识星球主 — 垂直领域付费社群，年入数十万到数百万",
        ],
    },
    {
        "id": "ai_service",
        "name": "AI 赋能服务型",
        "icon": "🤖",
        "description": "用 AI 工具 10 倍提效传统服务，赚取效率差价",
        "examples": [
            "AI 辅助设计（Logo、海报）",
            "AI 内容批量生产",
            "AI 数据分析报告",
            "AI 客服/聊天机器人搭建",
        ],
        "first_dollar": "用 AI 帮一个小企业主做他花 5000 元外包的事，收费 2000 元",
        "fit_tags": ["ai_tools", "automation", "consulting"],
        "effort": "低启动成本，需要学习 AI 工具",
        "scalability": "高 — AI 处理大部分工作，你只需管理",
        "role_models": [
            "佛山服装店 OPC — AI 生成脚本话术，6 个月复购率 82%",
            "AI 择校工具'选校鸟' — 从想法到落地仅 2 个月",
        ],
    },
]

EXPLORE_QUESTIONS = [
    {
        "section": "技能与经验",
        "icon": "🎯",
        "questions": [
            {
                "q": "你的职业/专业背景是什么？",
                "hint": "如：程序员、设计师、教师、学生、运营...",
                "key": "background",
                "type": "text",
            },
            {
                "q": "你有哪些别人经常向你请教的技能？",
                "hint": "如：修电脑、做PPT、拍照、化妆、理财...",
                "key": "asked_skills",
                "type": "text",
            },
            {
                "q": "如果有人付你钱让你教他们一件事，你会教什么？",
                "hint": "不用想太多，第一个浮现在脑海的答案",
                "key": "teach_skill",
                "type": "text",
            },
        ],
    },
    {
        "section": "兴趣与热情",
        "icon": "❤️",
        "questions": [
            {
                "q": "你在空闲时间最喜欢做什么？",
                "hint": "不为赚钱，纯粹享受的事",
                "key": "hobby",
                "type": "text",
            },
            {
                "q": "你能连续几小时做而不觉得累的事情是什么？",
                "hint": "这通常暗示你的天赋所在",
                "key": "flow_activity",
                "type": "text",
            },
            {
                "q": "你在网上最常浏览/搜索什么类型的内容？",
                "hint": "如：科技新闻、美食、投资、游戏攻略...",
                "key": "online_interest",
                "type": "text",
            },
        ],
    },
    {
        "section": "问题与痛点",
        "icon": "🔍",
        "questions": [
            {
                "q": "你生活/工作中最大的痛点是什么？",
                "hint": "你自己的问题往往也是别人的问题",
                "key": "pain_point",
                "type": "text",
            },
            {
                "q": "你最近花钱解决了什么问题？觉得值吗？",
                "hint": "愿意付费的地方就有商机",
                "key": "money_spent",
                "type": "text",
            },
            {
                "q": "如果有一个工具/服务能帮你解决一件事，你希望它是什么？",
                "hint": "这可能就是你的第一个产品创意",
                "key": "wished_tool",
                "type": "text",
            },
        ],
    },
    {
        "section": "资源与约束",
        "icon": "⚖️",
        "questions": [
            {
                "q": "你每周能投入多少小时在副业上？",
                "key": "time_available",
                "type": "choice",
                "options": ["5小时以下", "5-10小时", "10-20小时", "20小时以上（全职）"],
            },
            {
                "q": "你能接受的初始投入是多少？",
                "key": "budget",
                "type": "choice",
                "options": ["0元（纯时间投入）", "500元以下", "500-5000元", "5000元以上"],
            },
            {
                "q": "你更倾向哪种收入模式？",
                "key": "income_preference",
                "type": "choice",
                "options": [
                    "快速见到第一笔收入（哪怕很少）",
                    "愿意投入 3-6 个月换取更大回报",
                    "长期布局，1年后看结果",
                ],
            },
        ],
    },
]

SUCCESS_CASES = [
    {
        "name": "Dan Koe",
        "region": "海外",
        "flag": "🌍",
        "model": "内容创作 + 知识产品",
        "story": "通过个人品牌内容矩阵（Twitter、YouTube、Newsletter），年入超 $5M，利润率 98%。",
        "lesson": "你不需要成为专家，只需要比你的目标用户多懂一点。",
    },
    {
        "name": "Pieter Levels",
        "region": "海外",
        "flag": "🌍",
        "model": "SaaS 工具型",
        "story": "独自运营 Nomad List 和 RemoteOK，月入数十万美元。最初只是一个 Google 表格。",
        "lesson": "先用最简单的方式验证需求，再逐步构建产品。",
    },
    {
        "name": "Justin Welsh",
        "region": "海外",
        "flag": "🌍",
        "model": "LinkedIn 个人品牌 + 数字产品",
        "story": "从企业高管辞职后，通过 LinkedIn 内容建立个人品牌，销售在线课程和模板，年入 $5M+。",
        "lesson": "选一个平台深耕，而不是到处撒网。",
    },
    {
        "name": "杭州 95 后开发者",
        "region": "国内",
        "flag": "🇨🇳",
        "model": "AI + 出海 APP",
        "story": "1997 年出生，职高毕业。借助 AI 面向海外批量开发 APP，5 个月上线 120+ 应用，90% 有付费转化。",
        "lesson": "不需要名校背景，用 AI 工具降低技术门槛，关键是快速试错和迭代。",
    },
    {
        "name": "佛山服装店 OPC",
        "region": "国内",
        "flag": "🇨🇳",
        "model": "AI 赋能服务型",
        "story": "用 AI 生成脚本与话术，靠微信生态实现'展示-咨询-复购'闭环，6 个月复购率达 82%。",
        "lesson": "传统行业 + AI = 降维打击。不一定要做全新的事，把旧的事做出新效率就行。",
    },
    {
        "name": "'选校鸟' — 李涛",
        "region": "国内",
        "flag": "🇨🇳",
        "model": "AI 工具型",
        "story": "AI 择校工具，从想法到落地仅 2 个月。传统模式下同类产品需要 6-12 个月、5-10 人团队。",
        "lesson": "找到一个具体的、可验证的需求，用 AI 快速构建 MVP。",
    },
]

SEVEN_DAY_PLANS = {
    "knowledge_product": {
        "Day 1": "🔍 确定主题 — 回顾你的技能，选一个你能教别人的具体主题",
        "Day 2": "👤 用户研究 — 在社交媒体/论坛搜索相关问题，确认有人需要这个知识",
        "Day 3": "📝 内容大纲 — 列出解决这个问题的 5-10 个关键步骤",
        "Day 4": "✍️ 写作/录制 — 完成第一版内容（PDF/视频/文章）",
        "Day 5": "🎨 打包定价 — 设计封面，定价（建议 9.9-49 元起步）",
        "Day 6": "📢 发布推广 — 在朋友圈/社交媒体发布，附上购买链接",
        "Day 7": "📊 复盘优化 — 收集反馈，记录数据，规划下一步",
    },
    "freelance_service": {
        "Day 1": "📋 技能清单 — 列出你能提供的所有服务，选最擅长的 1-2 个",
        "Day 2": "🏪 开店/注册 — 在 Upwork/Fiverr/猪八戒/闲鱼注册服务",
        "Day 3": "💎 作品集 — 做 2-3 个样本作品展示你的能力",
        "Day 4": "📢 主动出击 — 发送 10 个报价/申请，或发朋友圈告知你在接单",
        "Day 5": "🤝 跟进沟通 — 回复询问，调整报价策略",
        "Day 6": "🚀 交付第一单 — 超预期完成，请求好评和推荐",
        "Day 7": "📊 复盘优化 — 分析什么有效，优化服务描述和定价",
    },
    "saas_tool": {
        "Day 1": "🔍 问题发现 — 列出你每天重复做的 5 件事，选最烦的一个",
        "Day 2": "🗣️ 需求验证 — 在社区/论坛问：'有多少人也有这个问题？'",
        "Day 3": "📐 MVP 设计 — 画出最简版本的功能（只保留核心 1 个功能）",
        "Day 4-5": "💻 快速开发 — 用最快的方式做出能用的版本",
        "Day 6": "🧪 找 5 个人试用 — 收集反馈，看他们愿不愿意付费",
        "Day 7": "💰 上线收费 — 定价，接入支付，正式发布",
    },
    "content_creator": {
        "Day 1": "🎯 定位 — 选择一个你有话说的垂直领域（越具体越好）",
        "Day 2": "📱 选平台 — 选 1 个主平台（小红书/B站/公众号/Twitter）",
        "Day 3": "📝 内容规划 — 列出 30 个你能写/拍的具体选题",
        "Day 4": "🎬 创作第一条 — 完成并发布第一条内容",
        "Day 5": "🎬 创作 2-3 条 — 保持发布节奏",
        "Day 6": "🎬 继续创作 — 同时研究平台算法和热门内容特征",
        "Day 7": "📊 数据复盘 — 分析哪条表现最好，为什么，继续这个方向",
    },
    "ecommerce": {
        "Day 1": "🔍 市场调研 — 浏览热门平台（小红书/TikTok），发现趋势产品",
        "Day 2": "🎯 选品 — 确定 1-2 个产品方向，分析竞品定价和销量",
        "Day 3": "🏭 供应链 — 联系供应商/注册 POD 服务（Printful、Redbubble 等）",
        "Day 4": "🎨 产品设计 — 用 AI 工具设计产品图片和描述",
        "Day 5": "🏪 开店上架 — 在平台/独立站上架产品",
        "Day 6": "📢 推广 — 社交媒体发布，或尝试小预算广告",
        "Day 7": "📊 复盘 — 分析流量和转化数据，调整策略",
    },
    "community": {
        "Day 1": "🎯 定主题 — 选一个你有热情的垂直话题",
        "Day 2": "🏠 建群 — 创建微信群/知识星球/Discord，写好群介绍",
        "Day 3": "👥 邀请种子用户 — 从朋友圈/社交媒体邀请前 20 人",
        "Day 4": "💎 提供价值 — 分享一篇干货内容或做一次小分享",
        "Day 5": "🗣️ 促进互动 — 发起讨论话题，让成员参与进来",
        "Day 6": "💰 试水变现 — 举办一次付费分享/问答（定价 9.9-19.9）",
        "Day 7": "📊 复盘规划 — 分析付费转化率，规划持续运营策略",
    },
    "ai_service": {
        "Day 1": "🔍 技能盘点 — 列出你会用的 AI 工具和你的专业领域",
        "Day 2": "🎯 找目标客户 — 谁在花大钱做你能用 AI 快速完成的事？",
        "Day 3": "📦 打包服务 — 定义具体服务内容和定价（比传统价格低 50-70%）",
        "Day 4": "💎 做案例 — 用 AI 做 2-3 个免费样本展示效果",
        "Day 5": "📢 主动找客户 — 发朋友圈、私信潜在客户、在相关社群推广",
        "Day 6": "🤝 接第一单 — 以优惠价完成，收集好评",
        "Day 7": "📊 复盘流程 — 把流程标准化，准备接更多单",
    },
}

VALIDATION_CHECKLIST = [
    "能用一句话说清楚你在帮谁解决什么问题",
    "至少找到 5 个有这个问题的人并跟他们聊过",
    "至少 1 个人表示愿意为你的解决方案付费",
    "你已经完成了最小可行产品（MVP）",
    "你已经赚到了第一块钱",
    "你找到了一个可重复的获客方式",
]
