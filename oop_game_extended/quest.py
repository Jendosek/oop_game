from factory import MonsterFactory
from battle import BattleSystem
import random

class Quest:
    def __init__(self, name, difficulty, gold_reward, exp_reward, monster_types):
        self.__name = name
        self.__difficulty = difficulty
        self.__gold_reward = gold_reward
        self.__exp_reward = exp_reward
        self.__monster_types = monster_types
        self.__status = "available"

    def get_name(self):
        return self.__name
    def get_status(self):
        return self.__status
    def get_difficulty(self):
        return self.__difficulty

    def show_info(self):
        return f"{self.__name} | Складність: {self.__difficulty} | Gold: {self.__gold_reward} | EXP: {self.__exp_reward} | Статус: {self.__status}"

    def start(self, hero):
        if self.__status == "completed":
            print("Це завдання вже виконане.")
            return

        if not hero.is_alive():
            print(f"{hero.get_name()} мертвий і не може йти на завдання.")
            return

        monster_factory = MonsterFactory()
        monster_type = random.choice(self.__monster_types)
        monster = monster_factory.create(monster_type)

        print(f"\n{hero.get_name()} вирушає на завдання: {self.__name}")
        print(f"На шляху зустрічається {monster.get_name()}!")

        battle = BattleSystem()
        battle.start_battle(hero, monster)

        if hero.is_alive():
            hero.add_gold(self.__gold_reward)
            hero.add_exp(self.__exp_reward)
            self.__status = "completed"
            print(f"Завдання виконане! Нагорода: {self.__gold_reward} золота, {self.__exp_reward} досвіду")
        else:
            self.__status = "failed"
            print(f"Завдання провалене...")


def create_quests():
    return [
        Quest("Гобліни в лісі", 1, 15, 25, ["goblin"]),
        Quest("Зачистка підземелля", 2, 30, 50, ["skeleton", "goblin"]),
        Quest("Орки біля села", 3, 50, 80, ["orc", "skeleton"]),
        Quest("Печера тролля", 4, 80, 120, ["troll", "orc"]),
        Quest("Лігво дракона", 5, 150, 200, ["dragon"]),
    ]