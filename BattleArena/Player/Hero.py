from Player.Weapon import Weapon
import random

class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.max_health_points = health_points
        self.is_weapon_equiped = False
        self.weapon: Weapon = None
        self.defense=1
    
    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equiped:
            self.attack_damage += self.weapon.attack_increas
            self.is_weapon_equiped = True
    
    def attack(self,damage):
        print(f'Hero attacks for {damage if damage >=0 else "0"} damage using his {self.weapon.weapon_type if self.is_weapon_equiped else "bare fists"}.')

    def special_attack(self):
            did_special_attack_work = random.random() < 0.4
            if(self.health_points < self.max_health_points -1 ):
                if(did_special_attack_work):
                    self.health_points += 1
                    print('Hero feels a second wind of life and heals')
            else:
                if(did_special_attack_work):
                    self.attack_damage +=1 
                    print('Hero feels totally healthy and gets more attack')
    
    def get_type_of_enemy(self):
        return 'Hero'
    
    def talk(self):
        print(f'I am a Hero and i will defeat you!!!')