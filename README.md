# 🎮 Mystery Adventure Game

Selamat datang di **Mystery Adventure Game** - sebuah game petualangan teks interaktif yang menantang kemampuan strategi dan keberuntungan Anda!

## 📋 Daftar Isi

- [Cara Bermain](#cara-bermain)
- [Fitur Game](#fitur-game)
- [Komponen Game](#komponen-game)
- [Sistem Musuh](#sistem-musuh)
- [Sistem Stage](#sistem-stage)
- [Tips dan Trik](#tips-dan-trik)
- [Cara Menjalankan](#cara-menjalankan)

---

## 🎯 Cara Bermain

### Memulai Game
1. Jalankan program dengan `python main.py`
2. Masukkan nama pemain Anda (minimal 3 karakter)
3. Pelajari statistik karakter Anda di awal game

### Mekanisme Utama: Hadapi atau Kabur

Di setiap pertemuan musuh, Anda memiliki pilihan strategis:

```
┌─────────────────────────────────────────┐
│  Apa yang ingin kamu lakukan?           │
│  1⚔️  'hadapi'  → Hadapi musuh langsung │
│  2🏃  'kabur'   → Cari peti untuk upgrade
└─────────────────────────────────────────┘
```

- **Hadapi**: Lawan musuh untuk dapatkan HP & Power upgrade
- **Kabur**: Cari peti harta karun untuk memperkuat diri tanpa bertarung

---

## ⚙️ Fitur Game

### 1. **Sistem Toko Senjata** ✨ BARU!
   - Beli senjata dengan gold yang dikumpulkan
   - 8 senjata dengan power bonus berbeda (25 - 220 power)
   - Akses toko kapan saja di antara pertemuan atau setelah kemenangan
   - Senjata yang lebih baik = harga lebih mahal tapi bonus lebih besar

### 2. **📈 Upgrade Rewards yang JAUH LEBIH BESAR** ✨ UPDATED!

**Dari Musuh Dikalahkan:**
- Max HP: +60% (naik dari 50%)
- Power: +120% (naik dari 80% → DOUBLE POWER!)
- Gold: ×2.5 multiplier (naik dari 1.5x)

**Dari Peti Harta Karun:**
- Senjata: +80-150 Power (naik dari 40-80)
- Armor: +25-40 Defense (naik dari 15-25)
- Gold: +150-250 Gold (naik dari 50-100 → SANGAT BANYAK!)

**Senjata di Toko (Power lebih besar, harga lebih terjangkau):**
- Pedang Besi: +35 Power (dari 25)
- Pedang Baja: +75 Power (dari 50)
- Pedang Perak: +120 Power (dari 75)
- Pedang Emas: +180 Power (dari 120)
- Pedang Legenda: +280 Power (dari 200)
- Kapak: +200 Power (dari 150)
- Tombak: +250 Power (dari 180)
- Glaive: +320 Power (dari 220)

### 3. **Sistem Pertarungan**
   - Pilih aksi: `serang`, `pertahan`, atau `minum` (potion)
   - Pertahanan mengurangi damage 50%
   - Potion mengembalikan 30 HP (biaya: 20 Gold)

### 4. **Musuh Variatif**
   - Setiap musuh memiliki tipe unik (Lemah, Normal, Kuat, Bos Mini)
   - Ada musuh yang bisa dikalahkan dan ada yang harus dihindari dulu
   - Sistem warning jika selisih kekuatan terlalu jauh

### 5. **Input Validation**
   - Setiap pilihan memiliki contoh input yang benar
   - Jika input salah, Anda diminta memasukkan ulang

---

## 👤 Komponen Game

### Player (Pemain)
```
Nama         : Nama karakter Anda
HP           : 100 → Dapat bertambah dari musuh yang dikalahkan
Weapon Power : 20  → Dapat bertambah dari musuh yang dikalahkan
Armor        : 10  (dapat di-upgrade dari peti)
Gold         : 0   (dari kemenangan musuh dan peti)
```

### Enemy (Musuh)

Setiap musuh memiliki **4 tipe dengan tingkat kesulitan berbeda**:

| Tipe | Simbol | Multiplier | Deskripsi | Strategi |
|------|--------|-----------|-----------|----------|
| **Lemah** | 👶 | 0.5x base power | Mudah dikalahkan | ⚔️ Hadapi langsung |
| **Normal** | 👹 | 1.0x base power | Seimbang | ⚔️ Hadapi atau upgrade |
| **Kuat** | 💪 | 1.5x base power | Butuh strategi | 🏃 Upgrade dulu, baru hadapi |
| **Bos Mini** | 👿 | 2.0x base power | Sangat kuat! | 🏃 Harus upgrade banyak atau skip |

#### Contoh Musuh di Setiap Stage:

**Stage 1 (Level Mudah):**
- 👶 Goblin Pengganggu (power 40)
- 👹 Goblin Prajurit (power 100)
- 💪 Goblin Kepala (power 195)

**Stage 2 (Level Normal):**
- 👶 Orc Pemula (power 100)
- 👹 Orc Penyerang (power 150)
- 💪 Orc Kepala Suku (power 300)
- 👿 Orc Berserker (power 500)

**Stage 3 (Level Sulit):**
- 👶 Werewolf Muda (power 130)
- 👹 Werewolf Dewasa (power 270)
- 💪 Werewolf Alpha (power 375)
- 👿 Werewolf Kuno (power 640)
- 👿 Werewolf Raja (power 760)

**Stage 4 (Level Sangat Sulit):**
- 👶 Vampire Muda (power 160)
- 👹 Vampire Gelap (power 330)
- 💪 Vampire Petualang (power 450)
- 👿 Vampire Gaib (power 760)
- 👿 Vampire Raja Malam (power 900)
- 👿 Naga Hitam (power 1000)

**Stage 5 (Final Boss):**
- 👿 Dark Lord - Penguasa Kegelapan (power 600)
  - Pelawan 3 ronde sekaligus
  - Saat menang: Dapat Senjata Emas + Armor Emas

### Treasure (Harta Karun) ✨ MASSIVELY INCREASED!
```
Tipe Peti (SANGAT BANYAK REWARD):
├─ Senjata  : +80 sampai +150 power (dari 40-80)
├─ Armor    : +25 sampai +40 defense (dari 15-25)
└─ Gold     : +150 sampai +250 gold (dari 50-100) ← REWARD TERBESAR!
```

**Keuntungan Treasure Gold:**
- 3-4 kali menemukan peti gold = 450-1000 gold
- Cukup untuk beli 2-3 senjata tier menengah!
- Strategis: kabur dari musuh kuat → cari peti gold → belanja → hadapi musuh

### Weapon Shop (Toko Senjata) ✨ UPDATED!

Beli senjata dengan gold untuk upgrade power lebih cepat (harga lebih terjangkau, power lebih besar!):

| No | Senjata | Power Bonus | Harga |
|----|---------|-----------| -----|
| 1 | Pedang Besi | +35 | 80 Gold |
| 2 | Pedang Baja | +75 | 150 Gold |
| 3 | Pedang Perak | +120 | 250 Gold |
| 4 | Pedang Emas | +180 | 400 Gold |
| 5 | Pedang Legenda | +280 | 600 Gold |
| 6 | Kapak Penghancur | +200 | 450 Gold |
| 7 | Tombak Langit | +250 | 550 Gold |
| 8 | Glaive Neraka | +320 | 700 Gold |

**Cara Akses Toko:**
- Menu saat pertemuan musuh (pilih 'toko')
- Setelah kemenangan melawan musuh
- Sebelum memasuki stage baru

---

## 🎭 Sistem Musuh (AI Strategi)

### Tipe Musuh & Rekomendasi

#### 👶 Musuh Lemah
- Power: 0.5x base
- HP: Direkomendasikan untuk dihadapi
- Bonus kecil tapi pasti menang
- **Strategi**: Hadapi langsung tanpa ragu

#### 👹 Musuh Normal
- Power: 1.0x base
- HP: Bisa dikalahkan dengan strategi
- Bonus sedang
- **Strategi**: Pertimbangkan upgrade armor dulu atau hadapi langsung

#### 💪 Musuh Kuat
- Power: 1.5x base
- HP: Butuh upgrade sebelum hadapi
- Bonus besar (30% max HP + 50% power)
- **Strategi**: ⚠️ Upgrade armor/weapon dulu, baru hadapi

#### 👿 Musuh Bos Mini
- Power: 2.0x base
- HP: Sangat tinggi
- Bonus sangat besar
- **Strategi**: 🏃 SANGAT DIREKOMENDASIKAN UNTUK SKIP/KABUR dulu!

### Warning System
Game otomatis memberikan peringatan ketika Anda menemui musuh yang **jauh lebih kuat**:
```
⚠️  PERINGATAN: Musuh ini jauh lebih kuat dari Anda!
💡 Saran: Kabur dulu untuk mencari upgrade (peti)
```

---

## 🎭 Sistem Stage

Game terdiri dari **5 Stage** dengan tingkat kesulitan yang meningkat:

| Stage | Level | Jumlah Musuh | Difficulty | Tipe Musuh |
|-------|-------|-------------|------------|-----------|
| 1 | 1 | 3 | 😊 Mudah | Goblin (1 kuat, rest normal) |
| 2 | 2 | 4 | 😐 Normal | Orc (1 bos, rest beragam) |
| 3 | 3 | 5 | 😠 Sulit | Werewolf (3 bos, rest beragam) |
| 4 | 4 | 6 | 😡 Very Hard | Vampire & Naga (2+ bos) |
| 5 | Final | 1 (3 ronde) | 💀 EKSTREM | Dark Lord |

### Setiap Stage:
- Terdiri dari beberapa pertemuan musuh unik
- Anda bisa memilih hadapi langsung atau kabur cari peti
- Jika kekalahan, bisa menyerah atau lanjut cari peti untuk upgrade
- Harus selesaikan semua musuh untuk lanjut ke stage berikutnya
- Game otomatis memberi rekomendasi berdasarkan kekuatan relatif

### Stage Terakhir (Boss Battle):
- Hadapi **Dark Lord** dalam **3 ronde pertarungan**
- Power awal: 600 setelah multiplier (kuat sekali!)
- Setiap ronde adalah kesempatan untuk defeat/heal/defend
- **Kemenangan**: Senjata Emas + Armor Emas + bonus power 100
- **Kekalahan**: Reset semua item & stat (tapi bisa main ulang)

---

## 💡 Tips dan Trik

### Strategi Bertahan Hidup - UPDATED!
1. **Kelola Gold dengan Optimal**: Gold sekarang reward-nya BESAR! 150-250 dari peti saja
2. **Hadapi Musuh Lemah Duluan**: 
   - Dapatkan +120% power dari musuh
   - +250 gold dari reward musuh
   - Cukup untuk 2-3 senjata immediately!
3. **Kabur Strategis untuk Peti Gold**:
   - Musuh terlalu kuat? Kabur & cari peti
   - Peti gold: 150-250 (bisa beli senjata bagus!)
4. **Investasi Senjata**: Harga lebih murah, power lebih besar → ROI bagus!
5. **Kombinasi Strategi**: Musuh bonus + treasure gold + belanja senjata = OP!

### Urutan Strategi Optimal (UPDATED!) ✨
```
Stage 1: 
  └─ Hadapi musuh lemah (Goblin) → +24 power, +125 gold
  └─ Beli Pedang Besi (80 gold) → +35 power (total ~60 power)
  └─ Hadapi musuh normal (Goblin Prajurit) → +120 power, +250 gold
  
Stage 2-4:
  ├─ Sebelum stage: Buka toko, belanja tier menengah (Perak/Emas)
  ├─ Hadapi musuh: Kombinasi hadapi normal + kabur cari peti
  ├─ Reward musuh: 2.5x gold = 250-375 per musuh
  ├─ Reward peti: 150-250 gold per peti
  └─ Beli 3-4 senjata tier bagus sebelum hadapi bos

Stage 5 (Boss):
  ├─ Weapon: 300+ (dari musuh bonus + senjata)
  ├─ Armor: 50+ (dari peti + upgrade)
  └─ HP: 400+ (dari bonus musuh)
```

### Contoh Progression Riil
```ini
Awal Stage 1:         Power 20
Hadapi 1 Goblin:      Power 20 + 24 = 44
Beli Pedang Besi:     Power 44 + 35 = 79
Hadapi 1 Goblin Prajurit: Power 79 + 120 = 199
Total Gold setelah: 125 + 250 = 375 gold

Dengan 375 gold bisa membeli:
- Pedang Perak (250) + Pedang Besi (80) = selesai
- Atau Pedang Emas (400) - belum cukup tapi close
```

### Tips Finansial Game - UPDATED!
- **Early Game (Stage 1)**: Focus hadapi musuh lemah = 125-250 gold each
- **Mid Game (Stage 2-3)**: Mulai beli senjata tier menengah (Perak 250, Emas 400)
- **Late Game (Stage 4-5)**: Beli senjata tier tinggi atau gunakan bonus musuh
- **Treasure Priority**: Gold treasure adalah yang terbaik (150-250 = 1-2 senjata!)

### Pemain Baru
- Jangan takut kabur dari musuh kuat - peti gold menanti!
- 1-2 peti saja bisa beli senjata bagus
- Musuh dikalahkan memberikan power DOUBLE (120%) - sangat worth it!
- Setiap permainan berbeda - experiment berbagai strategi!

---

## 🚀 Cara Menjalankan

### Requirements
- Python 3.6 atau lebih tinggi
- Tidak perlu library tambahan (hanya built-in)

### Menjalankan Game
```bash
python main.py
```

### Input Contoh
```
Nama pemain: [Pahlawan]
Hadapi/Kabur?: [hadapi] atau [kabur]
Aksi pertarungan: [serang] atau [pertahan] atau [minum]
Lanjut?: [ya] atau [tidak]
```

---

## 🎮 Contoh Gameplay (UPDATED dengan Toko)

```
==================================================
STAGE 1 - LEVEL KESULITAN: 1
==================================================

Pertemuan 1: Musuh muncul!

👶 Lemah MUSUH: Goblin Pengganggu
   HP: 60/60
   Power: 20
   ✅ Musuh ini bisa dikalahkan

Apa yang ingin kamu lakukan?
  1⚔️  'hadapi'  - Hadapi musuh
  2🏃 'kabur'   - Cari peti/jalan lain untuk upgrade
  3🏪 'toko'    - Buka toko senjata

Pilih (hadapi/kabur/toko): [hadapi]

==================================================
⚔️  PERTARUNGAN DIMULAI!
==================================================

Pilihan Aksi:
  1⚔️   'serang' - Serang musuh
  2🛡️   'pertahan' - Pertahan diri
  3💊  'minum' - Minum potion

Pilih aksi (serang/pertahan/minum): [serang]

💥 Anda menyerang! Damage: 22
✅ Goblin Pengganggu berhasil dikalahkan!

💪 Anda mendapatkan bonus dari musuh!
   HP Maximum: +30 (Total: 130)        [50% dari max HP musuh]
   Weapon Power: +16 (Total: 36)       [80% dari power musuh]
   💰 Reward: Gold +75                 [1.5x base reward]

==================================================
┌─ 📊 STATUS PEMAIN: Pahlawan
├─ HP: 130/130
├─ Kekuatan Senjata: 36
├─ Armor: 10
├─ Gold: 75
└─ Stage: 1
==================================================

Kemenangan! Apakah ingin membuka toko senjata?
  'ya'  - Buka toko
  'tidak' - Lanjut

Pilih (ya/tidak): [ya]

============================================================
🏪 TOKO SENJATA
============================================================

💰 Gold Anda saat ini: 75

Senjata yang tersedia:

1. ❌ Pedang Besi (+25 Power, Harga: 100 Gold)
2. ❌ Pedang Baja (+50 Power, Harga: 200 Gold)
3. ❌ Pedang Perak (+75 Power, Harga: 300 Gold)
4. ❌ Pedang Emas (+120 Power, Harga: 500 Gold)
5. ❌ Pedang Legenda (+200 Power, Harga: 800 Gold)
6. ❌ Kapak Penghancur (+150 Power, Harga: 600 Gold)
7. ❌ Tombak Langit (+180 Power, Harga: 700 Gold)
8. ❌ Glaive Neraka (+220 Power, Harga: 900 Gold)

0. Keluar dari toko

Pilih senjata (1-8) atau 0 untuk keluar: [0]

👋 Keluar dari toko...

... (lanjut pertemuan berikutnya)
```

---

## 🏆 Kondisi Kemenangan & Kekalahan

### Kemenangan
✅ Kalahkan semua musuh di Stage 1-4
✅ Kalahkan Dark Lord dalam 3 ronde
✅ Dapatkan Senjata Emas + Armor Emas

### Kekalahan
❌ Pilih "menyerah" saat dikalahkan musuh
❌ Kalah dari Dark Lord di Stage 5

---

## 📝 Catatan Penting

### Versi 2.2 - MASSIVE BALANCE UPDATE! ✨ LATEST!
- **Gold Rewards**: Peti treasure +150-250 gold (3-5x lebih besar!)
- **Power Rewards**: Musuh dikalahkan +120% power (DOUBLE dari sebelum!)
- **Senjata**: Power lebih besar (35-320), harga lebih terjangkau
- **Hasil**: Pemain bisa beli BANYAK senjata & rapid progression!

### Previous Updates
- v2.1: Toko senjata added
- v2.0: Musuh variatif dengan bonus system
- v1.0: Game awal dengan pertarungan basic

### General Notes
- **Random System**: Musuh sudah ditentukan per stage, peti random
- **Text-Based Game**: Berbasis teks tanpa grafis kompleks
- **Strategic Gameplay**: Ada 3 pilihan aksi: hadapi vs kabur vs belanja
- **Ekonomi Game**: Gold sekarang PENTING untuk progression cepat
- **Warning System**: Game membantu dengan rekomendasi otomatis

---

## 🎊 Selamat Bermain!

Terima kasih telah memainkan **Mystery Adventure Game**. Semoga Anda menikmati petualangan yang penuh misteri, strategi, dan excitement ini!

**Apakah Anda siap menghadapi tantangan? Mari dimulai!** 🚀

```bash
python main.py
```

---

**Dibuat dengan ❤️ untuk para petualang sejati**
**v2.2 - MASSIVE BALANCE UPDATE - Gold & Power Rewards Diperbanyak!**