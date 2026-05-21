from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp, damage):
        self._name = name
        self._hp = hp
        self._max_hp = hp
        self._damage = damage
        self._level = 1
        self._exp = 0
        self._gold = 0
        self._equipment = []

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        if hp < 0:
            hp = 0
        if hp > self._max_hp:
            hp = self._max_hp
        self._hp = hp

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = damage

    def get_level(self):
        return self._level

    def get_exp(self):
        return self._exp

    def get_gold(self):
        return self._gold

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)

    def heal(self, amount):
        self.set_hp(self.get_hp() + amount)

    def is_alive(self):
        return self.get_hp() > 0

    def add_exp(self, amount):
        self._exp += amount
        if self._exp >= self._level * 100:
            self._exp = 0
            self._level += 1
            self._max_hp += 10
            self._damage += 3
            self.set_hp(self._max_hp)
            print(f"{self._name} підвищив рівень до {self._level}!")

    def add_gold(self, amount):
        self._gold += amount

    def spend_gold(self, amount):
        if self._gold >= amount:
            self._gold -= amount
            return True
        print("Не вистачає золота!")
        return False

    def equip_item(self, item):
        self._equipment.append(item)
        item.apply(self)
        print(f"{self._name} екіпірував {item.get_name()}")

    def show_info(self):
        return f"{self._name} | HP: {self._hp}/{self._max_hp} | DMG: {self._damage} | LVL: {self._level} | EXP: {self._exp} | Gold: {self._gold}"

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def special_ability(self, target):
        pass


class Warrior(Character):
    def attack(self, target):
        damage = int(self.get_damage() * 1.5)
        target.take_damage(damage)
        return f"{self.get_name()} б'є мечем {target.get_name()} на {damage} урону"

    def special_ability(self, target):
        damage = int(self.get_damage() * 2.5)
        target.take_damage(damage)
        return f"{self.get_name()} використовує Потужний удар на {target.get_name()} на {damage} урону!"

class Mage(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.__mana = 100

    def attack(self, target):
        if self.__mana >= 10:
            self.__mana -= 10
            damage = int(self.get_damage() * 1.2)
            target.take_damage(damage)
            return f"{self.get_name()} кастує магію на {target.get_name()} на {damage} урону. Мана: {self.__mana}"
        else:
            damage = int(self.get_damage() * 0.4)
            target.take_damage(damage)
            return f"{self.get_name()} б'є посохом {target.get_name()} на {damage} урону. Мана закінчилась!"

    def special_ability(self, target):
        if self.__mana >= 30:
            self.__mana -= 30
            damage = int(self.get_damage() * 2)
            target.take_damage(damage)
            return f"{self.get_name()} використовує Вогняну кулю на {target.get_name()} на {damage} урону!"
        return f"{self.get_name()} не вистачає мани!"

class Archer(Character):
    def attack(self, target):
        import random
        if random.random() < 0.3:
            damage = int(self.get_damage() * 2)
            target.take_damage(damage)
            return f"{self.get_name()} наносить КРИТ по {target.get_name()} на {damage} урону!"
        damage = int(self.get_damage() * 1.2)
        target.take_damage(damage)
        return f"{self.get_name()} стріляє в {target.get_name()} на {damage} урону"

    def special_ability(self, target):
        import random
        damage = int(self.get_damage() * 1.5)
        for i in range(3):
            target.take_damage(damage)
        return f"{self.get_name()} випускає 3 стріли в {target.get_name()} по {damage} урону кожна!"

class Healer(Character):
    def attack(self, target):
        damage = int(self.get_damage() * 0.8)
        target.take_damage(damage)
        return f"{self.get_name()} б'є {target.get_name()} на {damage} урону"

    def special_ability(self, target=None):
        heal_amount = 40
        self.heal(heal_amount)
        return f"{self.get_name()} лікує себе на {heal_amount} HP!"

class Assassin(Character):
    def attack(self, target):
        damage = int(self.get_damage() * 1.3)
        target.take_damage(damage)
        return f"{self.get_name()} наносить удар з тіні по {target.get_name()} на {damage} урону"

    def special_ability(self, target):
        import random
        if random.random() < 0.5:
            damage = int(self.get_damage() * 3)
            target.take_damage(damage)
            return f"{self.get_name()} наносить смертельний удар по {target.get_name()} на {damage} урону!"
        damage = int(self.get_damage() * 0.5)
        target.take_damage(damage)
        return f"{self.get_name()} промахнувся! Завдає лише {damage} урону"