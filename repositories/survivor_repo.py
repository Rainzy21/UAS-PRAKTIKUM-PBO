from abc import ABC, abstractmethod
from typing import List, Optional
from models.users import Survivor

class ISurvivorRepository(ABC):
    @abstractmethod
    def save(self, survivor: Survivor) -> None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[Survivor]:
        pass

    @abstractmethod
    def get_all(self) -> List[Survivor]:
        pass

class InMemorySurvivorRepository(ISurvivorRepository):
    def __init__(self):
        self._storage = []

    def save(self, survivor: Survivor) -> None:
        self._storage.append(survivor)

    def find_by_id(self, user_id: int) -> Optional[Survivor]:
        for s in self._storage:
            if s.id == user_id:
                return s
        return None

    def get_all(self) -> List[Survivor]:
        return self._storage