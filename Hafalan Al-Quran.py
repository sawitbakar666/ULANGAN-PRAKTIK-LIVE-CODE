"""
Program Pendamping Tahfidz Al-Quran
Membantu hafiz/hafidzah menghafalkan dan melacak progress memorisasi surat-surat Al-Quran
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Tuple

class SurahDatabase:
    """Database untuk menyimpan informasi surah"""
    
    SURAHS = [
        {"no": 1, "nama": "Al-Fatihah", "ayat": 7},
        {"no": 2, "nama": "Al-Baqarah", "ayat": 286},
        {"no": 3, "nama": "Ali 'Imran", "ayat": 200},
        {"no": 4, "nama": "An-Nisa'", "ayat": 176},
        {"no": 5, "nama": "Al-Ma'idah", "ayat": 120},
        {"no": 6, "nama": "Al-An'am", "ayat": 165},
        {"no": 7, "nama": "Al-A'raf", "ayat": 206},
        {"no": 8, "nama": "Al-Anfal", "ayat": 75},
        {"no": 9, "nama": "At-Taubah", "ayat": 129},
        {"no": 10, "nama": "Yunus", "ayat": 109},
        {"no": 11, "nama": "Hud", "ayat": 123},
        {"no": 12, "nama": "Yusuf", "ayat": 111},
        {"no": 13, "nama": "Ar-Ra'd", "ayat": 43},
        {"no": 14, "nama": "Ibrahim", "ayat": 52},
        {"no": 15, "nama": "Al-Hijr", "ayat": 99},
        {"no": 16, "nama": "An-Nahl", "ayat": 128},
        {"no": 17, "nama": "Al-Isra'", "ayat": 111},
        {"no": 18, "nama": "Al-Kahf", "ayat": 110},
        {"no": 19, "nama": "Maryam", "ayat": 98},
        {"no": 20, "nama": "Ta-Ha", "ayat": 135},
        {"no": 21, "nama": "Al-Anbiya'", "ayat": 112},
        {"no": 22, "nama": "Al-Hajj", "ayat": 78},
        {"no": 23, "nama": "Al-Mu'minun", "ayat": 118},
        {"no": 24, "nama": "An-Nur", "ayat": 64},
        {"no": 25, "nama": "Al-Furqan", "ayat": 77},
        {"no": 26, "nama": "Asy-Syu'ara'", "ayat": 227},
        {"no": 27, "nama": "An-Naml", "ayat": 93},
        {"no": 28, "nama": "Al-Qassas", "ayat": 88},
        {"no": 29, "nama": "Al-'Ankabut", "ayat": 69},
        {"no": 30, "nama": "Ar-Rum", "ayat": 60},
        {"no": 31, "nama": "Luqman", "ayat": 34},
        {"no": 32, "nama": "As-Sajdah", "ayat": 30},
        {"no": 33, "nama": "Al-Ahzab", "ayat": 73},
        {"no": 34, "nama": "Saba'", "ayat": 54},
        {"no": 35, "nama": "Fatir", "ayat": 45},
        {"no": 36, "nama": "Ya-Sin", "ayat": 83},
        {"no": 37, "nama": "As-Saffat", "ayat": 182},
        {"no": 38, "nama": "Sad", "ayat": 88},
        {"no": 39, "nama": "Az-Zumar", "ayat": 75},
        {"no": 40, "nama": "Al-Mu'min", "ayat": 85},
        {"no": 41, "nama": "Fussilat", "ayat": 54},
        {"no": 42, "nama": "Asy-Syura", "ayat": 53},
        {"no": 43, "nama": "Az-Zukhruf", "ayat": 89},
        {"no": 44, "nama": "Ad-Dukhan", "ayat": 59},
        {"no": 45, "nama": "Al-Jathiyah", "ayat": 37},
        {"no": 46, "nama": "Al-Ahqaf", "ayat": 35},
        {"no": 47, "nama": "Muhammad", "ayat": 38},
        {"no": 48, "nama": "Al-Fath", "ayat": 29},
        {"no": 49, "nama": "Al-Hujurat", "ayat": 18},
        {"no": 50, "nama": "Qaf", "ayat": 45},
        {"no": 51, "nama": "Ad-Dhariyat", "ayat": 60},
        {"no": 52, "nama": "At-Tur", "ayat": 49},
        {"no": 53, "nama": "An-Najm", "ayat": 62},
        {"no": 54, "nama": "Al-Qamar", "ayat": 55},
        {"no": 55, "nama": "Ar-Rahman", "ayat": 78},
        {"no": 56, "nama": "Al-Waqi'ah", "ayat": 96},
        {"no": 57, "nama": "Al-Hadid", "ayat": 29},
        {"no": 58, "nama": "Al-Mujadilah", "ayat": 22},
        {"no": 59, "nama": "Al-Hashr", "ayat": 24},
        {"no": 60, "nama": "Al-Mumtahanah", "ayat": 13},
        {"no": 61, "nama": "As-Saff", "ayat": 14},
        {"no": 62, "nama": "Al-Jumu'ah", "ayat": 11},
        {"no": 63, "nama": "Al-Munafiqun", "ayat": 11},
        {"no": 64, "nama": "At-Taghabun", "ayat": 18},
        {"no": 65, "nama": "At-Talaq", "ayat": 12},
        {"no": 66, "nama": "At-Tahrim", "ayat": 12},
        {"no": 67, "nama": "Al-Mulk", "ayat": 30},
        {"no": 68, "nama": "Al-Qalam", "ayat": 52},
        {"no": 69, "nama": "Al-Haqqah", "ayat": 52},
        {"no": 70, "nama": "Al-Ma'arij", "ayat": 44},
        {"no": 71, "nama": "Nuh", "ayat": 28},
        {"no": 72, "nama": "Al-Jinn", "ayat": 28},
        {"no": 73, "nama": "Al-Muzzammil", "ayat": 20},
        {"no": 74, "nama": "Al-Muddassir", "ayat": 56},
        {"no": 75, "nama": "Al-Qiyamah", "ayat": 40},
        {"no": 76, "nama": "Al-Insan", "ayat": 31},
        {"no": 77, "nama": "Al-Mursalat", "ayat": 50},
        {"no": 78, "nama": "An-Naba'", "ayat": 40},
        {"no": 79, "nama": "An-Nazi'at", "ayat": 46},
        {"no": 80, "nama": "'Abasa", "ayat": 42},
        {"no": 81, "nama": "At-Takwir", "ayat": 29},
        {"no": 82, "nama": "Al-Infitar", "ayat": 19},
        {"no": 83, "nama": "Al-Mutaffifin", "ayat": 36},
        {"no": 84, "nama": "Al-Inshiqaq", "ayat": 25},
        {"no": 85, "nama": "Al-Buruj", "ayat": 22},
        {"no": 86, "nama": "At-Tariq", "ayat": 17},
        {"no": 87, "nama": "Al-A'la", "ayat": 19},
        {"no": 88, "nama": "Al-Ghashiyah", "ayat": 26},
        {"no": 89, "nama": "Al-Fajr", "ayat": 30},
        {"no": 90, "nama": "Al-Balad", "ayat": 20},
        {"no": 91, "nama": "Asy-Syams", "ayat": 15},
        {"no": 92, "nama": "Al-Lail", "ayat": 21},
        {"no": 93, "nama": "Ad-Duha", "ayat": 11},
        {"no": 94, "nama": "Asy-Syarh", "ayat": 8},
        {"no": 95, "nama": "At-Tin", "ayat": 8},
        {"no": 96, "nama": "Al-'Alaq", "ayat": 19},
        {"no": 97, "nama": "Al-Qadr", "ayat": 5},
        {"no": 98, "nama": "Al-Bayyinah", "ayat": 8},
        {"no": 99, "nama": "Az-Zilzal", "ayat": 8},
        {"no": 100, "nama": "Al-'Adiyat", "ayat": 11},
        {"no": 101, "nama": "Al-Qari'ah", "ayat": 11},
        {"no": 102, "nama": "At-Takatsur", "ayat": 8},
        {"no": 103, "nama": "Al-'Asr", "ayat": 3},
        {"no": 104, "nama": "Al-Humazah", "ayat": 9},
        {"no": 105, "nama": "Al-Fil", "ayat": 5},
        {"no": 106, "nama": "Quraisy", "ayat": 4},
        {"no": 107, "nama": "Al-Ma'un", "ayat": 7},
        {"no": 108, "nama": "Al-Kautsar", "ayat": 3},
        {"no": 109, "nama": "Al-Kafirun", "ayat": 6},
        {"no": 110, "nama": "An-Nasr", "ayat": 3},
        {"no": 111, "nama": "Al-Lahab", "ayat": 5},
        {"no": 112, "nama": "Al-Ikhlas", "ayat": 4},
        {"no": 113, "nama": "Al-Falaq", "ayat": 5},
        {"no": 114, "nama": "An-Nas", "ayat": 6},
    ]
    
    @staticmethod
    def get_all_surahs() -> List[Dict]:
        """Mendapatkan daftar semua surah"""
        return SurahDatabase.SURAHS
    
    @staticmethod
    def get_surah_by_no(no: int) -> Dict:
        """Mendapatkan informasi surah berdasarkan nomor"""
        for surah in SurahDatabase.SURAHS:
            if surah["no"] == no:
                return surah
        return None


class ProgressTracker:
    """Melacak progress hafalan pengguna"""
    
    def __init__(self, filename: str = "progress_tahfidz.json"):
        self.filename = filename
        self.data = self.load_progress()
    
    def load_progress(self) -> Dict:
        """Memuat progress dari file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {"surahs": {}, "stats": {"total_hafalan": 0, "total_review": 0}}
        return {"surahs": {}, "stats": {"total_hafalan": 0, "total_review": 0}}
    
    def save_progress(self):
        """Menyimpan progress ke file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
    
    def add_surah_progress(self, surah_no: int, status: str = "sedang_hafal"):
        """Menambahkan progress hafalan surah"""
        surah_key = str(surah_no)
        
        if surah_key not in self.data["surahs"]:
            self.data["surahs"][surah_key] = {
                "surah_no": surah_no,
                "status": status,
                "date_started": datetime.now().strftime("%Y-%m-%d"),
                "date_completed": None,
                "review_count": 0,
                "last_review": None
            }
        
        self.save_progress()
    
    def complete_surah(self, surah_no: int):
        """Menandai surah sebagai hafal"""
        surah_key = str(surah_no)
        
        if surah_key in self.data["surahs"]:
            self.data["surahs"][surah_key]["status"] = "hafal"
            self.data["surahs"][surah_key]["date_completed"] = datetime.now().strftime("%Y-%m-%d")
            self.data["stats"]["total_hafalan"] += 1
            self.save_progress()
    
    def add_review(self, surah_no: int):
        """Menambah jumlah review"""
        surah_key = str(surah_no)
        
        if surah_key in self.data["surahs"]:
            self.data["surahs"][surah_key]["review_count"] += 1
            self.data["surahs"][surah_key]["last_review"] = datetime.now().strftime("%Y-%m-%d")
            self.data["stats"]["total_review"] += 1
            self.save_progress()
    
    def get_progress(self) -> Dict:
        """Mendapatkan semua progress"""
        return self.data
    
    def get_completed_surahs(self) -> List[int]:
        """Mendapatkan daftar surah yang sudah hafal"""
        completed = []
        for surah_key, info in self.data["surahs"].items():
            if info["status"] == "hafal":
                completed.append(info["surah_no"])
        return sorted(completed)
    
    def get_in_progress_surahs(self) -> List[int]:
        """Mendapatkan daftar surah yang sedang dihafal"""
        in_progress = []
        for surah_key, info in self.data["surahs"].items():
            if info["status"] == "sedang_hafal":
                in_progress.append(info["surah_no"])
        return sorted(in_progress)


class TahfidzQuiz:
    """Sistem kuis untuk menguji hafalan"""
    
    def __init__(self, progress_tracker: ProgressTracker):
        self.tracker = progress_tracker
    
    def quiz_surah(self, surah_no: int) -> Tuple[bool, int]:
        """
        Kuis mengenai surah tertentu
        Returns: (berhasil, skor)
        """
        surah = SurahDatabase.get_surah_by_no(surah_no)
        
        if not surah:
            return False, 0
        
        print(f"\n{'='*50}")
        print(f"KUIS SURAH {surah['nama']} (Surah {surah['no']})")
        print(f"{'='*50}\n")
        
        pertanyaan = [
            f"Berapa banyak ayat dalam surah {surah['nama']}?",
            f"Surah {surah['nama']} adalah surah ke berapa?",
            f"Apa nama lain dari surah {surah['nama']} (jika ada)?"
        ]
        
        jawaban_benar = [
            str(surah['ayat']),
            str(surah['no']),
            surah['nama']
        ]
        
        skor = 0
        
        for i, pertanyaan_item in enumerate(pertanyaan[:2]):  # 2 pertanyaan saja
            print(f"Pertanyaan {i+1}: {pertanyaan_item}")
            jawaban_user = input("Jawaban Anda: ").strip()
            
            if jawaban_user.lower() == jawaban_benar[i].lower():
                print("✓ Benar!\n")
                skor += 50
            else:
                print(f"✗ Salah. Jawaban yang benar: {jawaban_benar[i]}\n")
        
        berhasil = skor >= 50
        return berhasil, skor
    
    def random_surah_test(self) -> int:
        """Test hafalan dengan surah acak"""
        completed = self.tracker.get_completed_surahs()
        
        if not completed:
            print("Anda belum menyelesaikan hafalan surah apapun.")
            return 0
        
        import random
        surah_no = random.choice(completed)
        surah = SurahDatabase.get_surah_by_no(surah_no)
        
        print(f"\n🎯 Surah Acak: {surah['nama']} (Surah {surah['no']})")
        print("Silakan mengulang hafalan surah ini!")
        
        input("\nTekan Enter setelah selesai...")
        self.tracker.add_review(surah_no)
        
        return surah_no


class TahfidzApp:
    """Aplikasi utama Pendamping Tahfidz"""
    
    def __init__(self):
        self.tracker = ProgressTracker()
        self.quiz = TahfidzQuiz(self.tracker)
    
    def tampilkan_banner(self):
        """Menampilkan banner aplikasi"""
        print("""
╔══════════════════════════════════════════════════════════╗
║         📖 PENDAMPING TAHFIDZ AL-QURAN 📖                ║
║                                                          ║
║     Alat bantu untuk menghafalkan Surat-surat Al-Quran   ║
║                                                          ║
║              "Allahumma infa'ni bima 'allamtani"         ║
╚══════════════════════════════════════════════════════════╝
""")
    
    def tampilkan_menu_utama(self):
        """Menampilkan menu utama"""
        print("\n" + "="*50)
        print("MENU UTAMA")
        print("="*50)
        print("1. 📚 Lihat Daftar Surah")
        print("2. ➕ Tambah Surah untuk Dihafal")
        print("3. ✅ Tandai Surah Sebagai Hafal")
        print("4. 📊 Lihat Progress Hafalan")
        print("5. 🧠 Kuis Hafalan")
        print("6. 🎯 Test Surah Hafalan Acak")
        print("7. 📈 Presentase Hafalan")
        print("8. ❌ Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-8): ").strip()
        return pilihan
    
    def tampilkan_daftar_surah(self):
        """Menampilkan daftar semua surah"""
        surahs = SurahDatabase.get_all_surahs()
        completed = self.tracker.get_completed_surahs()
        in_progress = self.tracker.get_in_progress_surahs()
        
        print("\n" + "="*70)
        print(f"{'No':<4} {'Nama Surah':<30} {'Ayat':<8} {'Status':<20}")
        print("="*70)
        
        for surah in surahs:
            no = surah['no']
            nama = surah['nama']
            ayat = surah['ayat']
            
            if no in completed:
                status = "✓ Sudah Hafal"
            elif no in in_progress:
                status = "⏳ Sedang Menghafal"
            else:
                status = "⭕ Belum Dimulai"
            
            print(f"{no:<4} {nama:<30} {ayat:<8} {status:<20}")
        
        print("="*70)
    
    def tambah_surah(self):
        """Menambah surah untuk dihafal"""
        print("\n" + "="*50)
        print("TAMBAH SURAH UNTUK DIHAFAL")
        print("="*50)
        
        try:
            surah_no = int(input("Masukan nomor surah (1-114): "))
            
            if surah_no < 1 or surah_no > 114:
                print("❌ Nomor surah harus antara 1-114")
                return
            
            surah = SurahDatabase.get_surah_by_no(surah_no)
            print(f"\n✓ Anda akan mulai hafal {surah['nama']} ({surah['ayat']} ayat)")
            print("Semoga Allah mudahkan hafalan Anda! 💪")
            
            self.tracker.add_surah_progress(surah_no, "sedang_hafal")
            
        except ValueError:
            print("❌ Input tidak valid!")
    
    def tandai_hafal(self):
        """Menandai surah sebagai hafal"""
        print("\n" + "="*50)
        print("TANDAI SURAH SEBAGAI HAFAL")
        print("="*50)
        
        in_progress = self.tracker.get_in_progress_surahs()
        
        if not in_progress:
            print("Tidak ada surah yang sedang dihafal.")
            return
        
        print("Surah yang sedang dihafal:")
        for i, surah_no in enumerate(in_progress, 1):
            surah = SurahDatabase.get_surah_by_no(surah_no)
            print(f"{i}. {surah['nama']} (Surah {surah['no']})")
        
        try:
            surah_no = int(input("\nMasukan nomor surah yang sudah hafal: "))
            
            if surah_no not in in_progress:
                print("❌ Surah tidak ditemukan dalam daftar hafalan!")
                return
            
            surah = SurahDatabase.get_surah_by_no(surah_no)
            print(f"\n🎉 Alhamdulillah! Anda berhasil menghafalkan {surah['nama']}!")
            print("Semoga Allah terima dari Anda dan buat hafalan ini berkah 📖")
            
            self.tracker.complete_surah(surah_no)
            
        except ValueError:
            print("❌ Input tidak valid!")
    
    def lihat_progress(self):
        """Menampilkan progress hafalan"""
        completed = self.tracker.get_completed_surahs()
        in_progress = self.tracker.get_in_progress_surahs()
        progress_data = self.tracker.get_progress()
        
        print("\n" + "="*50)
        print("PROGRESS HAFALAN ANDA")
        print("="*50)
        
        total_hafal = len(completed)
        print(f"\n📚 Total Surah Hafal: {total_hafal}/114")
        
        if completed:
            print("\n✅ Surah yang Sudah Hafal:")
            for surah_no in completed:
                surah = SurahDatabase.get_surah_by_no(surah_no)
                info = progress_data["surahs"][str(surah_no)]
                print(f"   • {surah['nama']} - Selesai: {info['date_completed']} (Review: {info['review_count']}x)")
        
        if in_progress:
            print("\n⏳ Surah yang Sedang Dihafal:")
            for surah_no in in_progress:
                surah = SurahDatabase.get_surah_by_no(surah_no)
                info = progress_data["surahs"][str(surah_no)]
                print(f"   • {surah['nama']} - Dimulai: {info['date_started']}")
        
        print("\n" + "="*50)
    
    def mulai_kuis(self):
        """Memulai sesi kuis"""
        print("\n" + "="*50)
        print("KUIS HAFALAN")
        print("="*50)
        
        in_progress = self.tracker.get_in_progress_surahs()
        
        if not in_progress:
            print("Tidak ada surah yang sedang dihafal.")
            return
        
        print("Surah yang siap dikuis:")
        for i, surah_no in enumerate(in_progress, 1):
            surah = SurahDatabase.get_surah_by_no(surah_no)
            print(f"{i}. {surah['nama']} (Surah {surah['no']})")
        
        try:
            surah_no = int(input("\nPilih nomor surah untuk kuis: "))
            
            if surah_no not in in_progress:
                print("❌ Surah tidak valid!")
                return
            
            berhasil, skor = self.quiz.quiz_surah(surah_no)
            
            print(f"\n📊 Hasil Kuis:")
            print(f"Skor Anda: {skor}/100")
            
            if berhasil:
                print("✓ Anda lulus! Pertahankan semangat hafalan Anda! 🎉")
            else:
                print("Anda perlu lebih giat lagi. Jangan menyerah! 💪")
            
        except ValueError:
            print("❌ Input tidak valid!")
    
    def test_random(self):
        """Test dengan surah acak"""
        self.quiz.random_surah_test()
    
    def tampilkan_statistik(self):
        """Menampilkan statistik"""
        progress_data = self.tracker.get_progress()
        stats = progress_data["stats"]
        completed = self.tracker.get_completed_surahs()
        
        print("\n" + "="*50)
        print("PRESENTASE HAFALAN")
        print("="*50)
        
        total_hafal = len(completed)
        persen = (total_hafal / 114) * 100
        
        print(f"\n📊 Total Hafalan: {total_hafal}/114 Surah ({persen:.1f}%)")
        print(f"📖 Total Review: {stats['total_review']} kali")
        
        if total_hafal > 0:
            print(f"\n🏆 Pencapaian:")
            print(f"   • Anda telah menghafalkan {total_hafal} surah")
            print(f"   • Rata-rata review per surah: {stats['total_review'] // total_hafal if total_hafal > 0 else 0} kali")
        
        print("\n💡 Motivasi:")
        if persen == 0:
            print("   Mulailah hari ini! Ayat Pertama adalah awal kesuksesan 📖")
        elif persen < 30:
            print("   Terus semangat! Anda sudah mulai perjalanan yang mulia 💪")
        elif persen < 60:
            print("   Luar biasa! Anda sudah mencapai setengah jalan! 🌟")
        elif persen < 100:
            print("   Hampir sampai! Waktu untuk menyelesaikan perjuangan Anda 🎯")
        else:
            print("   Alhamdulillah! Anda telah menyelesaikan hafalan seluruh Al-Quran (114 surah)! 🎉🎉🎉")
        
        print("="*50)
    
    def run(self):
        """Menjalankan aplikasi"""
        self.tampilkan_banner()
        
        while True:
            pilihan = self.tampilkan_menu_utama()
            
            if pilihan == "1":
                self.tampilkan_daftar_surah()
            elif pilihan == "2":
                self.tambah_surah()
            elif pilihan == "3":
                self.tandai_hafal()
            elif pilihan == "4":
                self.lihat_progress()
            elif pilihan == "5":
                self.mulai_kuis()
            elif pilihan == "6":
                self.test_random()
            elif pilihan == "7":
                self.tampilkan_statistik()
            elif pilihan == "8":
                print("\n🤝 Terima kasih telah menggunakan Pendamping Tahfidz!")
                print("Semoga Allah menerima hafalan Anda dan membuat hati Anda tenang. 📖")
                print("Wassalamualaikum wa rahmatullahi wa barakatuh 🤲\n")
                break
            else:
                print("❌ Pilihan tidak valid! Silakan pilih menu 1-8.")


def main():
    """Fungsi utama"""
    app = TahfidzApp()
    app.run()


if __name__ == "__main__":
    main()
