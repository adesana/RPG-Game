# Python Online
import random
from char import*

def bag1():
    bag.bagPower()
    if bag.amount > 0:
        print(f'''
====================================================
                Welcome to your bag!
    1. Super Tonic               2. Armor
    Amount:{superTonic.amount}                  Amount:{armor.amount}
    
    2. Evade                     3. Swap
    Amount:{evade.amount}                   Amount:{swap.amount}
                    5.Leave
=====================================================''')
    result = input ('>>')
    if result == '1':
        superTonic.use(hero)
        bag.amount -= 1
    if result == '2':
            armor.use(hero)
            bag.amount -= 1
    if result == '3':
            evade.use(hero)
            bag.amount -= 1
    if result == '4':
            swap.use(hero)
            bag.amount -= 1
    if bag.amount <= 0:
        bag.bagRes()
        return




def status():
    hero.status()
    main()

def shop():
    print('''
===================================================    
            Welcome to the shop!
        Please select one of the below!
    1. Super Tonic              2. Armor
    +100 Health                 +20 Armor
    80 Gold Coins               20 Gold Coins
    
    3. Evade                    4. Swap
    Add 20 Evade skill points   Swaps attack power with oppoenents.
    50 Gold Coins               50 Gold Coins
                    5. Leave
====================================================''')
    result = input('>>')
    if result == '1':
        if hero.gold >= 80:
            superTonic.amount += 1
            main()
        else:
            print("You don't have enough gold!")
            main()
    if result == '2':
        if hero.gold >= 20:
            armor.amount += 1
            main()
        else:
            print("You don't have enough gold")
            main()
    if result == '3':
        if hero.gold >= 50:
            evade.amount += 1
            main()
        else:
            print("You don't have enough gold!")
            main()
    if result == '4':
        if hero.gold >=50:
            swap.amount += 1
            main()
        else:
            print("You don't have enough gold!")
            main()
    if result == '5':
        main()

def heal():
    print('''
=================================================
            Welcome to the healing altar!
            Please select one of the below
    1. +100 Health                  2. +50 Health
     60 Gold coins                    30 Gold coins
    3. +100 Mana                    4. +50 Mana
     40 Gold coins                    20 Gold coins
                      5. Leave
==================================================''')
    result = input('>>')
    if result == '1':
        if hero.gold >= 60:
            hero.gold -= 60
            hero.health += 100
            main()
        else:
            print("You dont have enough gold!")
            main()
    elif result == '2':
        if hero.gold >= 30:
            hero.gold -= 30
            hero.health += 50
            main()
        else:
            print("You don't have enough gold!")
            main()
    elif result == '3':
        if hero.gold >= 40:
            hero.gold -= 40
            hero.mana += 100
            main()
        else:
            print("You don't have enough gold!")
            main()
    elif result == '4':
        if hero.gold >= 20:
            hero.gold -= 20
            hero.mana += 50
            main()
        else:
            print("You don't have enough gold!")
            main()
    elif result == '5':
        main()

def fight():
    randomEnemy = random.choice(enemyList)
    enemy = randomEnemy
    enemy.default()
    hero.heroPower()
    print(f'''
A wild {enemy} has appeared''')
    while hero.alive():
        hero.status()
        print('''
====================================================
            Please choose an attack
1. Stab(1x damage)       2. Slash(1.5x damage)
      0 Mana                     40 mana
3. Stun(Stun & flee)     4. Sword Dance(2x damage)
       100 Mana                  60 mana
                    5. Bag
====================================================''')
        result = input('>>')
        if result == '1':
            hero.attack(enemy, '1')
        elif result == '2':
            hero.attack(enemy, '2')
            hero.mana -= 40
        elif result == '3':
            hero.attack(enemy, '3')
            hero.mana -= 100
        elif result == '4':
            hero.attack(enemy, '4')
            hero.mana -= 60
        if enemy.alive() == False:
            print(f'The {enemy} is dead. Returning to main menu.')
            enemy.restore()
            hero.gold += enemy.gold
            main()
        elif result == '5':
            bag1()
        enemy.attack(hero, '0')
        hero.mana +=10
    else:
        print('You have died! Game over!')









print('''
         Welcome to Python Online!''')
def main():
    print('''
========================================
----------------------------------------
    1. Fight      2. Heal      3. Status
        4. Shop         5. Quit
----------------------------------------
========================================''')
    result = input('>>')
    if result == '1':
        fight()
    elif result == '2':
        heal()
    elif result == '3':
        status()
    elif result == '4':
        shop()
    elif result == '5':
        print ('Goodbye')
        return

main()