from abc import ABC, abstractmethod
from models.users import User 

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, user: User, message: str) -> None:
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, user: User, message: str) -> None:
        print(f"\n[EMAIL SENT] To: {user.name} | Body: {message}")