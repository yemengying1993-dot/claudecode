"""
Solo Business Model Discovery Tool — Web API
FastAPI backend serving the questionnaire, analysis, and frontend.
"""

import os
import traceback

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from data import (
    BUSINESS_MODELS,
    EXPLORE_QUESTIONS,
    SEVEN_DAY_PLANS,
    SUCCESS_CASES,
    VALIDATION_CHECKLIST,
)
import llm

app = FastAPI(title="Solo Biz Discovery", version="1.0.0")


# ─────────────────────────────────────────────
# Scoring logic (ported from CLI version)
# ─────────────────────────────────────────────

KEYWORD_TAGS = {
    "程序": ["coding", "automation", "problem_solving"],
    "开发": ["coding", "automation", "problem_solving"],
    "工程师": ["coding", "automation", "problem_solving"],
    "设计": ["design", "creativity"],
    "美术": ["design", "creativity"],
    "UI": ["design", "creativity"],
    "教": ["teaching", "writing"],
    "培训": ["teaching", "writing"],
    "老师": ["teaching", "writing"],
    "写": ["writing", "creativity"],
    "文案": ["writing", "creativity"],
    "编辑": ["writing", "creativity"],
    "翻译": ["language", "writing"],
    "英语": ["language", "writing"],
    "外语": ["language", "writing"],
    "营销": ["marketing", "community_building"],
    "运营": ["marketing", "community_building"],
    "推广": ["marketing", "community_building"],
    "销售": ["marketing", "networking"],
    "数据": ["data_analysis", "coding"],
    "分析": ["data_analysis", "problem_solving"],
    "AI": ["ai_tools", "automation"],
    "人工智能": ["ai_tools", "automation"],
    "GPT": ["ai_tools", "automation"],
    "咨询": ["consulting", "networking"],
    "顾问": ["consulting", "networking"],
    "金融": ["consulting", "data_analysis"],
    "财务": ["consulting", "data_analysis"],
    "法律": ["consulting", "expertise"],
    "医": ["expertise", "teaching"],
    "视频": ["creativity", "entertainment", "speaking"],
    "剪辑": ["creativity", "entertainment"],
    "拍摄": ["creativity", "speaking"],
    "摄影": ["design", "creativity"],
    "音乐": ["creativity", "entertainment"],
    "画": ["design", "creativity"],
    "插画": ["design", "creativity"],
    "PPT": ["design", "teaching"],
    "Excel": ["data_analysis", "teaching"],
    "电商": ["marketing", "trend_sense"],
    "产品": ["problem_solving", "design"],
    "管理": ["consulting", "networking"],
}


def collect_tags(answers: dict) -> list[str]:
    """Extract tags from user answers using keyword matching."""
    tags = set()
    text_keys = [
        "background", "asked_skills", "teach_skill",
        "hobby", "flow_activity", "online_interest",
        "pain_point", "money_spent", "wished_tool",
    ]
    combined = " ".join(answers.get(k, "") for k in text_keys)
    for keyword, tag_list in KEYWORD_TAGS.items():
        if keyword in combined:
            tags.update(tag_list)
    return list(tags)


def score_models(tags: list[str], answers: dict) -> list[dict]:
    """Score business models based on tags and user constraints."""
    scored = []
    time_val = answers.get("time_available", "")
    budget_val = answers.get("budget", "")
    income_val = answers.get("income_preference", "")

    for model in BUSINESS_MODELS:
        score = 0
        for tag in tags:
            if tag in model["fit_tags"]:
                score += 10
        # Time
        if "5小时以下" in time_val:
            if model["id"] in ["knowledge_product", "ecommerce"]:
                score += 5
        elif "全职" in time_val:
            score += 3
        # Budget
        if "0元" in budget_val:
            if model["id"] in ["freelance_service", "content_creator", "community"]:
                score += 5
        # Income preference
        if "快速" in income_val:
            if model["id"] in ["freelance_service", "ai_service"]:
                score += 8
        elif "长期" in income_val:
            if model["id"] in ["saas_tool", "content_creator"]:
                score += 8

        scored.append({**model, "score": score})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored


# ─────────────────────────────────────────────
# API routes
# ─────────────────────────────────────────────

@app.get("/")
async def index():
    return FileResponse("templates/index.html")


@app.get("/api/questions")
async def get_questions():
    return EXPLORE_QUESTIONS


@app.get("/api/models")
async def get_models():
    return BUSINESS_MODELS


@app.get("/api/examples")
async def get_examples():
    return SUCCESS_CASES


class AnalyzeRequest(BaseModel):
    answers: dict


@app.post("/api/analyze")
async def analyze(req: AnalyzeRequest):
    answers = req.answers

    # 1. Tag extraction & scoring
    tags = collect_tags(answers)
    scored = score_models(tags, answers)
    top3 = scored[:3]

    # 2. Get 7-day plan for best match
    best_id = top3[0]["id"]
    plan = SEVEN_DAY_PLANS.get(best_id, SEVEN_DAY_PLANS["freelance_service"])

    # 3. LLM analysis (if available)
    llm_analysis = None
    if llm.is_available():
        try:
            llm_analysis = await llm.generate_recommendation(answers, top3)
        except Exception as e:
            traceback.print_exc()
            llm_analysis = f"AI 分析暂时不可用（{type(e).__name__}），以下为规则匹配结果。"
    else:
        llm_analysis = "未配置 AI API Key，显示规则匹配结果。配置 GEMINI_API_KEY 或 ANTHROPIC_API_KEY 可获得个性化深度分析。"

    return {
        "top_models": top3,
        "seven_day_plan": plan,
        "llm_analysis": llm_analysis,
        "checklist": VALIDATION_CHECKLIST,
        "tags": tags,
    }


@app.get("/api/status")
async def status():
    provider = llm.get_provider()
    return {
        "llm_provider": provider,
        "llm_available": llm.is_available(),
    }
