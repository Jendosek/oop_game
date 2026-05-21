from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name, hp, damage, level):
        self.__name = name
        self.__hp = hp
        self.__damage = damage
        self.__level = level

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_hp(self):
         return self.__hp
    def set_hp(self, hp):
        if hp >= 0:
            self.__hp = hp

    def get_damage(self):
        return self.__damage
    def set_damage(self, damage):
        self.__damage = damage

    def get_level(self):
        return self.__level
    def set_level(self, level):
        self.__level = level

    def show_info(self):
        return f"Name: {self.__name}, HP: {self.__hp}, Damage: {self.__damage}, Level: {self.__level}"

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, damage):
        new_hp = self.get_hp() - damage
        if new_hp <= 0:
            new_hp = 0
        self.set_hp(new_hp)

    def heal(self, heal_hp):
        self.set_hp(self.get_hp() + heal_hp)

    def is_alive(self):
        if self.get_hp() > 0:
            return True
        else:
            return False

    def level_up(self):
        self.set_level(self.get_level() + 1)
        self.set_damage(self.get_damage() + 3)
        print(f"{self.get_name()} підвищив рівень до {self.get_level()}! Урон: {self.get_damage()}")


class Warrior(Character):
    def attack(self, target):
        damage = int(self.get_damage() * 1.5)
        target.take_damage(damage)
        print(f"{self.get_name()} наносить сильний удар по {target.get_name()} і завдає {damage} урону.")

class Mage(Character):
    def attack(self, target):
        damage = int(self.get_damage() * 0.9)
        target.take_damage(damage)
        print(f"{self.get_name()} наносить магічний удар по {target.get_name()} і завдає {damage} урону.")

    def heal(self, heal_hp):
        super().heal(heal_hp)
        print(f"{self.get_name()} використовує магію для лікування і відновлює {heal_hp} HP.")

class Archer(Character):
    def attack(self, target):
        if random.random() < 0.3:
            damage = int(self.get_damage() * 2)
            target.take_damage(damage)
            print(f"{self.get_name()} наносить КРИТИЧНИЙ удар по {target.get_name()} і завдає {damage} урону!")
        else:
            damage = int(self.get_damage() * 1.2)
            target.take_damage(damage)
            print(f"{self.get_name()} наносить точний удар по {target.get_name()} і завдає {damage} урону.")


def battle(hero, enemy):
    print(f"\nБій: {hero.get_name()} vs {enemy.get_name()}")
    round_num = 1

    while hero.is_alive() and enemy.is_alive():
        print(f"\nРаунд {round_num}")
        hero.attack(enemy)
        if enemy.is_alive():
            enemy.attack(hero)
        print(f"  {hero.get_name()}: {hero.get_hp()} HP")
        print(f"  {enemy.get_name()}: {enemy.get_hp()} HP")
        round_num += 1

    if hero.is_alive():
        print(f"\n{hero.get_name()} переміг!")
        hero.level_up()
    else:
        print(f"\n{enemy.get_name()} переміг!")
        enemy.level_up()


characters = []

while True:
    print("\nАрена героїв")
    print("1. Створити персонажа")
    print("2. Показати всіх персонажів")
    print("3. Почати бій")
    print("4. Показати живих персонажів")
    print("5. Вилікувати персонажа")
    print("0. Вихід")

    choice = input("Вибери: ")

    if choice == "1":
        name = input("Ім'я: ")
        if not name.strip():
            print("Ім'я не може бути порожнім.")
            continue
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        class_choice = input("Клас: ")
        if class_choice == "1":
            characters.append(Warrior(name, 100, 20, 1))
        elif class_choice == "2":
            characters.append(Mage(name, 80, 25, 1))
        elif class_choice == "3":
            characters.append(Archer(name, 90, 18, 1))
        else:
            print("Невірний клас.")
            continue
        print(f"{name} створений!")

    elif choice == "2":
        if not characters:
            print("Персонажів немає.")
        else:
            for index, character in enumerate(characters):
                status = "живий" if character.is_alive() else "мертвий"
                print(f"  {index + 1}. {character.show_info()} ({status})")

    elif choice == "3":
        alive = []
        for character in characters:
            if character.is_alive():
                alive.append(character)
        if len(alive) < 2:
            print("Потрібно мінімум 2 живих персонажі.")
            continue
        print("\nЖиві персонажі:")
        for index, character in enumerate(alive):
            print(f"  {index + 1}. {character.show_info()}")
        try:
            hero_num = int(input("Номер героя: ")) - 1
            enemy_num = int(input("Номер ворога: ")) - 1
            if hero_num == enemy_num:
                print("Не можна битися з самим собою.")
            elif 0 <= hero_num < len(alive) and 0 <= enemy_num < len(alive):
                battle(alive[hero_num], alive[enemy_num])
            else:
                print("Невірний номер.")
        except ValueError:
            print("Введіть число.")

    elif choice == "4":
        alive = [character for character in characters if character.is_alive()]
        if not alive:
            print("Живих персонажів немає.")
        else:
            for index, character in enumerate(alive):
                print(f"  {index + 1}. {character.show_info()}")

    elif choice == "5":
        alive = [character for character in characters if character.is_alive()]
        if not alive:
            print("Немає кого лікувати.")
        else:
            for index, character in enumerate(alive):
                print(f"  {index + 1}. {character.show_info()}")
            try:
                heal_num = int(input("Кого лікувати: ")) - 1
                if 0 <= heal_num < len(alive):
                    alive[heal_num].heal(30)
                    print(f"{alive[heal_num].get_name()} HP: {alive[heal_num].get_hp()}")
                else:
                    print("Невірний номер.")
            except ValueError:
                print("Введіть число.")

    elif choice == "0":
        print("Бувай!")
        break
    else:
        print("Невірний вибір.")