import json
import os
from typing import List
from models.users import Survivor
from repositories.survivor_repo import ISurvivorRepository

class JsonSurvivorRepository(ISurvivorRepository):
    def __init__(self, filename="data.json"):
        self.filename = filename
        self._storage: List[Survivor] = self._load_data()

    def _load_data(self) -> List[Survivor]:
        """Membaca file JSON dan mengubahnya jadi Objek Survivor."""
        if not os.path.exists(self.filename):
            return []
        
        with open(self.filename, 'r') as f:
            try:
                data_list = json.load(f)
                # Konversi Dict -> Object
                return [Survivor.from_dict(item) for item in data_list]
            except json.JSONDecodeError:
                return []

    def _save_file(self):
        """Menulis ulang seluruh list objek ke file JSON."""
        # Konversi Object -> Dict
        data_list = [s.to_dict() for s in self._storage]
        with open(self.filename, 'w') as f:
            json.dump(data_list, f, indent=4)

    def save(self, survivor: Survivor):
        self._storage.append(survivor)
        self._save_file() # Auto-save setiap ada data baru

    def find_by_id(self, user_id: int):
        for s in self._storage:
            if s.id == user_id:
                return s
        return None

    def get_all(self):
        return self._storage