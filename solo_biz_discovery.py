#!/usr/bin/env python3
"""
Solo Business Model Discovery Tool (一人公司商业模式发现工具)

帮助你从"不知道做什么"走到"可以先试这个"。
通过结构化的自我探索、市场匹配和行动计划生成，
找到适合你的一人公司商业模式。

Usage:
    python solo_biz_discovery.py              # 完整流程
    python solo_biz_discovery.py explore      # 仅自我探索
    python solo_biz_discovery.py models       # 浏览商业模式库
    python solo_biz_discovery.py plan         # 从已有档案生成行动计划
    python solo_biz_discovery.py examples     # 查看成功案例
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# 数据：商业模式库
# ─────────────────────────────────────────────

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

# ─────────────────────────────────────────────
# 数据：自我探索问题库
# ─────────────────────────────────────────────

EXPLORE_QUESTIONS = [
    {
        "section": "技能与经验",
        "icon": "🎯",
        "questions": [
            {
                "q": "你的职业/专业背景是什么？（如：程序员、设计师、教师、学生...）",
                "key": "background",
                "tags_map": {
                    "程序": ["coding", "automation", "problem_solving"],
                    "开发": ["coding", "automation", "problem_solving"],
                    "设计": ["design", "creativity"],
                    "教": ["teaching", "writing"],
                    "写": ["writing", "creativity"],
                    "翻译": ["language", "writing"],
                    "营销": ["marketing", "community_building"],
                    "销售": ["marketing", "networking"],
                    "数据": ["data_analysis", "coding"],
                    "AI": ["ai_tools", "automation"],
                    "咨询": ["consulting", "networking"],
                    "金融": ["consulting", "data_analysis"],
                    "法律": ["consulting", "expertise"],
                    "医": ["expertise", "teaching"],
                },
            },
            {
                "q": "你有哪些别人经常向你请教的技能？（如：修电脑、做PPT、拍照...）",
                "key": "asked_skills",
                "tags_map": {},
            },
            {
                "q": "如果有人付你钱让你教他们一件事，你会教什么？",
                "key": "teach_skill",
                "tags_map": {},
            },
        ],
    },
    {
        "section": "兴趣与热情",
        "icon": "❤️",
        "questions": [
            {
                "q": "你在空闲时间最喜欢做什么？（不为赚钱，纯粹享受的事）",
                "key": "hobby",
                "tags_map": {},
            },
            {
                "q": "你能连续几小时做而不觉得累的事情是什么？",
                "key": "flow_activity",
                "tags_map": {},
            },
            {
                "q": "你在网上最常浏览/搜索什么类型的内容？",
                "key": "online_interest",
                "tags_map": {},
            },
        ],
    },
    {
        "section": "问题与痛点",
        "icon": "🔍",
        "questions": [
            {
                "q": "你生活/工作中最大的痛点是什么？（你自己的问题往往也是别人的问题）",
                "key": "pain_point",
                "tags_map": {},
            },
            {
                "q": "你最近花钱解决了什么问题？觉得值吗？",
                "key": "money_spent",
                "tags_map": {},
            },
            {
                "q": "如果有一个工具/服务能帮你解决一件事，你希望它是什么？",
                "key": "wished_tool",
                "tags_map": {},
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
                "options": ["5小时以下", "5-10小时", "10-20小时", "20小时以上（全职）"],
            },
            {
                "q": "你能接受的初始投入是多少？",
                "key": "budget",
                "options": ["0元（纯时间投入）", "500元以下", "500-5000元", "5000元以上"],
            },
            {
                "q": "你更倾向哪种收入模式？",
                "key": "income_preference",
                "options": [
                    "快速见到第一笔收入（哪怕很少）",
                    "愿意投入 3-6 个月换取更大回报",
                    "长期布局，1年后看结果",
                ],
            },
        ],
    },
]

# ─────────────────────────────────────────────
# 核心逻辑
# ─────────────────────────────────────────────

DATA_DIR = Path.home() / ".solo_biz"
PROFILE_FILE = DATA_DIR / "profile.json"


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_profile(profile: dict):
    ensure_data_dir()
    profile["updated_at"] = datetime.now().isoformat()
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)


def load_profile() -> dict:
    if PROFILE_FILE.exists():
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def print_header(text: str, width: int = 60):
    print()
    print("=" * width)
    print(f"  {text}")
    print("=" * width)


def print_subheader(text: str):
    print(f"\n--- {text} ---\n")


def ask_input(prompt: str, default: str = "") -> str:
    """获取用户输入"""
    if default:
        result = input(f"  {prompt} [{default}]: ").strip()
        return result if result else default
    result = input(f"  {prompt}: ").strip()
    return result


def ask_choice(prompt: str, options: list[str]) -> str:
    """让用户选择"""
    print(f"\n  {prompt}")
    for i, opt in enumerate(options, 1):
        print(f"    [{i}] {opt}")
    while True:
        choice = input(f"  请选择 (1-{len(options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"  请输入 1 到 {len(options)} 之间的数字")


def collect_tags(answers: dict) -> list[str]:
    """从答案中提取标签"""
    tags = []
    for section in EXPLORE_QUESTIONS:
        for q_data in section["questions"]:
            key = q_data["key"]
            answer = answers.get(key, "")
            if not answer:
                continue
            # 从 tags_map 匹配
            for keyword, tag_list in q_data.get("tags_map", {}).items():
                if keyword in answer:
                    tags.extend(tag_list)
    return list(set(tags))


def score_models(tags: list[str], answers: dict) -> list[dict]:
    """根据标签和答案对商业模式评分"""
    scored = []
    time = answers.get("time_available", "")
    budget = answers.get("budget", "")
    income_pref = answers.get("income_preference", "")

    for model in BUSINESS_MODELS:
        score = 0

        # 标签匹配
        for tag in tags:
            if tag in model["fit_tags"]:
                score += 10

        # 时间匹配
        if "5小时以下" in time:
            if model["id"] in ["knowledge_product", "ecommerce"]:
                score += 5
        elif "全职" in time:
            score += 3  # 全职什么都能做

        # 预算匹配
        if "0元" in budget:
            if model["id"] in ["freelance_service", "content_creator", "community"]:
                score += 5

        # 收入偏好匹配
        if "快速" in income_pref:
            if model["id"] in ["freelance_service", "ai_service"]:
                score += 8
        elif "长期" in income_pref:
            if model["id"] in ["saas_tool", "content_creator"]:
                score += 8

        scored.append({**model, "score": score})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored


# ─────────────────────────────────────────────
# 命令：自我探索
# ─────────────────────────────────────────────

def cmd_explore():
    print_header("🔭 自我探索 — 发现你的商业潜力")
    print("\n  接下来我会问你一系列问题，没有对错之分。")
    print("  尽量具体地回答，这会帮助工具更好地匹配商业模式。")
    print("  如果某个问题不确定，可以直接回车跳过。\n")

    answers = {}
    profile = load_profile()

    for section in EXPLORE_QUESTIONS:
        print_subheader(f"{section['icon']} {section['section']}")
        for q_data in section["questions"]:
            old_answer = profile.get("answers", {}).get(q_data["key"], "")
            if "options" in q_data:
                answer = ask_choice(q_data["q"], q_data["options"])
            else:
                answer = ask_input(q_data["q"], default=old_answer)
            if answer:
                answers[q_data["key"]] = answer

    # 保存
    tags = collect_tags(answers)
    profile["answers"] = answers
    profile["tags"] = tags
    save_profile(profile)

    print_header("✅ 探索完成！你的档案已保存")
    print(f"\n  识别到的标签: {', '.join(tags) if tags else '（需要更多信息来匹配）'}")
    print(f"  档案位置: {PROFILE_FILE}")
    print("\n  下一步：运行 python solo_biz_discovery.py plan 生成你的行动计划")

    return answers, tags


# ─────────────────────────────────────────────
# 命令：浏览商业模式库
# ─────────────────────────────────────────────

def cmd_models():
    print_header("📖 一人公司商业模式库")

    for model in BUSINESS_MODELS:
        print(f"\n  {model['icon']} {model['name']}")
        print(f"     {model['description']}")
        print(f"     启动难度: {model['effort']}")
        print(f"     可扩展性: {model['scalability']}")
        print(f"     赚到第一块钱: {model['first_dollar']}")
        print(f"     案例:")
        for example in model["examples"]:
            print(f"       • {example}")

    print("\n" + "-" * 60)
    print("  提示：运行 python solo_biz_discovery.py explore 来找到最适合你的模式")


# ─────────────────────────────────────────────
# 命令：查看成功案例
# ─────────────────────────────────────────────

def cmd_examples():
    print_header("🌟 一人公司成功案例")

    cases = [
        {
            "name": "Dan Koe",
            "region": "🌍 海外",
            "model": "内容创作 + 知识产品",
            "story": "通过个人品牌内容矩阵（Twitter、YouTube、Newsletter），"
                     "年入超 $5M，利润率 98%。核心理念：个人兴趣与知识组合可以直接转化为商业模式。",
            "lesson": "你不需要成为专家，只需要比你的目标用户多懂一点。",
        },
        {
            "name": "Pieter Levels",
            "region": "🌍 海外",
            "model": "SaaS 工具型",
            "story": "独自运营 Nomad List 和 RemoteOK，月入数十万美元。"
                     "座右铭：'Automate, don't delegate.'（自动化，而非委托）",
            "lesson": "先用最简单的方式验证需求（他最初只是一个 Google 表格），再逐步构建产品。",
        },
        {
            "name": "Justin Welsh",
            "region": "🌍 海外",
            "model": "LinkedIn 个人品牌 + 数字产品",
            "story": "从企业高管辞职后，通过 LinkedIn 内容建立个人品牌，"
                     "销售在线课程和模板，年入 $5M+。",
            "lesson": "选一个平台深耕，而不是到处撒网。",
        },
        {
            "name": "杭州 95 后开发者",
            "region": "🇨🇳 国内",
            "model": "AI + 出海 APP",
            "story": "1997 年出生，职高毕业。2025 年 8 月开始借助 AI 面向海外批量开发 APP，"
                     "5 个月上线 120+ 应用，90% 有付费转化。",
            "lesson": "不需要名校背景，用 AI 工具降低技术门槛，关键是快速试错和迭代。",
        },
        {
            "name": "佛山服装店 OPC",
            "region": "🇨🇳 国内",
            "model": "AI 赋能服务型",
            "story": "用 AI 生成脚本与话术，靠微信生态实现'展示-咨询-复购'闭环，"
                     "6 个月复购率达 82%。",
            "lesson": "传统行业 + AI = 降维打击。不一定要做全新的事，把旧的事做出新效率就行。",
        },
        {
            "name": "'选校鸟' — 李涛",
            "region": "🇨🇳 国内",
            "model": "AI 工具型",
            "story": "AI 择校工具，从想法到落地仅 2 个月。"
                     "传统模式下同类产品需要 6-12 个月、5-10 人团队。",
            "lesson": "找到一个具体的、可验证的需求，用 AI 快速构建 MVP。",
        },
    ]

    for case in cases:
        print(f"\n  {case['region']} {case['name']}")
        print(f"     模式: {case['model']}")
        print(f"     故事: {case['story']}")
        print(f"     💡 启示: {case['lesson']}")

    print()


# ─────────────────────────────────────────────
# 命令：生成行动计划
# ─────────────────────────────────────────────

def cmd_plan():
    profile = load_profile()

    if not profile.get("answers"):
        print("\n  ⚠️  还没有做自我探索！先运行: python solo_biz_discovery.py explore")
        print("  或者现在开始？(y/n)")
        if input("  > ").strip().lower() in ("y", "yes", "是"):
            answers, tags = cmd_explore()
        else:
            return
    else:
        answers = profile["answers"]
        tags = profile.get("tags", [])

    print_header("🎯 你的个性化商业模式匹配报告")

    # 展示核心发现
    print_subheader("📋 你的核心信息")
    key_fields = [
        ("background", "职业背景"),
        ("asked_skills", "别人常请教你"),
        ("teach_skill", "你能教的技能"),
        ("flow_activity", "心流活动"),
        ("pain_point", "痛点"),
        ("time_available", "可用时间"),
        ("budget", "预算"),
        ("income_preference", "收入偏好"),
    ]
    for key, label in key_fields:
        val = answers.get(key)
        if val:
            print(f"  {label}: {val}")

    # 模式匹配
    scored = score_models(tags, answers)
    top3 = scored[:3]

    print_subheader("🏆 最适合你的 Top 3 商业模式")
    for i, model in enumerate(top3, 1):
        print(f"\n  #{i} {model['icon']} {model['name']} (匹配度: {'⭐' * min(5, max(1, model['score'] // 5))})")
        print(f"      {model['description']}")
        print(f"      可扩展性: {model['scalability']}")
        if model.get("role_models"):
            print(f"      参考案例:")
            for rm in model["role_models"]:
                print(f"        • {rm}")

    # 赚到第一块钱的行动计划
    best = top3[0]
    print_subheader(f"💰 赚到第一块钱 — {best['name']}行动计划")

    print(f"  推荐模式: {best['icon']} {best['name']}")
    print(f"  核心策略: {best['first_dollar']}")
    print()

    # 根据最佳匹配生成具体的 7 天计划
    plans = generate_7day_plan(best, answers)
    print("  📅 7 天行动计划:")
    print()
    for day, task in plans.items():
        print(f"  {day}: {task}")

    # 验证清单
    print_subheader("✅ 商业模式验证清单")
    checklist = [
        "[ ] 能用一句话说清楚你在帮谁解决什么问题",
        "[ ] 至少找到 5 个有这个问题的人并跟他们聊过",
        "[ ] 至少 1 个人表示愿意为你的解决方案付费",
        "[ ] 你已经完成了最小可行产品（MVP）",
        "[ ] 你已经赚到了第一块钱",
        "[ ] 你找到了一个可重复的获客方式",
    ]
    for item in checklist:
        print(f"  {item}")

    # 保存计划
    profile["recommended_model"] = best["id"]
    profile["plan_generated_at"] = datetime.now().isoformat()
    save_profile(profile)

    print(f"\n  💾 报告已保存到: {PROFILE_FILE}")
    print("\n  记住：完美是行动的敌人。先做出来，再做好。")
    print("  赚到第一块钱比想出完美计划重要 100 倍。\n")


def generate_7day_plan(model: dict, answers: dict) -> dict:
    """根据匹配的模式和用户答案生成 7 天计划"""
    model_id = model["id"]

    base_plans = {
        "knowledge_product": {
            "Day 1": "🔍 确定主题 — 回顾你的技能，选一个你能教别人的具体主题",
            "Day 2": "👤 用户研究 — 在社交媒体/论坛搜索相关问题，确认有人需要这个知识",
            "Day 3": "📝 内容大纲 — 列出解决这个问题的 5-10 个关键步骤",
            "Day 4": "✍️  写作/录制 — 完成第一版内容（PDF/视频/文章）",
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

    return base_plans.get(model_id, base_plans["freelance_service"])


# ─────────────────────────────────────────────
# 命令：完整流程
# ─────────────────────────────────────────────

def cmd_full():
    print_header("🚀 一人公司商业模式发现工具")
    print()
    print("  欢迎！这个工具会帮你：")
    print("  1. 探索你的技能、兴趣和资源")
    print("  2. 匹配最适合你的商业模式")
    print("  3. 生成赚到第一块钱的行动计划")
    print()
    print("  整个过程大约需要 10 分钟。准备好了吗？")
    print()

    ready = input("  按 Enter 开始，或输入 q 退出: ").strip()
    if ready.lower() == "q":
        return

    cmd_explore()
    print("\n  现在让我根据你的回答生成个性化的行动计划...\n")
    cmd_plan()


# ─────────────────────────────────────────────
# 主入口
# ─────────────────────────────────────────────

def main():
    commands = {
        "explore": cmd_explore,
        "models": cmd_models,
        "plan": cmd_plan,
        "examples": cmd_examples,
    }

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in commands:
            commands[cmd]()
        elif cmd in ("-h", "--help", "help"):
            print(__doc__)
        else:
            print(f"  未知命令: {cmd}")
            print(__doc__)
    else:
        cmd_full()


if __name__ == "__main__":
    main()
