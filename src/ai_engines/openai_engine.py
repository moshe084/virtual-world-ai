import openai
from typing import Dict, List, Any
from .base_engine import AIEngine

class OpenAIEngine(AIEngine):
    def __init__(self, model: str = "gpt-4", api_key: str = None):
        self.model = model
        openai.api_key = api_key

    async def process_task(self, task: str, context: Dict[str, Any]) -> str:
        response = await openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an AI agent in a virtual world."},
                {"role": "user", "content": f"Task: {task}\nContext: {context}"}
            ]
        )
        return response.choices[0].message.content

    async def get_decision(self, situation: str, options: List[str]) -> str:
        options_text = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(options)])
        response = await openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Make a decision based on the situation."},
                {"role": "user", "content": f"Situation: {situation}\nOptions:\n{options_text}"}
            ]
        )
        return response.choices[0].message.content