import sys
from repositories.json_repo import JsonSurvivorRepository
from services.counseling import TraumaService
from utils.logger import setup_logger
from utils.notifications import EmailNotificationService

"""Setup logger aplikasi."""
logger = setup_logger()

def main():
    """Fungsi utama menjalankan aplikasi CLI Trauma Healing."""
    repo_storage = JsonSurvivorRepository("data_korban.json")
    
    """Inisialisasi Service dengan Dependency Injection."""
    app_service = TraumaService(repo_storage)
    
    """Setup Notifikasi."""
    notifier = EmailNotificationService()

    print("=== SISTEM LAYANAN DUKUNGAN PSIKOSOSIAL (TRAUMA HEALING) ===")

    while True:
        print("\nMenu Utama:")
        print("1. Daftar Korban")
        print("2. Lihat Data")
        print("3. Cek Skor Dampak (Fitur Khusus)")
        print("4. Keluar")
        
        try:
            choice = input("Pilih menu: ")
            
            if choice == '1':
                """Handle Input Pendaftaran Korban Baru"""
                try:
                    uid = int(input("Masukkan ID (Angka): "))
                except ValueError:
                    print("Error: ID harus berupa angka.")
                    continue
                    
                nama = input("Nama Lengkap: ")
                trauma = input("Jenis Trauma: ")
                mental = input("Status Mental (Ringan/Sedang/Berat): ")
                
                """Register Survivor"""
                app_service.register_survivor(uid, nama, trauma, mental)
                
                """Kirim Notifikasi Registrasi Berhasil"""
                notifier.send_notification(app_service.repo.find_by_id(uid), "Registrasi Berhasil")
                print(">> Sukses: Data berhasil disimpan.")

            elif choice == '2':
                """Lihat Data Korban"""
                data = app_service.get_all_survivors()
                print("\n--- Data Korban ---")
                if not data:
                    print("Belum ada data.")
                for s in data:
                    print(s.get_role_info())

            elif choice == '3':
                """Cek Skor Dampak Trauma"""
                try:
                    search_id = int(input("Masukkan ID Korban: "))
                    score = app_service.calculate_impact_score(search_id)
                    print(f">> Skor Dampak Trauma: {score}/100")
                except ValueError:
                    print("Error: ID harus angka.")

            elif choice == '4':
                print("Keluar dari sistem...")
                sys.exit()
            
            else:
                print("Pilihan tidak valid.")

        except ValueError as e:
            """Menangkap Error Validasi Input"""
            logger.error(f"Input Error: {e}")
            print(f"Error: {e}")
        except KeyError as e:
            """Menangkap Error Data Tidak Ditemukan"""
            logger.error(f"Logic Error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            """Menangkap Error Tak Terduga (Crash Prevention)"""
            logger.critical(f"Critical Error: {e}")
            print("Terjadi kesalahan sistem.")

if __name__ == "__main__":
    main()