import sys
from repositories.survivor_repo import InMemorySurvivorRepository
from services.counseling import TraumaService
from utils.logger import setup_logger
from utils.notifications import EmailNotificationService
logger = setup_logger()

def main():
    repo_storage = InMemorySurvivorRepository()
    app_service = TraumaService(repo_storage)

    print("=== SISTEM LAYANAN DUKUNGAN PSIKOSOSIAL (TRAUMA HEALING) ===")

    while True:
        print("\nMenu Utama:")
        print("1. Daftar Korban")
        print("2. Lihat Data")
        print("3. Cek Skor Dampak")
        print("4. Keluar")
        
        try:
            choice = input("Pilih menu: ")
            
            if choice == '1':
                print("\n--- Form Daftar Korban ---")
                uid = int(input("Masukkan ID (Angka): "))
                nama = input("Nama Lengkap: ")
                trauma = input("Jenis Trauma: ")
                mental = input("Status Mental (Ringan/Sedang/Berat): ")
                
                app_service.register_survivor(uid, nama, trauma, mental)
                print(">> Sukses: Data berhasil disimpan.")

            elif choice == '2':
                data = app_service.get_all_survivors()
                print("\n--- Data Korban ---")
                if not data:
                    print("Belum ada data.")
                for s in data:
                    print(s.get_role_info())

            elif choice == '3':
                search_id = int(input("Masukkan ID Korban: "))
                score = app_service.calculate_impact_score(search_id)
                print(f">> Skor Dampak Trauma: {score}/100")

            elif choice == '4':
                print("Keluar dari sistem...")
                sys.exit()
            
            else:
                print("Pilihan tidak valid.")

        except ValueError as e:
            logger.error(f"Input Error: {e}")
            print(f"Error: Masukan tidak valid! ({e})")
        except KeyError as e:
            logger.error(f"Logic Error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            logger.critical(f"Critical Error: {e}")
            print("Terjadi kesalahan sistem.")

if __name__ == "__main__":
    main()