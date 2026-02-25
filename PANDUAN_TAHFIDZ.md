# 📖 Pendamping Tahfidz Al-Quran

Program bantu untuk memudahkan seorang tahfidz/hafidzah dalam menghafalkan surat-surat Al-Quran dengan tracking progress dan fitur-fitur menarik.

## ✨ Fitur Utama

### 1. **Daftar Surat Al-Quran** 📚
   - Melihat daftar lengkap 30 surat dengan jumlah ayat
   - Status setiap surat (Belum Dimulai, Sedang Hafal, atau Sudah Hafal)
   - Tracking otomatis progress hafalan

### 2. **Manajemen Hafalan** ➕
   - Tambah surat untuk dihafal
   - Tandai surat yang sudah hafal
   - Lacak tanggal mulai dan selesai hafalan

### 3. **Sistem Kuis** 🧠
   - Kuis interaktif untuk menguji pemahaman
   - Pertanyaan tentang jumlah ayat dan nomor surat
   - Sistem penilaian otomatis

### 4. **Test Acak** 🎯
   - Random surah testing untuk surat yang sudah hafal
   - Membantu mempertahankan hafalan yang sudah dicapai
   - Tracking jumlah review per surat

### 5. **Statistik & Motivasi** 📈
   - Melihat progress keseluruhan hafalan
   - Persentase penyelesaian
   - Pesan motivasi berbeda sesuai progress
   - Riwayat review per surat

### 6. **Penyimpanan Progress** 💾
   - Otomatis menyimpan progress ke file JSON
   - Data tersimpan permanen
   - Bisa dilanjutkan kapan saja

## 🚀 Cara Menggunakan

### Instalasi
Program ini menggunakan Python 3 standar tanpa library tambahan yang kompleks.

```bash
python tahfidz_quran.py
```

### Menu-Menu Utama

#### 1️⃣ Lihat Daftar Surah
```
Pilih: 1
```
Menampilkan semua 30 surah dengan status hafalan Anda:
- ✓ Sudah Hafal
- ⏳ Sedang Hafal
- ⭕ Belum Dimulai

#### 2️⃣ Tambah Surah untuk Dihafal
```
Pilih: 2
Masukan nomor surah (1-30): [nomor surah]
```
Contoh: Untuk memulai hafal Al-Fatihah, masukan `1`

#### 3️⃣ Tandai Surah Sebagai Hafal
```
Pilih: 3
```
Program akan menampilkan surah yang sedang dihafal, pilih salah satu yang sudah selesai.

#### 4️⃣ Lihat Progress Hafalan
```
Pilih: 4
```
Melihat:
- Total surah yang sudah hafal
- Daftar surah dengan tanggal selesai
- Jumlah review untuk setiap surah
- Surah yang sedang dihafal

#### 5️⃣ Kuis Hafalan
```
Pilih: 5
```
- Pilih surah yang sedang dihafal
- Jawab 2 pertanyaan tentang surah tersebut
- Dapatkan skor dan umpan balik
- Skor: 100 = Lulus sempurna, <100 = Perlu belajar lebih giat

#### 6️⃣ Test Surah Acak
```
Pilih: 6
```
- Program secara acak memilih surat dari yang sudah hafal
- Anda mengulang/meucapkan hafalan surah tersebut
- Review count otomatis bertambah
- Membantu mempertahankan hafalan

#### 7️⃣ Statistik Kepribadian
```
Pilih: 7
```
Menampilkan:
- Total surah yang sudah hafal (dari 30)
- Persentase penyelesaian
- Total ulangan/review
- Pesan motivasi yang disesuaikan
- Tips untuk meningkatkan hafalan

#### 8️⃣ Keluar
```
Pilih: 8
```
Keluar dari program (progress otomatis disimpan)

## 📊 Struktur Data

Program menyimpan data progress dalam file `progress_tahfidz.json`:

```json
{
    "surahs": {
        "1": {
            "surah_no": 1,
            "status": "hafal",
            "date_started": "2026-02-25",
            "date_completed": "2026-02-26",
            "review_count": 5,
            "last_review": "2026-02-28"
        }
    },
    "stats": {
        "total_hafalan": 1,
        "total_review": 5
    }
}
```

## 💡 Tips dan Trik

### Untuk Hasil Maksimal:

1. **Konsistensi** ⏰
   - Tentukan jadwal hafalan yang teratur
   - Lebih baik hafal sedikit tapi konsisten daripada banyak tapi tidak teratur

2. **Review Berkala** 🔄
   - Gunakan fitur "Test Surah Acak" untuk mempertahankan hafalan
   - Target minimal 3-5 kali review per surat sebelum menghafalkan surah baru

3. **Jangan Terburu-buru** 🐢
   - Kualitas hafalan lebih penting daripada kecepatan
   - Pastikan satu surah benar-benar hafal sebelum ke surah berikutnya

4. **Gunakan Fitur Kuis** 🧠
   - Kuis membantu mengecek pemahaman akan surah
   - Lakukan kuis sebelum menandai surah sebagai "hafal"

5. **Motivasi Diri** 💪
   - Lihat statistik untuk melihat progress Anda
   - Renungkan tujuan hafalan Al-Quran
   - Berbagi progress dengan teman/keluarga

## 📚 Surat-Surat dalam Program

Program mencakup surat 1-30 dari Al-Quran:

| No | Nama Surat | Ayat |
|----|-----------|------|
| 1 | Al-Fatihah | 7 |
| 2 | Al-Baqarah | 286 |
| ... | ... | ... |
| 30 | Ar-Rum | 60 |

## 🔧 Troubleshooting

### Progress tidak tersimpan?
- Pastikan program ditutup dengan benar (pilih menu 8)
- Cek apakah file `progress_tahfidz.json` ada di folder yang sama

### Ingin reset progress?
- Hapus file `progress_tahfidz.json`
- Program akan membuat file baru saat dijalankan

### Ingin menambah surah lebih dari 30?
- Edit bagian `SURAHS` dalam class `SurahDatabase`
- Ikuti format yang sama untuk surah-surah berikutnya

## 📖 Doa Sebelum Hafalan

> "Allahumma infa'ni bima 'allamtani wa 'allimni ma yanfa'uni wa zidni 'ilman"
> "Ya Allah, manfaatkan aku dengan ilmu yang Engkau ajarkan, ajarkan aku ilmu yang bermanfaat, dan tambahkan ilmuku"

---

**Semoga Allah memudahkan hafalan Anda dan menjadikan hati ini tempat Al-Quran yang mulia! 🤲📖**

Wassalamu alaikum wa rahmatullahi wa barakatuh ☪️
