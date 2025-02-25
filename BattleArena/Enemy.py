class Enemy:

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1, defense = 1):
        self.__type_of_enemy=type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.max_health_points = health_points
        self.defense = defense
        self.default_defense = defense
        self.default_attack = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f' I am a {self.__type_of_enemy}. Be prepared to fight')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self, damage):
        print(f'{self.__type_of_enemy} attacks for {damage if damage >= 0 else "0"}.')

    def special_attack(self):
        print('Enemy has no special attack.')