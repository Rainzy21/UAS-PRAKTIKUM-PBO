from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    """
    Abstract base class untuk semua tipe pengguna sistem.
    """
    def __init__(self, user_id: int, name: str):
        self.__id = user_id        # Private attribute
        self.__name = name         # Private attribute
        self.__created_at = datetime.now()  # Timestamp pembuatan user

    @property
    def id(self) -> int:
        """Getter untuk ID pengguna."""
        return self.__id

    @property
    def name(self) -> str:
        """Getter untuk nama pengguna."""
        return self.__name
    
    @property
    def created_at(self):
        return self.__created_at.strftime("%Y-%m-%d %H:%M:%S")

    @abstractmethod
    def get_role_info(self) -> str:
        pass

class Survivor(User):
    """
    Kelas turunan untuk merepresentasikan korban trauma dalam sistem.
    Mewarisi kelas User.
    """
    def __init__(self, user_id: int, name: str, trauma_type: str, mental_status: str):
        super().__init__(user_id, name)
        self.__trauma_type = trauma_type
        self.__mental_status = mental_status

    @property
    def mental_status(self) -> str:
        """Getter untuk status mental."""
        return self.__mental_status
    
    @mental_status.setter
    def mental_status(self, value: str):
        """
        Setter dengan validasi: Menolak input yang tidak valid.
        """
        valid_statuses = ["ringan", "sedang", "berat"]
        if value.lower() not in valid_statuses:
            raise ValueError(f"Status mental harus: {', '.join(valid_statuses)}")
        self.__mental_status = value

    def get_mental_status(self) -> str:
        return self.__mental_status

    def get_role_info(self) -> str:
        """Implementasi abstrak untuk mendapatkan info peran."""
        return f"[SURVIVOR] {self.name} | Trauma: {self.__trauma_type} | Status: {self.__mental_status}"
    
    def to_dict(self):
        """Mengubah objek menjadi dictionary agar bisa disimpan ke JSON."""
        return {
            "id": self.id,  # Menggunakan property getter
            "name": self.name,
            "trauma_type": self._Survivor__trauma_type, # Akses atribut private
            "mental_status": self._Survivor__mental_status,
            "created_at": self.created_at_str
        }
    
    @classmethod
    def from_dict(cls, data):
        """Mengubah dictionary dari JSON kembali menjadi Objek Survivor."""
        return cls(
            user_id=data["id"],
            name=data["name"],
            trauma_type=data["trauma_type"],
            mental_status=data["mental_status"]
        )