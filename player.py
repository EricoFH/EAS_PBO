player = {
    "name": "Supri",
    "hp": 30,
    "max_hp" : 30,
    "attack": 5,
    "gold": 10,
    "dodge" : 30
}

def show_status():
    print("\n=== STATUS PLAYER ===")
    print(f"Nama   : {player['name']}")
    print(f"HP     : {player['hp']}")
    print(f"Attack : {player['attack']}")
    print(f"Gold   : {player['gold']}")