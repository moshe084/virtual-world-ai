from abc import ABC, abstractmethod
from typing import Dict, List, Any
from enum import Enum

class AIProvider(Enum):
    OPENAI = "openai"
    OPENAI_ASSISTANT = "openai_assistant"
    CLAUDE = "claude"
    GEMINI = "gemini"

class AIEngine(ABC):
    @abstractmethod
    async def process_task(self, task: str, context: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    async def get_decision(self, situation: str, options: List[str]) -> str:
        pass