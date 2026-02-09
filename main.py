import random
import time

# ==================== KELAS GAME ====================

class Weapon:
    """Kelas untuk senjata yang dapat dibeli di toko"""
    def __init__(self, name, power_bonus, price):
        self.name = name
        self.power_bonus = power_bonus
        self.price = price
    
    def display(self):
        return f"{self.name} (+{self.power_bonus} Power, Harga: {self.price} Gold)"

# Daftar senjata yang tersedia di toko
SHOP_WEAPONS = [
    Weapon("Pedang Besi", 35, 80),
    Weapon("Pedang Baja", 75, 150),
    Weapon("Pedang Perak", 120, 250),
    Weapon("Pedang Emas", 180, 400),
    Weapon("Pedang Legenda", 280, 600),
    Weapon("Kapak Penghancur", 200, 450),
    Weapon("Tombak Langit", 250, 550),
    Weapon("Glaive Neraka", 320, 700),
]


class ShopSystem:
    """Sistem toko untuk membeli senjata"""
    def __init__(self):
        self.weapons = SHOP_WEAPONS
    
    def display_shop(self, player_gold):
        """Tampilkan senjata yang tersedia"""
        print(f"\n{'='*60}")
        print("🏪 TOKO SENJATA")
        print(f"{'='*60}\n")
        print(f"💰 Gold Anda saat ini: {player_gold}\n")
        print("Senjata yang tersedia:\n")
        
        for idx, weapon in enumerate(self.weapons, 1):
            affordable = "✅" if player_gold >= weapon.price else "❌"
            print(f"{idx}. {affordable} {weapon.display()}")
        
        print(f"\n0. Keluar dari toko")
        print(f"{'='*60}\n")
    
    def buy_weapon(self, player, weapon_index):
        """Beli senjata"""
        if weapon_index < 1 or weapon_index > len(self.weapons):
            return False, "Pilihan tidak valid!"
        
        weapon = self.weapons[weapon_index - 1]
        
        if player.gold < weapon.price:
            return False, f"❌ Gold tidak cukup! (Butuh: {weapon.price}, Punya: {player.gold})"
        
        player.gold -= weapon.price
        player.weapon_power += weapon.power_bonus
        
        return True, f"✅ Berhasil membeli {weapon.name}! Weapon Power +{weapon.power_bonus}"

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.weapon_power = 20
        self.armor = 10
        self.gold = 0
        self.stage = 1
        self.has_golden_weapon = False
        self.has_golden_armor = False
    
    def take_damage(self, damage):
        reduced_damage = max(1, damage - self.armor)
        self.hp -= reduced_damage
        return reduced_damage
    
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
    
    def upgrade_weapon(self, power):
        self.weapon_power += power
        self.gold -= 50
    
    def upgrade_armor(self, defense):
        self.armor += defense
        self.gold -= 50
    
    def display_stats(self):
        print(f"\n{'='*50}")
        print(f"┌─ 📊 STATUS PEMAIN: {self.name}")
        print(f"├─ HP: {self.hp}/{self.max_hp}")
        print(f"├─ Kekuatan Senjata: {self.weapon_power}")
        print(f"├─ Armor: {self.armor}")
        print(f"├─ Gold: {self.gold}")
        print(f"└─ Stage: {self.stage}")
        
        if self.has_golden_weapon:
            print(f"⭐ Memiliki Senjata Emas")
        if self.has_golden_armor:
            print(f"⭐ Memiliki Armor Emas")
        print(f"{'='*50}\n")


class Enemy:
    """Kelas Enemy dengan berbagai tipe dan kesulitan"""
    TYPES = {
        'weak': {'multiplier': 0.5, 'symbol': '👶', 'description': 'Lemah'},
        'normal': {'multiplier': 1.0, 'symbol': '👹', 'description': 'Normal'},
        'strong': {'multiplier': 1.5, 'symbol': '💪', 'description': 'Kuat'},
        'boss': {'multiplier': 2.0, 'symbol': '👿', 'description': 'Bos Mini'},
    }
    
    def __init__(self, name, power, reward, enemy_type='normal'):
        self.name = name
        self.enemy_type = enemy_type
        self.base_power = power
        self.power = int(power * self.TYPES[enemy_type]['multiplier'])
        self.hp = int(self.power * 3)
        self.max_hp = self.hp
        self.reward = reward
        self.is_boss = False
        self.can_defeat = self.base_power <= 150  # Musuh yang bisa dikalahkan
    
    def take_damage(self, damage):
        self.hp -= damage
    
    def get_damage(self):
        variance = random.randint(-5, 5)
        return max(10, self.power + variance)
    
    def get_difficulty_indicator(self):
        """Return emoji indikator kesulitan"""
        type_info = self.TYPES[self.enemy_type]
        return f"{type_info['symbol']} {type_info['description']}"
    
    def display_info(self):
        difficulty = self.get_difficulty_indicator()
        print(f"\n{difficulty} MUSUH: {self.name}")
        print(f"   HP: {self.hp}/{self.max_hp}")tidak
        print(f"   Power: {self.power}")
        
        # Tampilkan rekomendasi
        if not self.can_defeat:
            print(f"   ⚠️  MUSUH SANGAT KUAT! Disarankan KABUR terlebih dahulu!")
        else:
            print(f"   ✅ Musuh ini bisa dikalahkan")
        print()


class Treasure:
    def __init__(self, treasure_type):
        self.type = treasure_type  # 'weapon' atau 'armor'
        
        if treasure_type == 'weapon':
            self.reward = random.randint(80, 150)  # Increased from 40-80
        elif treasure_type == 'armor':
            self.reward = random.randint(25, 40)  # Increased from 15-25
        else:
            self.reward = random.randint(150, 250)  # Increased from 50-100 (BANYAK GOLD!)
    
    def open(self, player):
        if self.type == 'weapon':
            print(f"\n✨ Anda menemukan Peti Senjata! Power +{self.reward}")
            player.weapon_power += self.reward
        elif self.type == 'armor':
            print(f"\n✨ Anda menemukan Peti Armor! Defense +{self.reward}")
            player.armor += self.reward
        else:
            print(f"\n✨ Anda menemukan Peti Harta Karun! Gold +{self.reward}")
            player.gold += self.reward
        
        time.sleep(1)


class Stage:
    def __init__(self, stage_num):
        self.stage_num = stage_num
        self.level = stage_num
        self.enemies = []
        self.create_enemies()
    
    def create_enemies(self):
        """Buat musuh dengan variasi tipe yang berbeda"""
        base_power = 100 + (self.level - 1) * 50
        
        enemy_pool = {
            1: [
                ("Goblin Pengganggu", 80, 40, 'weak'),
                ("Goblin Prajurit", 100, 60, 'normal'),
                ("Goblin Kepala", 130, 80, 'strong'),
            ],
            2: [
                ("Orc Pemula", 100, 60, 'weak'),
                ("Orc Penyerang", 150, 100, 'normal'),
                ("Orc Kepala Suku", 200, 120, 'strong'),
                ("Orc Berserker", 250, 150, 'boss'),
            ],
            3: [
                ("Werewolf Muda", 130, 80, 'weak'),
                ("Werewolf Dewasa", 180, 120, 'normal'),
                ("Werewolf Alpha", 250, 150, 'strong'),
                ("Werewolf Kuno", 320, 180, 'boss'),
                ("Werewolf Raja", 380, 200, 'boss'),
            ],
            4: [
                ("Vampire Muda", 160, 100, 'weak'),
                ("Vampire Gelap", 220, 150, 'normal'),
                ("Vampire Petualang", 300, 180, 'strong'),
                ("Vampire Gaib", 380, 220, 'boss'),
                ("Vampire Raja Malam", 450, 250, 'boss'),
                ("Naga Hitam", 500, 280, 'boss'),
            ],
            5: [
                ("Demon Kecil", 200, 120, 'weak'),
                ("Demon Menengah", 280, 160, 'normal'),
                ("Demon Kuat", 380, 200, 'strong'),
                ("Demon Raja Dimensional", 550, 300, 'boss'),
            ],
        }
        
        enemies_for_stage = enemy_pool.get(self.level, [])
        
        for enemy_name, power, reward, enemy_type in enemies_for_stage:
            self.enemies.append(Enemy(enemy_name, power, reward, enemy_type))
    
    def get_next_enemy(self):
        if self.enemies:
            return self.enemies.pop(0)
        return None


# ==================== FUNGSI UTILITY ====================

def clear_screen():
    """Membersihkan layar terminal"""
    print("\033[2J\033[H", end="")

def display_title():
    """Menampilkan judul game"""
    print("\n" + "="*60)
    print(" "*15 + "🎮 MYSTERY ADVENTURE GAME 🎮")
    print("="*60)
    print("\n  Selamat datang di dunia penuh misteri!")
    print("  Kamu akan menghadapi berbagai musuh dan tantangan.")
    print("  Carilah harta karun untuk memperkuat dirimu!")
    print("\n" + "="*60 + "\n")

def get_valid_input(prompt, valid_options):
    """Mendapatkan input yang valid dari pemain"""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in valid_options:
            return user_input
        else:
            options_str = ", ".join([f"'{opt}'" for opt in valid_options])
            print(f"\n❌ Input salah! Pilihan yang benar: {options_str}")
            print()

def choose_direction():
    """Pemain memilih arah"""
    print("\nPilih arah untuk dilanjutkan:")
    print("  1️⃣  'depan' - Hadapi musuh di depan")
    print("  2️⃣  'kanan' - Jelajahi ke kanan (cari harta karun)")
    print("  3️⃣  'kiri'  - Jelajahi ke kiri (cari harta karun)")
    print()
    
    direction = get_valid_input("Pilih arah (depan/kanan/kiri): ", ['depan', 'kanan', 'kiri'])
    return direction

def open_shop_option(player):
    """Tanya pemain apakah ingin buka toko"""
    print("\nApakah ingin membuka TOKO SENJATA?")
    print("  'ya'  - Buka toko")
    print("  'tidak' - Lanjut permainan")
    print()
    
    choice = get_valid_input("Pilih (ya/tidak): ", ['ya', 'tidak'])
    
    if choice == 'ya':
        open_weapon_shop(player)

def open_weapon_shop(player):
    """Buka toko senjata"""
    shop = ShopSystem()
    
    while True:
        shop.display_shop(player.gold)
        
        choice = input("Pilih senjata (1-8) atau 0 untuk keluar: ").strip()
        
        if choice == '0':
            print("\n👋 Keluar dari toko...\n")
            break
        
        try:
            weapon_index = int(choice)
            success, message = shop.buy_weapon(player, weapon_index)
            
            if success:
                print(f"\n{message}")
                player.display_stats()
                
                # Tanya apakah ingin membeli lagi
                print("\nBeli senjata lagi?")
                print("  'ya'  - Lanjut berbelanja")
                print("  'tidak' - Keluar dari toko")
                
                choice_again = get_valid_input("Pilih (ya/tidak): ", ['ya', 'tidak'])
                if choice_again == 'tidak':
                    print("\n👋 Keluar dari toko...\n")
                    break
            else:
                print(f"\n{message}\n")
        
        except ValueError:
            print("\n❌ Masukkan angka yang valid!\n")

# ==================== FUNGSI GAME MECHANIC ====================

def battle(player, enemy, is_boss=False):
    """Sistem pertarungan dengan musuh"""
    print(f"\n{'='*50}")
    print(f"⚔️  PERTARUNGAN DIMULAI!")
    print(f"{'='*50}")
    
    round_num = 1
    max_rounds = 3 if is_boss else 1
    
    while round_num <= max_rounds:
        if is_boss:
            print(f"\n🏆 PERTARUNGAN RONDE {round_num}/{max_rounds} 🏆\n")
        
        enemy.display_info()
        
        print("\nPilihan Aksi:")
        print("  1⚔️   'serang' - Serang musuh")
        print("  2🛡️   'pertahan' - Pertahan diri (mengurangi damage 50%)")
        print("  3💊  'minum' - Minum potion (heal 30 HP)")
        print()
        
        action = get_valid_input("Pilih aksi (serang/pertahan/minum): ", ['serang', 'pertahan', 'minum'])
        
        # Aksi pemain
        if action == 'serang':
            damage = player.weapon_power + random.randint(-10, 10)
            enemy.take_damage(damage)
            print(f"\n💥 Anda menyerang! Damage: {damage}")
        
        elif action == 'pertahan':
            print(f"\n🛡️  Anda mempertahankan diri!")
        
        elif action == 'minum':
            if player.gold >= 20:
                player.heal(30)
                player.gold -= 20
                print(f"\n💊 Anda minum potion! HP: +30 (Gold: -20)")
            else:
                print(f"\n❌ Gold tidak cukup! (Butuh: 20, Punya: {player.gold})")
                continue
        
        # Cek apakah musuh sudah mati
        if enemy.hp <= 0:
            print(f"\n✅ {enemy.name} berhasil dikalahkan!")
            
            # Pemain mendapatkan HP dan Power dari musuh (MASSIVELY INCREASED BONUS)
            hp_gain = int(enemy.max_hp * 0.6)  # Increased from 0.5 to 0.6
            power_gain = int(enemy.power * 1.2)  # Increased from 0.8 to 1.2 (DOUBLE POWER!)
            
            player.max_hp += hp_gain
            player.hp = player.max_hp
            player.weapon_power += power_gain
            
            # Tambahan gold reward
            gold_reward = int(enemy.reward * 2.5)  # Increased reward from 1.5 to 2.5
            
            print(f"💪 Anda mendapatkan bonus dari musuh!")
            print(f"   HP Maximum: +{hp_gain} (Total: {player.max_hp})")
            print(f"   Weapon Power: +{power_gain} (Total: {player.weapon_power})")
            print(f"   💰 Reward: Gold +{gold_reward}")
            
            player.gold += gold_reward
            return True
        
        # Aksi musuh
        if action != 'pertahan':
            enemy_damage = enemy.get_damage()
            reduced_damage = player.take_damage(enemy_damage)
            print(f"👹 {enemy.name} menyerang! Damage: {reduced_damage}")
        else:
            enemy_damage = enemy.get_damage() // 2
            reduced_damage = player.take_damage(enemy_damage)
            print(f"👹 {enemy.name} menyerang! Damage: {reduced_damage} (Pertahanan -50%)")
        
        # Cek status pemain
        if player.hp <= 0:
            print(f"\n❌ Anda telah dikalahkan!\n")
            return False
        
        player.display_stats()
        round_num += 1
        time.sleep(1)
    
    return True

def handle_treasure_choice(player):
    """Pemain menemukan peti harta karun"""
    print("\n" + "="*50)
    print("🎁 ANDA MENEMUKAN PETI HARTA KARUN!")
    print("="*50)
    
    treasure = Treasure(random.choice(['weapon', 'armor', 'gold']))
    treasure.open(player)
    
    player.display_stats()
    
    # Tanya apakah ingin ke toko
    open_shop_option(player)

def stage_encounter(player, stage):
    """Pertemuan di setiap stage"""
    print(f"\n{'='*50}")
    print(f"🎭 STAGE {stage.stage_num} - LEVEL KESULITAN: {stage.level}")
    print(f"{'='*50}\n")
    
    encounter_count = 0
    
    while True:
        enemy = stage.get_next_enemy()
        
        if enemy is None:
            print(f"\n✨ Anda telah menyelesaikan Stage {stage.stage_num}!")
            print(f"Lanjut ke Stage berikutnya...\n")
            time.sleep(2)
            return True
        
        encounter_count += 1
        print(f"\n{'─'*50}")
        print(f"Pertemuan {encounter_count}: Musuh muncul!\n")
        
        player.display_stats()
        enemy.display_info()
        
        # Rekomendasi berdasarkan power musuh vs pemain
        if enemy.power > player.weapon_power * 1.5:
            print("⚠️  PERINGATAN: Musuh ini jauh lebih kuat dari Anda!")
            print("   💡 Saran: Kabur dulu untuk mencari upgrade (peti) atau beli senjata")
            print()
        
        # Tanyakan pilihan kepada pemain
        print("Apa yang ingin kamu lakukan?")
        print("  1⚔️   'hadapi' - Hadapi musuh")
        print("  2🏃  'kabur'  - Cari peti/jalan lain untuk upgrade")
        print("  3🏪  'toko'   - Buka toko senjata")
        print()
        
        choice = get_valid_input("Pilih (hadapi/kabur/toko): ", ['hadapi', 'kabur', 'toko'])
        
        if choice == 'toko':
            # Buka toko senjata
            open_weapon_shop(player)
            # Tampilkan musuh lagi setelah keluar toko
            print(f"\n{'─'*50}")
            print(f"Musuh masih menunggu Anda!\n")
            enemy.display_info()
            print("\nApa yang ingin kamu lakukan?")
            print("  1⚔️   'hadapi' - Hadapi musuh")
            print("  2🏃  'kabur'  - Cari peti/jalan lain untuk upgrade")
            print()
            choice = get_valid_input("Pilih (hadapi/kabur): ", ['hadapi', 'kabur'])
        
        if choice == 'hadapi':
            result = battle(player, enemy)
            
            if not result:
                # Pemain kalah
                print(f"\n{'='*50}")
                print("💀 Anda Dikalahkan!")
                print(f"{'='*50}\n")
                
                print("Pilihan:")
                print("  1 - Menyerah (Game Over)")
                print("  2 - Cari peti untuk memperkuat diri dan coba lagi")
                print()
                
                choice = get_valid_input("Pilih (menyerah/cari): ", ['menyerah', 'cari'])
                
                if choice == 'menyerah':
                    return False
                else:
                    handle_treasure_choice(player)
                    player.hp = player.max_hp  # Restore HP setelah mencari peti
            else:
                player.display_stats()
                
                # Tanya apakah ingin buka toko setelah kemenangan
                print("Kemenangan! Apakah ingin membuka toko senjata?")
                print("  'ya'  - Buka toko")
                print("  'tidak' - Lanjut")
                print()
                
                choice = get_valid_input("Pilih (ya/tidak): ", ['ya', 'tidak'])
                if choice == 'ya':
                    open_weapon_shop(player)
        
        else:  # kabur
            print("\n🏃 Anda memilih untuk kabur dan mencari peti...")
            handle_treasure_choice(player)

def boss_battle(player):
    """Pertarungan dengan musuh utama (3 ronde)"""
    print(f"\n{'='*60}")
    print("⚡ ANDA TELAH SAMPAI KE TAHAP AKHIR!")
    print("⚡ HADAPI MUSUH UTAMA DALAM 3 RONDE PERTARUNGAN!")
    print(f"{'='*60}\n")
    
    time.sleep(2)
    
    boss = Enemy("DARK LORD - PENGUASA KEGELAPAN", 300, 500, 'boss')
    boss.is_boss = True
    boss.display_info()
    
    result = battle(player, boss, is_boss=True)
    
    if result:
        print(f"\n{'='*60}")
        print("🏆 VICTORY! ANDA TELAH MENGALAHKAN MUSUH UTAMA! 🏆")
        print(f"{'='*60}\n")
        
        print("⭐ REWARD LUAR BIASA! ⭐")
        print("  🔱 Senjata Emas diterima!")
        print("  🛡️  Armor Emas diterima!")
        
        player.has_golden_weapon = True
        player.has_golden_armor = True
        player.weapon_power += 100
        player.armor += 50
        
        player.display_stats()
        return True
    else:
        print(f"\n{'='*60}")
        print("💀 ANDA KALAH DARI MUSUH UTAMA!")
        print("❌ SEMUA HADIAH AKAN HILANG!")
        print(f"{'='*60}\n")
        
        player.has_golden_weapon = False
        player.has_golden_armor = False
        player.gold = 0
        player.weapon_power = 20
        player.armor = 10
        player.max_hp = 100
        player.hp = 100
        
        print("Statistik Anda telah direset...")
        time.sleep(2)
        return False

def play_game(player_name):
    """Loop utama game"""
    player = Player(player_name)
    current_stage = 1
    
    display_title()
    print(f"Selamat datang, {player_name}!\n")
    player.display_stats()
    time.sleep(2)
    
    while current_stage <= 5:
        # Menu sebelum stage (jika bukan stage 1)
        if current_stage > 1:
            print("\n" + "="*50)
            print(f"Bersiaplah untuk STAGE {current_stage}!")
            print("="*50)
            print("\nToko terbuka sebelum stage baru!")
            print("Apakah ingin masuk toko untuk belanja senjata?")
            print("  'ya'  - Buka toko")
            print("  'tidak' - Lanjut ke stage")
            print()
            
            choice = get_valid_input("Pilih (ya/tidak): ", ['ya', 'tidak'])
            
            if choice == 'ya':
                open_weapon_shop(player)
            
            time.sleep(1)
        
        if current_stage == 5:
            # Stage terakhir - hadapi boss
            result = boss_battle(player)
            if result:
                return True  # Game dimenangkan
            else:
                return False  # Game dikalahkan
        
        else:
            # Stage biasa
            stage = Stage(current_stage)
            result = stage_encounter(player, stage)
            
            if not result:
                return False  # Kalah/Menyerah
            
            current_stage += 1

def main():
    """Fungsi utama"""
    while True:
        clear_screen()
        display_title()
        
        print("Masukkan nama pemain Anda:")
        print("(Hanya huruf dan angka, minimum 3 karakter)")
        print()
        
        while True:
            name = input("Nama pemain: ").strip()
            if len(name) >= 3 and name.replace('_', '').isalnum():
                break
            else:
                print("❌ Nama tidak valid! Gunakan huruf/angka minimal 3 karakter.\n")
        
        result = play_game(name)
        
        # Tampilkan hasil akhir
        print(f"\n{'='*60}")
        if result:
            print("🎊 ANDA TELAH MENYELESAIKAN GAME! 🎊")
            print("Terima kasih telah bermain Mystery Adventure!")
        else:
            print("💀 GAME OVER!")
            print("Lebih baik keberuntungan di permainan berikutnya!")
        print(f"{'='*60}\n")
        
        # Tanya apakah ingin bermain lagi
        print("Apakah ingin bermain lagi?")
        print("  'ya'  - Bermain lagi")
        print("  'tidak' - Keluar game")
        print()
        
        choice = get_valid_input("Pilih (ya/tidak): ", ['ya', 'tidak'])
        
        if choice == 'tidak':
            print("\n👋 Terima kasih telah bermain Mystery Adventure!")
            print("   Sampai jumpa lagi!\n")
            break


# ==================== MAIN PROGRAM ====================

if __name__ == "__main__":
    main()
