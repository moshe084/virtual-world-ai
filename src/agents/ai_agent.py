from typing import Dict, List, Optional, Any
from datetime import datetime
from .base_agent import Agent, Task
from ..ai_engines.base_engine import AIProvider, AIEngine

class AIAgent(Agent):
    def __init__(self, agent_id: str, ai_provider: AIProvider, ai_config: Dict[str, Any], skills: List[str], role: str):
        super().__init__(agent_id, skills, role)
        self.ai_engine = self._create_ai_engine(ai_provider, ai_config)
        self.memory: List[Dict[str, Any]] = []  # Agent's memory/history

    async def perform_task(self) -> bool:
        if not self.current_task:
            return False

        context = {
            "agent_role": self.role,
            "agent_skills": self.skills,
            "task_history": self.memory[-5:],  # Last 5 tasks
            "environment_state": self.get_environment_state()
        }

        try:
            result = await self.ai_engine.process_task(
                str(self.current_task.description),
                context
            )
            
            self.memory.append({
                "timestamp": datetime.now(),
                "task": self.current_task.description,
                "result": result,
                "success": True
            })
            return True
        except Exception as e:
            self.memory.append({
                "timestamp": datetime.now(),
                "task": self.current_task.description,
                "error": str(e),
                "success": False
            })
            return False

    def get_environment_state(self) -> Dict[str, Any]:
        return {
            "current_time": datetime.now(),
            "available_resources": {},
            "recent_events": []
        }