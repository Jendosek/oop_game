from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price

    @abstractmethod
    def apply(self, character):
        pass

    @abstractmethod
    def show_info(self):
        pass

class Weapon(Item):
    def __init__(self, name, price, bonus_damage):
        super().__init__(name, price)
        self.__bonus_damage = bonus_damage

    def apply(self, character):
        character.set_damage(character.get_damage() + self.__bonus_damage)

    def show_info(self):
        return f"{self.get_name()} | +{self.__bonus_damage} урону | {self.get_price()} золота"

class Armor(Item):
    def __init__(self, name, price, bonus_hp):
        super().__init__(name, price)
        self.__bonus_hp = bonus_hp

    def apply(self, character):
        character.set_hp(character.get_hp() + self.__bonus_hp)

    def show_info(self):
        return f"{self.get_name()} | +{self.__bonus_hp} HP | {self.get_price()} золота"

class Potion(Item):
    def __init__(self, name, price, heal_amount):
        super().__init__(name, price)
        self.__heal_amount = heal_amount

    def apply(self, character):
        character.heal(self.__heal_amount)

    def show_info(self):
        return f"{self.get_name()} | +{self.__heal_amount} лікування | {self.get_price()} золота"

class Shop:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__items = [
                Weapon("Іржавий меч", 20, 5),
                Weapon("Сталевий меч", 50, 10),
                Weapon("Легендарний меч", 100, 20),
                Armor("Шкіряна броня", 25, 15),
                Armor("Залізна броня", 60, 30),
                Armor("Діамантова броня", 120, 50),
                Potion("Мале зілля", 10, 20),
                Potion("Велике зілля", 30, 50),
            ]
        return cls._instance

    def show_items(self):
        for index, item in enumerate(self.__items):
            print(f"  {index + 1}. {item.show_info()}")

    def buy(self, character, item_num):
        if 0 <= item_num < len(self.__items):
            item = self.__items[item_num]
            if character.spend_gold(item.get_price()):
                character.equip_item(item)
                return f"{character.get_name()} купив {item.get_name()}"
            return "Не вистачає золота!"
        return "Невірний номер предмета."