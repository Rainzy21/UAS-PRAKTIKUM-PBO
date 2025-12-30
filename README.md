```markdown
# Sistem Layanan Dukungan Psikososial (Trauma Healing CLI)

Aplikasi berbasis **Command Line Interface (CLI)** ini dirancang untuk mengelola data korban bencana alam serta melakukan asesmen awal kesehatan mental (*Trauma Healing*). Proyek ini dibangun sebagai Tugas Besar Pemrograman Berorientasi Objek (PBO) dengan menerapkan standar **Layered Architecture**, **SOLID Principles**, **Unit Testing**, dan **Data Persistence (JSON)**.

---

## Latar Belakang
Dalam situasi pasca-bencana, pendataan korban dan identifikasi tingkat trauma seringkali tidak terorganisir dengan baik. Sistem ini dikembangkan untuk memberikan solusi teknis berupa:
* **Dokumentasi Terstruktur:** Menyimpan informasi korban secara rapi, sistematis, dan mudah diakses.
* **Asesmen Otomatis:** Melakukan kalkulasi skor (*scoring*) tingkat trauma korban (Ringan/Sedang/Berat) berdasarkan parameter mental yang terukur.
* **Transparansi Sistem:** Menyediakan rekam jejak (*logging*) aktivitas sistem yang akurat dan berbasis waktu (*real-time*).

---

## Struktur Proyek
Sistem ini menggunakan **Layered Architecture** untuk memisahkan tanggung jawab (*concern*) antara data, logika bisnis, dan antarmuka.

```text
UAS_Trauma_Healing/
│
├── models/             # [Entity Layer] Representasi Objek Nyata
│   ├── __init__.py
│   └── users.py        # Abstract Class (User) & Serialisasi JSON
│
├── repositories/       # [Data Layer] Manipulasi Penyimpanan Data
│   ├── __init__.py
│   ├── survivor_repo.py # Interface (ISurvivorRepository) - Kontrak DIP
│   └── json_repo.py     # Implementasi Penyimpanan File JSON
│
├── services/           # [Logic Layer] Aturan Bisnis & Algoritma
│   ├── __init__.py
│   └── counseling.py   # Parent (CounselingService) & Child (TraumaService)
│
├── utils/              # [Utility Layer] Fungsi Bantuan
│   ├── __init__.py
│   ├── logger.py       # Konfigurasi Logging dengan Timestamp
│   └── notifications.py# Abstraksi Sistem Notifikasi (OCP)
│
├── tests/              # [Testing Layer] Pengujian Reliabilitas
│   ├── __init__.py
│   └── test_service.py # Unit Test (CRUD, Logic, Validation)
│
├── main.py             # [Presentation Layer] Orchestrator / Entry Point
├── data_korban.json    # [Database] File penyimpanan data permanen
├── uml.png             # [Docs] Diagram Arsitektur
└── README.md           # Dokumentasi Proyek

```

---

## Implementasi Teknis (OOP & SOLID)

Sistem ini dinilai berdasarkan penerapan konsep-konsep berikut:

### 1. Object-Oriented Programming (OOP)

* **Encapsulation:** Seluruh atribut vital (seperti `__id`, `__mental_status`) bersifat **Private** dan hanya bisa diakses melalui Getter/Setter tervalidasi.
* **Inheritance:** `TraumaService` (Child) mewarisi `CounselingService` (Parent); `Survivor` mewarisi `User`.
* **Polymorphism:** Method `get_role_info()` dan `to_dict()` memiliki implementasi berbeda pada setiap entitas turunan.
* **Abstraction:** Menggunakan `ABC` (*Abstract Base Class*) pada `User` dan Interface pada Repository.

### 2. SOLID Principles

* **SRP (Single Responsibility):** Pemisahan tegas: `json_repo.py` hanya mengurus file, `counseling.py` hanya mengurus logika skor.
* **OCP (Open/Closed):** Modul notifikasi dan repository dirancang agar mudah diperluas tanpa memodifikasi kode inti.
* **DIP (Dependency Inversion):** `TraumaService` tidak bergantung pada class konkret repository, melainkan pada kontrak interface `ISurvivorRepository`.

---

## Fitur Utama

1. **Penyimpanan Permanen (JSON Storage):** Data korban disimpan dalam file `data_korban.json` secara otomatis. Data tidak hilang meskipun aplikasi ditutup.
2. **Manajemen Korban (CRUD):** Pencatatan data dengan validasi input yang ketat (cegah data kosong/invalid).
3. **Trauma Scoring System:** Algoritma otomatis menghitung skor dampak (30-90) berdasarkan status mental (Ringan/Sedang/Berat).
4. **Real-time Logging:** Setiap transaksi (sukses/gagal) direkam ke `logs/app.log` dengan Timestamp presisi.
5. **Robust Error Handling:** Sistem tahan banting terhadap input salah atau file korup tanpa menyebabkan *crash*.

---

## Desain UML

![UML Class Diagram](./uml.png)

Struktur kode dibangun berdasarkan rancangan UML Class Diagram berikut:

> **Keterangan Diagram:**
> * **Service Layer:** `TraumaService` (Child) mewarisi `CounselingService` (Parent) untuk memperluas kapabilitas asesmen.
> * **Data Layer:** `ISurvivorRepository` bertindak sebagai kontrak (Interface). Pada implementasi final, digunakan `JsonSurvivorRepository` (menggantikan `InMemory` pada diagram) untuk persistensi data.
> * **Model:** `Survivor` dan `Counselor` adalah turunan dari Abstract Class `User`.
> * **Utility:** `NotificationService` menerapkan pola Observer/Interface untuk fleksibilitas notifikasi.

---

**Identitas Pengembang:**

* **Nama:** [Isi Nama Anda]
* **NIM:** [Isi NIM Anda]
* **Kelas:** [Isi Kelas Anda]

```

```