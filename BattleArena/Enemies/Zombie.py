from Enemy import  *
import random

class Zombie(Enemy):
    
    def __init__(self, health_points=10, attack_damage=1, defense=1):
        super().__init__('Zombie', health_points, attack_damage, defense)

    def talk(self):
        print('Zombie *Grumbles*')

    def spread_disease(self):
        print(f'Zombie is trying to spread infection.')

    def special_attack(self):
        did_special_attack_work = random.random() > 0.5
        if(did_special_attack_work):
            if(self.health_points > self.max_health_points-2):
                self.health_points=self.max_health_points
            else:
                self.health_points += 3
            print('Zombie used special attack and regenerated 3HP!.')