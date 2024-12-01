from anthropic import Anthropic
from typing import Dict, List, Any
from .base_engine import AIEngine

class ClaudeEngine(AIEngine):
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key)

    async def process_task(self, task: str, context: Dict[str, Any]) -> str:
        response = await self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"Task: {task}\nContext: {context}"
            }]
        )
        return response.content[0].text

    async def get_decision(self, situation: str, options: List[str]) -> str:
        options_text = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(options)])
        response = await self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"Situation: {situation}\nOptions:\n{options_text}"
            }]
        )
        return response.content[0].text