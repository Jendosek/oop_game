from events import EventLog

class BattleSystem:
    def __init__(self):
        self.__log = EventLog()

    def start_battle(self, hero, monster):
        self.__log.log(f"\n=== Бій: {hero.get_name()} vs {monster.get_name()} ===")
        round_num = 1

        while hero.is_alive() and monster.is_alive():
            self.__log.log(f"\n--- Раунд {round_num} ---")
            self.__hero_turn(hero, monster)
            if monster.is_alive():
                self.__monster_turn(hero, monster)
            self.__show_status(hero, monster)
            round_num += 1

        self.__end_battle(hero, monster)

    def __hero_turn(self, hero, monster):
        result = hero.attack(monster)
        self.__log.log(result)

    def __monster_turn(self, hero, monster):
        result = monster.attack(hero)
        self.__log.log(result)

    def __show_status(self, hero, monster):
        self.__log.log(f"  {hero.get_name()}: {hero.get_hp()} HP")
        self.__log.log(f"  {monster.get_name()}: {monster.get_hp()} HP")

    def __end_battle(self, hero, monster):
        if hero.is_alive():
            gold = monster.get_gold_reward()
            exp = monster.get_exp_reward()
            hero.add_gold(gold)
            hero.add_exp(exp)
            self.__log.log(f"\n{hero.get_name()} переміг!")
            self.__log.log(f"  Отримано: {gold} золота, {exp} досвіду")
        else:
            self.__log.log(f"\n{hero.get_name()} програв...")