from factory import HeroFactory, MonsterFactory
from items import Shop
from events import EventLog
from battle import BattleSystem
from quest import create_quests

hero_factory = HeroFactory()
monster_factory = MonsterFactory()
shop = Shop()
event_log = EventLog()
event_log.add_listener(print)
battle_system = BattleSystem()

heroes = []
quests = create_quests()

while True:
    print("\nГільдія мисливців")
    print("1. Створити героя")
    print("2. Показати героїв")
    print("3. Магазин")
    print("4. Купити предмет")
    print("5. Показати завдання")
    print("6. Відправити героя на завдання")
    print("7. Тренувальний бій")
    print("8. Журнал подій")
    print("9. Відпочинок героя")
    print("0. Вихід")

    choice = input("Вибери: ")

    if choice == "1":
        name = input("Ім'я героя: ")
        if not name.strip():
            print("Ім'я не може бути порожнім.")
            continue
        print("Класи:", ", ".join(hero_factory.get_types()))
        hero_type = input("Клас: ").lower()
        hero = hero_factory.create(hero_type, name)
        if hero:
            heroes.append(hero)
            print(f"{name} ({hero_type}) створений!")
        else:
            print("Невірний клас.")

    elif choice == "2":
        if not heroes:
            print("Героїв немає.")
        else:
            for index, hero in enumerate(heroes):
                status = "живий" if hero.is_alive() else "мертвий"
                print(f"  {index + 1}. {hero.show_info()} | {status}")

    elif choice == "3":
        print("\n--- Магазин ---")
        shop.show_items()

    elif choice == "4":
        if not heroes:
            print("Спочатку створіть героя.")
            continue
        for index, hero in enumerate(heroes):
            print(f"  {index + 1}. {hero.show_info()}")
        try:
            hero_num = int(input("Номер героя: ")) - 1
            if 0 <= hero_num < len(heroes):
                shop.show_items()
                item_num = int(input("Номер предмета: ")) - 1
                result = shop.buy(heroes[hero_num], item_num)
                print(result)
            else:
                print("Невірний номер.")
        except ValueError:
            print("Введіть число.")

    elif choice == "5":
        print("\n--- Завдання ---")
        for index, quest in enumerate(quests):
            print(f"  {index + 1}. {quest.show_info()}")

    elif choice == "6":
        if not heroes:
            print("Спочатку створіть героя.")
            continue
        alive_heroes = [hero for hero in heroes if hero.is_alive()]
        if not alive_heroes:
            print("Немає живих героїв.")
            continue
        for index, hero in enumerate(alive_heroes):
            print(f"  {index + 1}. {hero.show_info()}")
        try:
            hero_num = int(input("Номер героя: ")) - 1
            if 0 <= hero_num < len(alive_heroes):
                available = [quest for quest in quests if quest.get_status() == "available"]
                if not available:
                    print("Немає доступних завдань.")
                    continue
                for index, quest in enumerate(available):
                    print(f"  {index + 1}. {quest.show_info()}")
                quest_num = int(input("Номер завдання: ")) - 1
                if 0 <= quest_num < len(available):
                    available[quest_num].start(alive_heroes[hero_num])
                else:
                    print("Невірний номер.")
            else:
                print("Невірний номер.")
        except ValueError:
            print("Введіть число.")

    elif choice == "7":
        if not heroes:
            print("Спочатку створіть героя.")
            continue
        alive_heroes = [hero for hero in heroes if hero.is_alive()]
        if not alive_heroes:
            print("Немає живих героїв.")
            continue
        for index, hero in enumerate(alive_heroes):
            print(f"  {index + 1}. {hero.show_info()}")
        try:
            hero_num = int(input("Номер героя: ")) - 1
            if 0 <= hero_num < len(alive_heroes):
                print("Монстри:", ", ".join(monster_factory.get_types()))
                monster_type = input("Тип монстра: ").lower()
                monster = monster_factory.create(monster_type)
                if monster:
                    battle_system.start_battle(alive_heroes[hero_num], monster)
                else:
                    print("Невірний тип монстра.")
            else:
                print("Невірний номер.")
        except ValueError:
            print("Введіть число.")

    elif choice == "8":
        print("\n--- Журнал подій ---")
        event_log.show_log()

    elif choice == "9":
        if not heroes:
            print("Спочатку створіть героя.")
            continue
        for index, hero in enumerate(heroes):
            print(f"  {index + 1}. {hero.show_info()}")
        try:
            hero_num = int(input("Номер героя: ")) - 1
            if 0 <= hero_num < len(heroes):
                heroes[hero_num].heal(50)
                print(f"{heroes[hero_num].get_name()} відпочив. HP: {heroes[hero_num].get_hp()}")
            else:
                print("Невірний номер.")
        except ValueError:
            print("Введіть число.")

    elif choice == "0":
        print("Бувай!")
        break
    else:
        print("Невірний вибір.")