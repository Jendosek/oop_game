from characters import Warrior, Mage, Archer, Healer, Assassin
from monsters import Goblin, Orc, Skeleton, Troll, Dragon
import random

class HeroFactory:
    heroes = {
        "warrior": {"class": Warrior, "hp": 120, "damage": 20},
        "mage": {"class": Mage, "hp": 80, "damage": 25},
        "archer": {"class": Archer, "hp": 90, "damage": 18},
        "healer": {"class": Healer, "hp": 100, "damage": 12},
        "assassin": {"class": Assassin, "hp": 85, "damage": 22},
    }

    def create(self, hero_type, name):
        if hero_type in self.heroes:
            data = self.heroes[hero_type]
            return data["class"](name, data["hp"], data["damage"])
        return None

    def get_types(self):
        return list(self.heroes.keys())

class MonsterFactory:
    monsters = {
        "goblin": {"class": Goblin, "hp": 50, "damage": 8, "gold": 10, "exp": 20},
        "orc": {"class": Orc, "hp": 80, "damage": 12, "gold": 20, "exp": 40},
        "skeleton": {"class": Skeleton, "hp": 60, "damage": 10, "gold": 15, "exp": 30},
        "troll": {"class": Troll, "hp": 100, "damage": 14, "gold": 30, "exp": 50},
        "dragon": {"class": Dragon, "hp": 150, "damage": 20, "gold": 50, "exp": 100},
    }

    def create(self, monster_type):
        if monster_type in self.monsters:
            data = self.monsters[monster_type]
            return data["class"](data["class"].__name__, data["hp"], data["damage"], data["gold"], data["exp"])
        return None

    def create_random(self):
        monster_type = random.choice(list(self.monsters.keys()))
        return self.create(monster_type)

    def get_types(self):
        return list(self.monsters.keys())