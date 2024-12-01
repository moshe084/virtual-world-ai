from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from datetime import datetime

class Task:
    def __init__(self, task_id: str, description: str, required_skills: List[str]):
        self.id = task_id
        self.description = description
        self.required_skills = required_skills
        self.status = "pending"

class Agent(ABC):
    def __init__(self, agent_id: str, skills: List[str], role: str):
        self.id = agent_id
        self.skills = skills
        self.role = role
        self.current_task: Optional[Task] = None
        self.state = "idle"
        self.performance_metrics = {}

    @abstractmethod
    async def perform_task(self) -> bool:
        pass

    def can_perform_task(self, task: Task) -> bool:
        return all(skill in self.skills for skill in task.required_skills)

    def assign_task(self, task: Task) -> bool:
        if self.can_perform_task(task):
            self.current_task = task
            self.state = "working"
            return True
        return False