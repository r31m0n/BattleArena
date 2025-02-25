from Enemy import *
import random

class Vampire(Enemy):

    def __init__(self, health_points=10, attack_damage=1, defense=1):
        super().__init__("Vampire", health_points, attack_damage, defense)

    def talk(self):
        print(f'{self.get_type_of_enemy()} Flashes his teeth.')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.4
        if(did_special_attack_work):
            self.attack_damage += 1
            if(self.health_points < self.max_health_points -1):
                self.health_points += 1
            print('Vampire uses special attack and deals extra damage and heals.')