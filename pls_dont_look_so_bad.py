# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random
from random import randint
from characters import*


def fight():
    randomEnemy = random.choice(enemylist)
    enemy = randomEnemy
    randomAlly = random.choice(allyList)
    enemy.default()
    print(f'A wild {enemy} has appeared')
    enemy.appear()
    hero.status()
    while hero.alive():
        if enemy.dead():
            enemy.restore()
            randomEnemy = random.choice(enemylist)
            enemy = randomEnemy
            enemy.default()
            enemy.appear()
            print(f'A wild {enemy} has appeared')
            hero.status()
        print(f'''
============================
What would you like to do?
1. Fight
2. Heal
3. Flee
>>>>>>>>>>>>>>>''')       
        raw_input = input()
        if raw_input == "1":
            attacker = input('''
Who is attacking?
=================
1. The Hero
2. Medic       ''')
            if attacker == '1':
                hero.attack(enemy)
            if attacker == '2':
                medic.attack(enemy)
        elif raw_input == "2":
            healTarget = input('''
Who would you like to heal?
===========================
1. The Hero
2. The Medic''')
            if healTarget == '1':
                medic.heal(hero)
            if healTarget == '2':
                medic.heal(medic)
            
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        enemy.attack(random.choice(allyList))
        
        if medic.health > 15:
            medic.selfHeal



fight()




