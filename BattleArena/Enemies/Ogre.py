from Enemy import *
import random

class Ogre(Enemy):

    def __init__(self, health_points=10, attack_damage=1, defense=1):
        super().__init__("Ogre", health_points, attack_damage, defense)

    def talk(self):
        print(f'Ogre Slam hands into the ground.')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.3
        if(did_special_attack_work):
            self.attack_damage += 2
            print('Ogre used special attack and attack stat increased increased.')