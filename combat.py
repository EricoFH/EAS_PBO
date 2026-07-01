import random
import player
import enemy
import inventory

def calculate_damage(attacker): #< kita buat sebagai random dmg
    base = attacker["attack"]
    return random.randint(int(base * 0.8), int(base * 1.2))

def is_miss(chance): # kita buat sebagai random dodge
    return random.randint(1, 100) <= chance

def roll_drops(current_enemy): # loot atau hadiah yang didapat 
    print("\n=== LOOT ===")
    player.player["gold"] += current_enemy["gold"]
    print(f"Gold +{current_enemy['gold']}")

    for drop in current_enemy["drops"]:
        if random.randint(1, 100) <= drop["chance"]:
            inventory.add_item(drop["item"], drop["type"])

def check_low_hp_trigger(current_enemy, triggered_flag):
    # mengecek  HP enemy apakah sudah turun di bawah threshold dan trigger belum pernah aktif
    trigger = current_enemy.get("low_hp_trigger")
    if not trigger or triggered_flag["active"]:
        return triggered_flag

    hp_percent = (current_enemy["hp"] / current_enemy["max_hp"]) * 100
    if hp_percent > trigger["threshold"] or current_enemy["hp"] <= 0:
        return triggered_flag

    print(f"\n!!! {trigger['message']} !!!")
    effect_type = trigger["type"]

    if effect_type == "panic":
        current_enemy["dodge"] = max(0, current_enemy["dodge"] - trigger["dodge_penalty"])
        print(f"{current_enemy['name']} menjadi lebih mudah diserang (dodge -{trigger['dodge_penalty']}).")

    elif effect_type == "enrage":
        current_enemy["attack"] += trigger["attack_boost"]
        print(f"{current_enemy['name']} menjadi lebih kuat (attack +{trigger['attack_boost']}).")

    elif effect_type == "self_heal":
        heal = trigger["heal_amount"]
        current_enemy["hp"] = min(current_enemy["hp"] + heal, current_enemy["max_hp"])
        print(f"{current_enemy['name']} memulihkan HP sebesar {heal}.")

    elif effect_type == "enrage_poison":
        current_enemy["attack"] += trigger["attack_boost"]
        triggered_flag["poison_turns_left"] = trigger["poison_turns"]
        triggered_flag["poison_damage"] = trigger["poison_damage"]
        print(f"{current_enemy['name']} menjadi lebih kuat (attack +{trigger['attack_boost']}) dan meracunimu!")

    triggered_flag["active"] = True
    return triggered_flag

def apply_poison(triggered_flag):
    # efek khusus dmg over time 
    if triggered_flag.get("poison_turns_left", 0) > 0:
        dmg = triggered_flag["poison_damage"]
        player.player["hp"] -= dmg
        triggered_flag["poison_turns_left"] -= 1
        print(f"Racun mengalir di tubuhmu! -{dmg} HP ({triggered_flag['poison_turns_left']} giliran tersisa).")

def enemy_attack(current_enemy):
    # serangan balik enemy standar, dipakai berulang di beberapa cabang choice
    if is_miss(player.player["dodge"]):
        print(f"Kamu menghindar dari serangan {current_enemy['name']}!")
    else:
        damage = calculate_damage(current_enemy)
        player.player["hp"] -= damage
        print(f"{current_enemy['name']} menyerang balik sebesar {damage} damage!")

def battle(): # buat musuh random
    if random.randint(1, 100) <= 50:
        current_enemy = random.choice(enemy.boss_pool).copy()
        print(f"\nBOSS MUNCUL!")
    else:
        current_enemy = random.choice(enemy.enemy_pool).copy()

    current_enemy["max_hp"] = current_enemy["hp"]  # simpan HP awal ( acuan yang di pakai persen)
    triggered_flag = {"active": False, "poison_turns_left": 0, "poison_damage": 0}

    print(f"Sebuah {current_enemy['name']} muncul!")

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
                triggered_flag = check_low_hp_trigger(current_enemy, triggered_flag)

            if current_enemy["hp"] > 0:
                enemy_attack(current_enemy)

        elif choice == "2":
            inventory.use_potion()  # kita membuat Enemy tetap dapat menyerang setelah memakai potion
            if current_enemy["hp"] > 0:
                enemy_attack(current_enemy)

        elif choice == "3":
            print("Kamu kabur!")
            break
        else:
            print("Pilihan tidak valid.")
            continue

        if player.player["hp"] > 0:
            apply_poison(triggered_flag)

    if current_enemy["hp"] <= 0:
        print(f"\n{current_enemy['name']} kalah!")
        roll_drops(current_enemy)

    if player.player["hp"] <= 0:
        print("\nKamu kalah...")
