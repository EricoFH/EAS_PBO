import player
import inventory

def toko():
    while True:
        print("\n=== TOKO ===")
        print(f"Gold: {player.player['gold']}")
        print("1. Upgrade max HP   + 20   (50 gold)")
        print("2. Upgrade ATK      + 3    (20 gold)")
        print("3. Potion           + 1    (10 gold)")
        print("4. Jual")
        print('5. Keluar')

        choice = input("> ")

        if choice == "1":
            if player.player["gold"] >= 50:
                player.player["max_hp"] += 20
                player.player["hp"] = player.player["max_hp"]
                player.player["gold"] -= 50
                print("Max HP +20 !")
            else:
                print("Gold tidak cukup")

        elif choice == "2":
            if player.player["gold"] >= 20:
                player.player["attack"] += 3
                player.player["gold"] -= 20
                print("ATK +3 !")
            else:
                print("Gold tidak cukup")

        elif choice == "3":
            if player.player["gold"] >= 10:
                inventory.add_item("Potion", "consumable")
                player.player["gold"] -=10
                print("Potion +1 !")
            else:
                print("Gold tidak cukup")

        elif choice == "4":
            jual()
        
        elif choice == "5":
            break

        else:
            ("Tidak valid")

harga_jual = {
    "Goblin Ear": 5,
    "Bone Fragment": 8,
    "Minotaur Horn": 15,
    "Red Horn": 30,
}

def jual():
    if len(inventory.inventory) == 0:
        print("Inventory kosong.")
        return

    print("\n=== JUAL ITEM ===")
    
    bisa_dijual = {
        item: data for item, data in inventory.inventory.items()
        if data["type"] == "material" and item in harga_jual
    }

    if len(bisa_dijual) == 0:
        print("Tidak ada item yang bisa dijual.")
        return

    for i, (item, data) in enumerate(bisa_dijual.items(), 1):
        print(f"{i}. {item} x{data['qty']} ({harga_jual[item]} gold/item)")

    print("0. Batal")
    choice = input("> ")

    if choice == "0":
        return

    try:
        idx = int(choice) - 1
        item_name = list(bisa_dijual.keys())[idx]
        total = harga_jual[item_name] * inventory.inventory[item_name]["qty"]
        player.player["gold"] += total
        print(f"{item_name} terjual! Gold +{total}")
        del inventory.inventory[item_name]
    except (ValueError, IndexError):
        print("Pilihan tidak valid.")
