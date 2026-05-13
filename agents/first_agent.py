import json
from pathlib import Path
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


class AgentResponse(BaseModel):
    problem_summary: str
    domain: str
    agent_opportunity: str
    recommended_agent_type: str
    tools_needed: List[str]
    next_steps: List[str]
    risk_or_constraint: str
    confidence_score: float = Field(ge=0, le=1)


def load_system_prompt() -> str:
    prompt_path = Path("prompts/system_prompt.txt")
    return prompt_path.read_text(encoding="utf-8")


def run_first_agent(user_problem: str) -> AgentResponse:
    """Runs a simple first AI agent and returns structured output."""

    system_prompt = load_system_prompt()

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_problem}
        ],
        response_format={"type": "json_object"}
    )

    raw_output = response.choices[0].message.content

    try:
        parsed = json.loads(raw_output)
        return AgentResponse(**parsed)
    except Exception as e:
        raise ValueError(f"Agent returned invalid JSON. Error: {e}\nRaw output: {raw_output}")
