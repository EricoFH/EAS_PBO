import random
import player
import enemy
import inventory

def battle():
    if random.randint(1, 100) <= 20:
        current_enemy = random.choice(enemy.boss_pool).copy()
        print(f"\nBOSS MUNCUL!")
    else:
        current_enemy = random.choice(enemy.enemy_pool).copy()
    
    print(f"Sebuah {current_enemy['name']} muncul!")

def calculate_damage(attacker): # random damage
    base = attacker["attack"]
    return random.randint(int(base * 0.8), int(base * 1.2))

def is_miss(chance): # random dodge
    return random.randint(1, 100) <= chance

def roll_drops(current_enemy): #loot yang didapat setelah battle
    print("\n=== LOOT ===")
    player.player["gold"] += current_enemy["gold"]
    print(f"Gold +{current_enemy['gold']}")

    for drop in current_enemy["drops"]:
        if random.randint(1, 100) <= drop["chance"]:
            inventory.add_item(drop["item"], drop["type"])

def battle(): # kode untuk battle dengan musuh random
    current_enemy = random.choice(enemy.enemy_pool).copy()
    print(f"\nSebuah {current_enemy['name']} muncul!")

    while current_enemy["hp"] > 0 and player.player["hp"] > 0: # pilihan saat battle
        print(f"\nHP Kamu: {player.player['hp']} | HP {current_enemy['name']}: {current_enemy['hp']}")
        print("1. Attack")
        print("2. Pakai Potion")
        print("3. Kabur")

        choice = input("> ")

        if choice == "1":
            if is_miss(current_enemy["dodge"]):
                print(f"{current_enemy['name']} menghindar!")
            else:
                damage = calculate_damage(player.player)
                current_enemy["hp"] -= damage
                print(f"Kamu menyerang {current_enemy['name']} sebesar {damage} damage!")

            if current_enemy["hp"] > 0:
                if is_miss(player.player["dodge"]):
                    print(f"Kamu menghindar dari serangan {current_enemy['name']}!")
                else:
                    damage = calculate_damage(current_enemy)
                    player.player["hp"] -= damage
                    print(f"{current_enemy['name']} menyerang balik sebesar {damage} damage!")

        elif choice == "2":
            inventory.use_potion()  # Enemy tetap serang setelah pakai potion
            if current_enemy["hp"] > 0:
                if is_miss(player.player["dodge"]):
                    print(f"Kamu menghindar dari serangan {current_enemy['name']}!")
                else:
                    damage = calculate_damage(current_enemy)
                    player.player["hp"] -= damage
                    print(f"{current_enemy['name']} menyerang saat kamu minum potion! {damage} damage!")

        elif choice == "3":
            print("Kamu kabur!")
            break
        else:
            print("Pilihan tidak valid.")

    if current_enemy["hp"] <= 0:
        print(f"\n{current_enemy['name']} kalah!")
        roll_drops(current_enemy)

    if player.player["hp"] <= 0:
        print("\nKamu kalah...")