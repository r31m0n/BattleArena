
from Enemy import *
from Player.Hero import Hero
import random

def battle(e1: Enemy, e2: Enemy):
    turn = 1
    print('***************************************************')
    print('\n')
    e1.talk()
    e2.talk()
    print('\n')

    while e1.health_points > 0 and e2.health_points > 0 :
        print('***************************************************')
        print(f' ------Turn {turn}------')
        if random.randint(1,2) == 1 :
            attack(e1,e2,e1,e2)
            print('\n')
        else:
            attack(e2,e1,e1,e2)
            print('\n')
        turn +=1
    print('***************************************************')
    
    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')
    print('***************************************************')
    e1.health_points = e1.max_health_points
    e1.defense = e1.default_defense
    e1.attack_damage = e1.default_attack
    e2.health_points = e2.max_health_points
    e2.defense = e2.default_defense
    e2.attack_damage = e2.default_attack

def hero_battle(hero:Hero, enemy:Enemy):
        turn = 1
        print('***************************************************')
        print('\n')
        hero.talk()
        enemy.talk()
        print('\n')

        while hero.health_points > 0 and enemy.health_points > 0 :
            print('***************************************************')
            print(f' ------Turn {turn}------')
            if random.randint(1,2) == 1 :
                attack(hero,enemy,hero,enemy)
                print('\n')
            else:
                attack(enemy,hero,hero,enemy)
                print('\n')
            turn +=1
        print('***************************************************')
        
        if hero.health_points > 0:
            print(f'Hero wins!')
        else:
            print(f'{enemy.get_type_of_enemy()} wins!')
        print('***************************************************')
        hero.health_points = hero.max_health_points
        enemy.health_points = enemy.max_health_points
        enemy.defense = enemy.default_defense
        enemy.attack_damage = enemy.default_attack


def attack(attacker: Enemy, defender: Enemy, e1:Enemy, e2:Enemy):
    print('\n')
    attacker.special_attack()
    attacker_damage = 0 
    if(attacker.get_type_of_enemy()=='Zombie'):
        attacker_damage = attacker.attack_damage - defender.defense
    else:
        attacker_damage = (random.randint(1,attacker.attack_damage) - defender.defense)
    if(attacker_damage>=0):
        defender.health_points -= attacker_damage
    attacker.attack(attacker_damage)
    if defender.health_points <= 0 :
        print('---------------------------------------------------')
        print(f'{e1.get_type_of_enemy()} has {e1.health_points} hp left || {e2.get_type_of_enemy()} has {e2.health_points} hp left ')
        return
    defender.special_attack()
    defender_damage = 0 
    if(defender.get_type_of_enemy()=='Zombie'):
        defender_damage = defender.attack_damage - attacker.defense
    else:
        defender_damage = (random.randint(1,defender.attack_damage) - attacker.defense)
    if(defender_damage>=0):
        attacker.health_points -= defender_damage
    defender.attack(defender_damage)
    print('---------------------------------------------------')
    print(f'{e1.get_type_of_enemy()} has {e1.health_points} hp left || {e2.get_type_of_enemy()} has {e2.health_points} hp left ')