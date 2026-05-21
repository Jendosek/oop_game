from abc import ABC, abstractmethod
import random

class Monster(ABC):
    def __init__(self, name, hp, damage, gold_reward, exp_reward):
        self.__name = name
        self.__hp = hp
        self.__max_hp = hp
        self.__damage = damage
        self.__gold_reward = gold_reward
        self.__exp_reward = exp_reward

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        if hp < 0:
            hp = 0
        if hp > self.__max_hp:
            hp = self.__max_hp
        self.__hp = hp

    def get_damage(self):
        return self.__damage

    def get_gold_reward(self):
        return self.__gold_reward

    def get_exp_reward(self):
        return self.__exp_reward

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)

    def is_alive(self):
        return self.get_hp() > 0

    def show_info(self):
        return f"{self.__name} | HP: {self.__hp}/{self.__max_hp} | DMG: {self.__damage} | Gold: {self.__gold_reward} | EXP: {self.__exp_reward}"

    @abstractmethod
    def attack(self, target):
        pass

class Goblin(Monster):
    def attack(self, target):
        damage = self.get_damage()
        target.take_damage(damage)
        return f"Гоблін кусає {target.get_name()} на {damage} урону"

class Orc(Monster):
    def attack(self, target):
        damage = int(self.get_damage() * 1.5)
        target.take_damage(damage)
        return f"Орк б'є булавою {target.get_name()} на {damage} урону"

class Troll(Monster):
    def attack(self, target):
        damage = int(self.get_damage() * 1.3)
        target.take_damage(damage)
        heal = 5
        self.set_hp(self.get_hp() + heal)
        return f"Тролль б'є {target.get_name()} на {damage} урону і регенерує {heal} HP"

class Skeleton(Monster):
    def take_damage(self, damage):
        reduced = int(damage * 0.7)
        super().take_damage(reduced)
        return f"Скелет поглинає частину урону! Отримав {reduced} замість {damage}"

    def attack(self, target):
        damage = self.get_damage()
        target.take_damage(damage)
        return f"Скелет б'є {target.get_name()} на {damage} урону"

class Dragon(Monster):
    def attack(self, target):
        if random.random() < 0.4:
            damage = int(self.get_damage() * 2)
            target.take_damage(damage)
            return f"Дракон дихає ВОГНЕМ на {target.get_name()} на {damage} урону!"
        damage = int(self.get_damage() * 1.2)
        target.take_damage(damage)
        return f"Дракон б'є хвостом {target.get_name()} на {damage} урону"