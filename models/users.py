from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id: int, name: str):
        self.__id = user_id        
        self.__name = name         

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_role_info(self) -> str:
        pass

class Survivor(User):
    def __init__(self, user_id: int, name: str, trauma_type: str, mental_status: str):
        super().__init__(user_id, name)
        self.__trauma_type = trauma_type
        self.__mental_status = mental_status

    def get_mental_status(self) -> str:
        return self.__mental_status

    def get_role_info(self) -> str:
        return f"[SURVIVOR] {self.name} | Trauma: {self.__trauma_type} | Status: {self.__mental_status}"