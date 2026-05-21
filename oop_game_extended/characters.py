from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp, damage):
        self.__name = name
        self.__hp = hp
        self.__max_hp = hp
        self.__damage = damage
        self.__level = 1
        self.__exp = 0
        self.__gold = 0
        self.__equipment = []

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

        def set_damage(self, damage):
            self.__damage = damage

        def get_level(self):
            return self.__level

        def get_exp(self):
            return self.__exp

        def get_gold(self):
            return self.__gold

        def take_damage(self, damage):
            self.set_hp(self.get_hp() - damage)

        def heal(self, amount):
            self.set_hp(self.get_hp() + amount)

        def is_alive(self):
            return self.get_hp() > 0

        def add_exp(self, amount):
            self.__exp += amount
            if self.__exp >= self.__level * 100:
                self.__exp = 0
                self.__level += 1
                self.__max_hp += 10
                self.__damage += 3
                self.set_hp(self.__max_hp)
                print(f"{self.__name} підвищив рівень до {self.__level}!")

        def add_gold(self, amount):
            self.__gold += amount

        def spend_gold(self, amount):
            if self.__gold >= amount:
                self.__gold -= amount
                return True
            print("Не вистачає золота!")
            return False

        def equip_item(self, item):
            self.__equipment.append(item)
            item.apply(self)
            print(f"{self.__name} екіпірував {item.get_name()}")

        def show_info(self):
            return f"{self.__name} | HP: {self.__hp}/{self.__max_hp} | DMG: {self.__damage} | LVL: {self.__level} | EXP: {self.__exp} | Gold: {self.__gold}"

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