import player
import inventory
import combat
import toko

def main_menu():

    while True:

        print("\nTEXT RPG")
        print("1. Status")
        print("2. Inventory")
        print("3. Battle")
        print("4. Toko")
        print("5. Keluar")

        choice = input("> ")

        if choice == "1":
            player.show_status()

        elif choice == "2":
            inventory.show_inventory()

        elif choice == "3":
            combat.battle()

            if player.player["hp"] <= 0:
                break
            
        elif choice == "4":
            toko.toko()

        elif choice == "5":
            print("Game selesai.")
            break

        else:
            print("Pilihan tidak valid.")

main_menu()
