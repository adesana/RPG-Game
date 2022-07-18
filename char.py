# Characters


from random import randint

charDic = {}
heroDic = {}
bagDic = {}


class Character:
    def __init__(self, name, power, health, mana, armor, evade, gold):
        self.name = name
        self.power = power
        self.health = health
        self.gold = gold
        self.mana = mana
        self.armor = armor
        self.evade = evade
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def __repr__(self):
        return self.name
    def default(self):
        charDic.update({self.name : self.health})
    def heroPower(self):
        heroDic.update({self.name : self.power})
    def heroRes(self):
        self.power = heroDic['Hero']
    def heroAttack(self, enemy, type):
        prob = randint(1,10)
        if type == '1':
            enemy.health -= self.power
            print(f'You attack the enemy with stab and do {self.power}, {enemy} health is now {enemy.health}')

        if type == '2':
            if self.mana >= 40:
                enemy.health -= self.power*1.5
                print (f'You attack the enemy with slash and do {self.power*1.5}, {enemy} health is now {enemy.health}')
            else:
                print("You don't have enough mana.")
        if type == '3':
            if prob > 2:
                print(f'You have failed to escape the {enemy}!')
            elif prob <= 2:
                print(f'You have sucessfully escaped the {enemy}!')
                enemy.health -= self.power*100
        if type == '4':
            if self.mana >= 60:
                enemy.health -= self.power*2
                print(f'You attck the enemy with sword dance and do {self.power*2}, {enemy} health is now {enemy.health}')
            else:
                print("You dont have enough mana.")
    def attack(self, enemy, type):
        prob = randint(1,10)
        dodge = enemy.evade*.5
        if enemy.name == 'Shadow':
            if prob > 1:
                self.power = 0
                print(f'You do {self.power} to the shadow, your attack seems to be blocked by unknown means.')
            elif prob == 1:
                self.power = heroDic['Hero']
                self.heroAttack(enemy, type)
        if enemy.name == 'Dark Priest':
            if prob <= 2:
                self.heroAttack(enemy, type)
                enemy.health += 10
                print(f'The Dark Priest has automatically healed for 2 health. {enemy.health}')
            else:
                self.heroAttack(enemy, type)

        elif enemy.name == 'Goblin':
            if prob < 5:
                self.power = 0
                print (f'You do {self.power} to the Goblin, your attack has been evaded.')
            elif prob > 5:
                self.power = heroDic['Hero']
                self.heroAttack(enemy, type)
        if enemy.name == 'Zombie':
            print(f'This creature is immortal, use an item or stun to run away.')
            self.heroAttack(enemy, type)
        if enemy.name == 'Hero':
            prob = randint(1,100)
            while prob > dodge:
                if enemy.armor > 0:
                    enemy.health  -= (self.power - enemy.armor)
                    print(f'{self} has done {self.power - 10} to {enemy}, new health is {enemy.health}')
                    enemy.armor -= 10
                    break
                elif enemy.armor <= 0:
                    enemy.health -= self.power
                    print(f'{self} has done {self.power} to {enemy}, new health is {enemy.health}')
                    break
            else:
                print('You have evaded the attack')
    def status(self):
        print(f' You have {self.power} power, {self.mana} mana, {self.health} health, {self.armor} armor, {self.evade} evade and {self.gold} gold.')



class Hero(Character):
    def restore(self):
        self.power = heroDic['Hero']
class Goblin(Character):        
    def restore(self):
        self.health = charDic["Goblin"]


class Shadow(Character):
    def restore(self):
        self.health = charDic["Shadow"]
class Zombie(Character):
    def restore(self):
        self.health = charDic["Zombie"]  
class DarkPriest(Character):
    def restore(self):
        self.health = charDic["Dark Priest"]      

class Items:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name
    def uses(self):
        self.amount += 1
    def bagPower(self):
        bagDic.update({self.name : self.amount})

class SuperTonic(Items):
    def use(self, target):
        target.health += 100
        target.status()
        self.amount -= 1
class Armor(Items):
    def use(self, target):
        target.armor += 20
        target.status()
        self.amount -= 1

class Evade(Items):
    def use(self, target):
        hero.evade += 20
        self.amount -= 1
class Swap(Items):
    def use(self, target, enemy):
        pass
class Bag(Items):
    def bagRes(self):
        self.amount = bagDic['Bag']

superTonic = SuperTonic('Super Tonic', 0)
armor = Armor('Armor', 0)
evade = Evade('Evade', 0)
swap = Swap('Swap', 0)
bag = Bag('Bag', 1)












hero = Hero('Hero', 30, 100, 100, 0, 0, 0)
shadow = Shadow('Shadow', 5, 1, 0, 0, 0, 40)
zombie = Zombie('Zombie', 10, 2000, 0, 0, 0, 0)
darkPriest = DarkPriest('Dark Priest', 10, 100, 0, 0, 0, 40)
goblin = Goblin('Goblin', 10, 60, 0, 0, 0, 40)

enemyList = [shadow, darkPriest, goblin]