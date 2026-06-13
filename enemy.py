goblin = {
    "name": "Goblin",
    "hp": 15,
    "attack": 3,
    "gold": 5,
    "dodge": 25,
    "drops": [
        {"item": "Goblin Ear", "type": "material", "chance": 80},
        {"item": "Potion", "type": "consumable", "chance": 35},
    ]
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
    ]
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
    ]
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
    ]
}
enemy_pool = [goblin, skeleton, minotaur]
boss_pool = [naga]