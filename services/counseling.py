from datetime import datetime
from typing import List
from repositories.survivor_repo import ISurvivorRepository
from models.users import Survivor
from utils.logger import setup_logger

logger = setup_logger()

class CounselingService:
    """
    [PARENT CLASS]
    logika dasar manajemen data (CRUD)
    """
    def __init__(self, repository: ISurvivorRepository):
        # Sesuai UML: Aggregation (Dependency Injection)
        self.repo = repository

    def register_survivor(self, uid: int, name: str, trauma: str, mental: str) -> bool:
        """
        Mendaftarkan survivor baru dan mencatat waktu transaksi.
        """
        """Validasi Input Sederhana"""
        if not name or not trauma:
            """Logging Warning untuk Input Tidak Lengkap"""
            logger.warning(f"Gagal daftar: Data input tidak lengkap untuk ID {uid}")
            raise ValueError("Nama dan Jenis Trauma tidak boleh kosong.")
            
        """Buat Objek Survivor Baru"""
        survivor = Survivor(uid, name, trauma, mental)
        
        """Simpan ke Repository"""
        self.repo.save(survivor)
        
        """Dapatkan Waktu Transaksi dengan datetime"""
        txn_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        """Logging Informasi Transaksi Sukses"""
        logger.info(f"[{txn_time}] TRANSAKSI SUKSES: Survivor {name} (ID: {uid}) berhasil didaftarkan.")
        return True

    def get_all_survivors(self) -> List[Survivor]:
        logger.info("Aktivitas: Mengambil seluruh data survivor.")
        return self.repo.get_all()

class TraumaService(CounselingService):
    """
    [CHILD CLASS]
    Mewarisi CounselingService dan memiliki fitur spesifik asesmen.
    """
    def calculate_impact_score(self, uid: int) -> int:
        """
        Fitur spesifik: Menghitung skor dampak trauma.
        """
        """Ambil Data Survivor dari Repository"""
        survivor = self.repo.find_by_id(uid)
        
        if not survivor:
            """Logging Error jika Survivor Tidak Ditemukan"""
            logger.error(f"Error Asesmen: Survivor ID {uid} tidak ditemukan.")
            raise KeyError("Survivor tidak ditemukan.")
            
        """Logika Perhitungan Skor Sederhana Berdasarkan Status Mental"""
        status = survivor.get_mental_status().lower()
        
        score = 30 # Default untuk 'Ringan'
        if "berat" in status:
            score = 90
        elif "sedang" in status:
            score = 60
            
        logger.info(f"Asesmen Selesai: ID {uid} mendapatkan skor {score}")
        return score