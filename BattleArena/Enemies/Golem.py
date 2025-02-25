from Enemy import *
import random

class Golem(Enemy):

    def __init__(self, health_points=10, attack_damage=1, defense=2):
        super().__init__("Golem", health_points, attack_damage, defense)

    def talk(self):
        print(f'Golem cracks!!.')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if(did_special_attack_work):
            self.attack_damage += 1
            self.defense += 1
            print('Golem used special attack def and attack increased!.')