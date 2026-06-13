inventory = {
    "Potion": {"type": "consumable", "qty": 2},
}

def show_inventory():
    print("\n=== INVENTORY ===")
    if len(inventory) == 0:
        print("Inventory kosong.")
    else:
        for item, data in inventory.items():
            print(f"- {item} x{data['qty']}")

def add_item(item, item_type="material"):
    if item in inventory:
        inventory[item]["qty"] += 1
    else:
        inventory[item] = {"type": item_type, "qty": 1}
    print(f"{item} ditambahkan ke inventory.")

def use_potion():
    if "Potion" not in inventory or inventory["Potion"]["qty"] <= 0:
        print("Kamu tidak punya Potion!")
        return False
    
    import player
    heal = 30
    player.player["hp"] += heal
    inventory["Potion"]["qty"] -= 1

    if inventory["Potion"]["qty"] == 0:
        del inventory["Potion"]

    print(f"Kamu minum Potion! HP pulih sebesar {heal}.")
    return True