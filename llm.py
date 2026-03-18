"""
LLM abstraction layer supporting Gemini and Claude.
Provides a unified interface for generating personalized business model recommendations.
"""

import json
import os


def get_provider() -> str:
    """Get configured LLM provider. Defaults to gemini."""
    return os.environ.get("LLM_PROVIDER", "gemini").lower()


def is_available() -> bool:
    """Check if any LLM provider is configured."""
    provider = get_provider()
    if provider == "claude":
        return bool(os.environ.get("ANTHROPIC_API_KEY"))
    return bool(os.environ.get("GEMINI_API_KEY"))


def build_prompt(answers: dict, scored_models: list[dict]) -> str:
    """Build the analysis prompt from user answers and scored models."""
    answers_text = "\n".join(f"- {k}: {v}" for k, v in answers.items() if v)
    models_text = "\n".join(
        f"#{i+1} {m['name']}（匹配分: {m['score']}）— {m['description']}"
        for i, m in enumerate(scored_models[:3])
    )

    return f"""你是一位经验丰富的个人商业模式顾问。用户刚刚完成了一份自我探索问卷，以下是他们的回答和系统的初步匹配结果。

请基于这些信息，给出个性化的深度分析。

## 用户回答
{answers_text}

## 系统匹配的 Top 3 商业模式
{models_text}

## 请你输出以下内容（用中文）：

### 1. 个性化洞察
分析用户的技能、兴趣和痛点之间的交叉点，指出他们可能没意识到的商业机会。不要泛泛而谈，要具体到他们的情况。

### 2. 推荐的第一步
基于用户的时间和预算约束，给出一个具体的、可以在本周末就开始的行动。要足够具体，让用户读完就知道该做什么。

### 3. 风险提示
针对用户的具体情况，指出 1-2 个最可能踩的坑，以及如何避免。

### 4. 激励
用一句话鼓励用户迈出第一步。要真诚，不要鸡汤。

请直接输出分析内容，不要重复我的指令。保持简洁有力，总计不超过 500 字。"""


async def generate_recommendation(answers: dict, scored_models: list[dict]) -> str:
    """Generate personalized recommendation using configured LLM."""
    provider = get_provider()
    prompt = build_prompt(answers, scored_models)

    if provider == "claude":
        return await _call_claude(prompt)
    else:
        return await _call_gemini(prompt)


async def _call_gemini(prompt: str) -> str:
    """Call Gemini API."""
    from google import genai

    api_key = os.environ.get("GEMINI_API_KEY", "")
    client = genai.Client(api_key=api_key)

    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


async def _call_claude(prompt: str) -> str:
    """Call Claude API."""
    import anthropic

    client = anthropic.AsyncAnthropic()

    message = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text
