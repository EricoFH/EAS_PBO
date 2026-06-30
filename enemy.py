goblin = {
    "name": "Goblin",
    "hp": 15,
    "attack": 3,
    "gold": 5,
    "dodge": 25,
    "drops": [
        {"item": "Goblin Ear", "type": "material", "chance": 80},
        {"item": "Potion", "type": "consumable", "chance": 35},
    ],
    "low_hp_trigger": {
        "threshold": 30,        # efek yang kita kasih persen HP
        "type": "panic",        # efek yang kita kasih dodge turun drastis
        "dodge_penalty": 15,
        "message": "Goblin panik dan mulai gemetar ketakutan!"
    }
}

skeleton = {
    "name": "Skeleton",
    "hp": 25,
    "attack": 7,
    "gold": 5,
    "dodge": 10,
    "drops": [
        {"item": "Bone Fragment", "type": "material", "chance": 80},
        {"item": "Potion", "type": "consumable", "chance": 40},
    ],
    "low_hp_trigger": {
        "threshold": 30,
        "type": "enrage",       # buff efek attack naik
        "attack_boost": 4,
        "message": "Skeleton mengamuk, tulangnya berderak hebat!"
    }
}

minotaur = {
    "name": "Minotaur",
    "hp": 35,
    "attack": 12,
    "gold": 10,
    "dodge": 5,
    "drops": [
        {"item": "Minotaur Horn", "type": "material", "chance": 70},
        {"item": "Potion", "type": "consumable", "chance": 50},
    ],
    "low_hp_trigger": {
        "threshold": 25,
        "type": "self_heal",    # efek heal sekali pakai
        "heal_amount": 10,
        "message": "Minotaur meraung dan memulihkan sebagian lukanya!"
    }
}

naga = {
    "name": "Crimson Dragon",
    "hp": 100,
    "attack": 15,
    "gold": 50,
    "dodge": 20,
    "drops": [
        {"item": "Red Horn", "type": "material", "chance": 70},
        {"item": "Potion", "type": "consumable", "chance": 100},
    ],
    "low_hp_trigger": {
        "threshold": 20,
        "type": "enrage_poison",  # buff khusus attack naik + poison ke player
        "attack_boost": 6,
        "poison_damage": 4,
        "poison_turns": 3,
        "message": "Crimson Dragon mengamuk dan menyemburkan racun mematikan!"
    }
}
enemy_pool = [goblin, skeleton, minotaur]
boss_pool = [naga]
