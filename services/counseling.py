from typing import List
from repositories.survivor_repo import ISurvivorRepository
from models.users import Survivor
from utils.logger import setup_logger

logger = setup_logger()

class TraumaService:
    def __init__(self, repository: ISurvivorRepository):
        self.repo = repository

    def register_survivor(self, uid: int, name: str, trauma: str, mental: str) -> bool:
        if not name or not trauma:
            logger.warning(f"Gagal daftar: Data tidak lengkap untuk ID {uid}")
            raise ValueError("Nama dan Jenis Trauma tidak boleh kosong.")
            
        survivor = Survivor(uid, name, trauma, mental)
        self.repo.save(survivor)
        logger.info(f"Survivor terdaftar: {name} (ID: {uid})")
        return True

    def get_all_survivors(self) -> List[Survivor]:
        logger.info("Mengambil semua data survivor.")
        return self.repo.get_all()

    def calculate_impact_score(self, uid: int) -> int:
        survivor = self.repo.find_by_id(uid)
        if not survivor:
            logger.error(f"Survivor ID {uid} tidak ditemukan saat asesmen.")
            raise KeyError("Survivor tidak ditemukan.")
            
        status = survivor.get_mental_status().lower()
        if "berat" in status:
            return 90
        elif "sedang" in status:
            return 60
        return 30