"""
Contoh penggunaan Program Pendamping Tahfidz Al-Quran
File ini menunjukkan bagaimana menggunakan library secara programatik
"""

from tahfidz_quran import SurahDatabase, ProgressTracker, TahfidzApp, TahfidzQuiz

def contoh_penggunaan_library():
    """Menunjukkan penggunaan library tanpa UI interaktif"""
    
    print("\n" + "="*60)
    print("CONTOH PENGGUNAAN LIBRARY TAHFIDZ")
    print("="*60)
    
    # 1. Mengakses Database Surah
    print("\n1. 📚 MENGAKSES DATABASE SURAH")
    print("-" * 60)
    
    surahs = SurahDatabase.get_all_surahs()
    print(f"Total surah dalam Al-Quran: {len(surahs)}")
    
    # Tampilkan beberapa surah pertama
    print("\nSurah pertama:")
    for surah in surahs[:3]:
        print(f"  • Surah {surah['no']}: {surah['nama']} ({surah['ayat']} ayat)")
    
    # Ambil informasi surah tertentu
    surah_al_fatihah = SurahDatabase.get_surah_by_no(1)
    print(f"\nDetail Surah: {surah_al_fatihah['nama']}")
    print(f"  - Nomor: {surah_al_fatihah['no']}")
    print(f"  - Ayat: {surah_al_fatihah['ayat']}")
    
    # 2. Menggunakan Progress Tracker
    print("\n\n2. 📊 MENGGUNAKAN PROGRESS TRACKER")
    print("-" * 60)
    
    tracker = ProgressTracker("contoh_progress.json")
    
    # Tambah beberapa surah
    print("Menambahkan surah untuk dihafal...")
    tracker.add_surah_progress(1, "sedang_hafal")  # Al-Fatihah
    tracker.add_surah_progress(2, "sedang_hafal")  # Al-Baqarah
    tracker.add_surah_progress(3, "sedang_hafal")  # Ali Imran
    
    print("✓ 3 surah sudah ditambahkan\n")
    
    # Tandai satu surah sebagai hafal
    print("Menandai Al-Fatihah sebagai hafal...")
    tracker.complete_surah(1)
    print("✓ Al-Fatihah ditandai sebagai hafal\n")
    
    # Lihat progress
    completed = tracker.get_completed_surahs()
    in_progress = tracker.get_in_progress_surahs()
    
    print(f"Surah yang sudah hafal: {len(completed)}")
    for no in completed:
        surah = SurahDatabase.get_surah_by_no(no)
        print(f"  ✓ {surah['nama']}")
    
    print(f"\nSurah yang sedang dihafal: {len(in_progress)}")
    for no in in_progress:
        surah = SurahDatabase.get_surah_by_no(no)
        print(f"  ⏳ {surah['nama']}")
    
    # 3. Review tracking
    print("\n\n3. 🔄 REVIEW TRACKING")
    print("-" * 60)
    
    print("Menambahkan review untuk Al-Fatihah...")
    tracker.add_review(1)
    tracker.add_review(1)
    
    progress_data = tracker.get_progress()
    review_count = progress_data["surahs"]["1"]["review_count"]
    
    print(f"✓ Al-Fatihah sudah direview {review_count} kali\n")
    
    # 4. Statistik
    print("\n4. 📈 STATISTIK")
    print("-" * 60)
    
    stats = progress_data["stats"]
    print(f"Total hafalan selesai: {stats['total_hafalan']}")
    print(f"Total review dilakukan: {stats['total_review']}")
    
    # Hitung persentase
    total_surah = len(surahs)
    persen = (len(completed) / total_surah) * 100
    print(f"Progress keseluruhan: {len(completed)}/{total_surah} ({persen:.1f}%)")
    
    print("\n" + "="*60)
    print("📝 Catatan: File 'contoh_progress.json' telah dibuat")
    print("="*60 + "\n")


def contoh_implementasi_custom():
    """Contoh implementasi custom dengan tracker"""
    
    print("\n" + "="*60)
    print("CONTOH IMPLEMENTASI CUSTOM")
    print("="*60)
    
    tracker = ProgressTracker("custom_progress.json")
    
    # Skenario: Membuat program untuk tracking hafalan harian
    print("\n📅 Skenario: Tracking Hafalan Harian")
    print("-" * 60)
    
    # Data hafalan hari ini
    hafalan_hari_ini = [
        (1, "review"),    # Review Al-Fatihah
        (2, "baru"),      # Mulai hafal Al-Baqarah
    ]
    
    for surah_no, tipe in hafalan_hari_ini:
        surah = SurahDatabase.get_surah_by_no(surah_no)
        
        if tipe == "baru":
            tracker.add_surah_progress(surah_no, "sedang_hafal")
            print(f"✓ Mulai hafal: {surah['nama']}")
        elif tipe == "review":
            tracker.add_review(surah_no)
            print(f"✓ Review: {surah['nama']}")
    
    print("\n" + "="*60 + "\n")


def tampilkan_informasi_surah():
    """Menampilkan informasi lengkap surah"""
    
    print("\n" + "="*60)
    print("INFORMASI LENGKAP SURAH")
    print("="*60 + "\n")
    
    # Tampilkan surah berdasarkan kategori panjang
    surahs = SurahDatabase.get_all_surahs()
    
    # Kategori: Surah Pendek (< 50 ayat)
    pendek = [s for s in surahs if s['ayat'] < 50]
    print(f"📖 Surah Pendek (< 50 ayat): {len(pendek)} surah")
    print("Cocok untuk pemula!")
    for s in pendek[:5]:
        print(f"  • {s['nama']}: {s['ayat']} ayat")
    print()
    
    # Kategori: Surah Sedang (50-150 ayat)
    sedang = [s for s in surahs if 50 <= s['ayat'] < 150]
    print(f"📖 Surah Sedang (50-150 ayat): {len(sedang)} surah")
    for s in sedang[:5]:
        print(f"  • {s['nama']}: {s['ayat']} ayat")
    print()
    
    # Kategori: Surah Panjang (>= 150 ayat)
    panjang = [s for s in surahs if s['ayat'] >= 150]
    print(f"📖 Surah Panjang (>= 150 ayat): {len(panjang)} surah")
    print("Untuk hafiz yang sudah berpengalaman")
    for s in panjang:
        print(f"  • {s['nama']}: {s['ayat']} ayat")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║           CONTOH PENGGUNAAN TAHFIDZ PROGRAM            ║
╚══════════════════════════════════════════════════════════╝
""")
    
    # Jalankan contoh-contoh
    contoh_penggunaan_library()
    contoh_implementasi_custom()
    tampilkan_informasi_surah()
    
    print("\n✓ Semua contoh telah dijalankan!")
    print("Untuk menjalankan program interaktif, gunakan: python tahfidz_quran.py\n")
