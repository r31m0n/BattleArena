from Enemies.Zombie import Zombie
from Enemies.Ogre import Ogre
from Enemies.Vampire import Vampire
from Enemies.Golem import Golem
from Player.Hero import Hero
from Player.Weapon import Weapon
from Battle_functions.Battle_functions import *
import random

def hero_weapon_select_menu(weapon_list, hero):
        
        hero_weapon_select_menu_open = True
        while hero_weapon_select_menu_open:
            print("\nHero weapon select menu")
            print("1. Equip Dagger")
            print("2. Equip Sword")
            print("3. Equip Greatsword")
            print("4. Equip random gear")
            print("5 Go back")

            hero_equipment_option = input("Enter your choice: ")
            if hero_equipment_option == '1':
                hero.weapon=weapon_list[0]
                hero.equip_weapon()
                print('\n**Dagger equiped**')
            elif hero_equipment_option=='2':
                hero.weapon=weapon_list[1]
                hero.equip_weapon()
                print('\n**Sword equiped**')
            elif hero_equipment_option=='3':
                hero.weapon=weapon_list[2]
                hero.equip_weapon()
                print('\n**Greatsword equiped**')
            elif hero_equipment_option=='4':
                selected_weapon = random.sample(weapon_list,1)
                hero.weapon = selected_weapon[0]
                hero.equip_weapon()
                print(f'\n**{selected_weapon[0].weapon_type} equiped**')
            elif hero_equipment_option == '5':
                hero_weapon_select_menu_open = False
            else:
                print("Invalid option. Please try again.")

def select_enemy_menu(monsters, selected_enemy):

    select_enemy_menu_open = True

    print("\nselect enemy")

    while select_enemy_menu_open == True:
        for index, enemy in enumerate(monsters):
            print(f'{index+1}. Select {enemy.get_type_of_enemy()}')
            
        enemy_selection_option = input("Enter your choice: ")

        try:
            selected_index = int(enemy_selection_option)-1
            for index, enemy in enumerate(monsters):
                if selected_index >= 0 and selected_index < len(monsters):
                    if selected_index == index:
                        selected_enemy = enemy
                        print(f'\n***{selected_enemy.get_type_of_enemy()} selected to fight***')
                        select_enemy_menu_open = False
                else:
                    print(f'Invalid monster selection, select a number between 1 and {len(monsters)-1}')
        except ValueError:
            print('Invalid input! Please enter a valid number.')
    return selected_enemy


def hero_battle_select_enemy(hero, monsters):
    
    hero_select_enemy_menu_open = True
    selected_enemy = monsters[0]

    while hero_select_enemy_menu_open == True:

        print("\nHero select fight menu")
        print("1. select enemy")
        print(f'2. Fight {selected_enemy.get_type_of_enemy()}')
        print("3. Go back")
    
        hero_battle_option = input("Enter your choice: ")

        if hero_battle_option == '1':
           selected_enemy = select_enemy_menu(monsters, selected_enemy)
        elif hero_battle_option=='2':
            hero_battle(hero,selected_enemy)
        elif hero_battle_option=='3':
            hero_select_enemy_menu_open = False
        else:
            print("Invalid option. Please try again.")


def hero_battle_menu():

    menu_open = True
    zombie = Zombie(20,3)
    ogre = Ogre(30,3)
    vampire = Vampire(25,3)
    golem = Golem(35,2)
    hero = Hero(20,2)
    dagger = Weapon("Dagger",1)
    sword = Weapon("Sword", 3)
    greatsword = Weapon("Greatsword",6)
    weapon_list = [dagger, sword, greatsword]
    weapon = None
    hero.weapon = weapon
    hero.equip_weapon()
    monsters = [zombie,ogre,vampire,golem]
   
    while menu_open:
    
        print("\nHero battle menu")
        print("1. Select weapon")
        print("2. Random Fight")
        print("3. Select Fight")
        print("4. Go back")

        hero_battle_option = input("Enter your choice: ")

        if hero_battle_option == '1':
            hero_weapon_select_menu(weapon_list, hero)
        elif hero_battle_option=='2':
            hero_battle(hero,monsters[random.randint(0,len(monsters)-1)])
        elif hero_battle_option=='3':
            hero_battle_select_enemy(hero, monsters)
        elif hero_battle_option=='4':
            break
        else:
            print("Invalid option. Please try again.")

def hero_battle_select_fight():
    print('Selec fight')

play = True
while play:

    print("\nSelect an option:")
    print("1. Hero Battle")
    print("2. Monster Battle")
    print("3. Exit")
    
    option = input("Enter your choice: ")
    
    if option == '1':
        hero_battle_menu()
        
    elif option == '2':
        zombie = Zombie(20,3)
        ogre = Ogre(30,3)
        vampire = Vampire(25,3)
        golem = Golem(35,2)
        monsters = [zombie,ogre,vampire,golem]
        selected_monsters = random.sample(monsters, 2)
        battle(selected_monsters[0],selected_monsters[1])
        
    elif option == '3':
        print("Exiting the game. Goodbye!")
        play = False
    else:
        print("Invalid option. Please try again.")