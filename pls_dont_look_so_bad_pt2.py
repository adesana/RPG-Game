# Characters

from random import randint

enemyDic = {}

class Character:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def alive(self):
        return self.health > 0
    def __repr__(self):
        return self.name
    def dead(self):
        return self.health < 0
        if self == zombie:
            self.dead()==self.alive()






class Hero(Character):



    def attack(self, enemy):
        prob = randint(1,10)
        if enemy.name == shadow:
            if prob == 1:
                enemy.health -= self.power
                (f"You do {self.power} damage to the {enemy}.")
            if prob > 1:
                self.power = 0
                print('Your attack has been negated by an unknown power')
            if shadow.health <= 0:
                print(f'{shadow} is dead.')        
                
        if prob <= 2:
                enemy.health -= (self.power*2)
                print(f"Critical strike! You do {self.power*2} damage to the {enemy}.")
        if prob > 2:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")  
        if enemy.health <= 0:
            print(f'{enemy} is dead.')
        if enemy.name == shadow:
            if prob == 1:
                enemy.health -= self.power
                (f"You do {self.power} damage to the {enemy}.")
            if prob < 1:
                self.power = 0
                print('Your attack has been negated by an unknown power')
            if shadow.health <= 0:
                print(f'{shadow} is dead.')
                

        

    
    def status(self):
        print("You have {} health and {} power.".format(self.health, self.power))
        
            
          

class Goblin(Character):

    enemyDic = {}
    def attack(self, enemy):
        if self.health > 0:
            # Goblin attacks hero
            enemy.health -= self.power
            print(f"The goblin does {self.power} damage to {enemy}.")
            if enemy.health <= 0:
                print("You are dead.")

    def status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))
             
    def default(self):
        enemyDic.update({self.name : self.health})
    def restore(self):
        self.health = enemyDic['Goblin']
    def appear(self):
        print('''
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⠤⢶⣿⣿⣿⡿⠋⠛⢻⣷⣤⡀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣠⠶⣏⣀⣼⣿⣿⣿⣷⣄⣀⣈⣿⡿⢷⡀⠄⠄⠄⠄⠄⠄
⠄⠄⢠⠤⠤⠤⠠⠾⠷⠾⠿⣿⣿⠿⠛⠛⠛⠛⣛⣋⣉⣁⡀⢳⡀⠄⠄⠄⠄⠄
⠄⠄⢸⡀⢰⡆⢀⡤⠄⢰⡂⠉⠛⠁⢹⣿⠿⠛⢩⣥⣶⣿⠃⢸⣧⠄⠄⠄⠄⡄
⠄⠄⠄⣧⡄⡇⢸⠁⣶⣧⠄⣤⣿⣧⠈⠁⣶⣷⠄⢸⣿⣿⠄⣿⣿⠄⠄⠄⣼⡇
⠄⠄⢶⣌⡁⠉⠘⠄⠈⢁⣔⠉⢹⣿⢆⢠⣬⣥⣤⣤⣤⣤⣤⣿⠟⣠⠶⢋⡽⠁
⠄⠄⢠⠛⠃⣤⢾⣿⠃⣎⣹⣿⣿⣷⠿⢆⣿⠿⠿⠟⣛⡛⠿⣿⣼⠃⣶⡞⠃⠄
⠄⠄⠄⢠⣼⢱⠖⡀⡀⢿⣿⠿⠛⣁⣋⣭⠖⣌⠻⢿⣿⠟⡆⣹⣥⡏⣀⡄⠄⠄
⠄⠄⢿⡈⢹⡎⣾⡇⠱⠈⡁⠄⣶⠉⣉⢁⢸⣿⡀⠈⠁⣆⣰⣿⠏⣰⣿⡇⠄⠄
⠄⠄⠄⢀⣀⣓⠘⠃⢛⣠⣥⣤⣶⡶⣶⣶⣦⣤⣤⣴⠾⢋⣌⠻⠂⣉⣉⠄⠄⠄
⠄⣴⡃⣿⡿⢡⣆⢉⣛⣩⣭⣤⣶⣶⣦⣬⣭⣥⣶⡶⠇⣿⡟⢰⣷⡌⣿⣷⡀⠄
⢀⠻⡇⠛⢃⡟⣿⢰⣌⢙⠻⠿⢿⣿⡿⢻⠟⣁⠉⢡⡆⠋⠞⣸⠟⡁⠉⣿⣧⠄
⠘⢧⡄⣤⣤⢠⡟⣸⣿⣿⣧⣀⣠⣜⣠⣤⣼⣿⡇⠸⢃⣼⡄⢃⣼⠃⣤⣿⣿⠄
⠄⠄⠁⠄⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⠁⠄⠄⠄⠄⠄''')
    

class Medic(Character):
    

    def selfHeal(self):
        prob = randint(1,10)
        if prob <= 2:
            self.health += 2
            print('The medic healed itself')

    def heal(self, target):
        target.health += 3 
        print(f'The Medic has healed {target}, new health is {target.health}')

    def attack(self, enemy):
        if self.health > 0:
            enemy.health -= self.power
            print(f"The Medic does {self.power} damage to {enemy}.")
            if enemy.health <= 0:
                print("You are dead.")

        




class Shadow(Character):
    
    def attack(self, enemy):
        if self.health > 0:
            # Goblin attacks hero
            enemy.health -= self.power
            print(f"The Shadow does {self.power} damage to {enemy}.")

    def default(self):
       enemyDic.update({self.name : self.health})
    def restore(self):
        self.health = enemyDic['Shadow']

    def appear(self):
        print('''
⠄⠄⠄⠄⠄⠄⠄⠄⣔⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠄⢣⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠇⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⢠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠘⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⡌⣿⣿⢿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⢷⠄⠇⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢰⢸⠉⠠⠻⠎⠻⢿⣿⣿⣿⣿⠿⠋⠙⠛⢿⡇⠃⢸⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⡆⣾⠄⠄⠄⠄⠄⠄⠘⣿⣿⠄⠄⠰⠆⠄⢸⣿⠇⠄⡆⠄⠄⠄⠄
⠄⠄⠄⠄⠰⠄⣿⠄⢀⠄⠄⠄⠄⣸⣿⣿⣷⣄⣠⣶⣶⣾⣿⣠⠄⢠⠄⠄⠄⠄
⠄⠄⠄⠄⠂⠄⣻⠄⠄⠄⣤⠠⠈⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠄⠈⡄⠄⠄⠄
⠄⠄⠄⠘⠄⠄⢿⡄⠄⢸⣻⡃⠄⢾⣿⣿⡿⣿⣿⣿⣿⣿⣿⣸⠄⠄⢃⠄⠄⠄
⠄⠄⢀⠃⠄⠄⣞⣇⠄⠐⡿⣣⡤⠤⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠘⡀⠄⠄
⠄⠄⡘⠄⠄⠄⠹⣞⡀⠄⠄⠋⠄⠄⠄⠄⠉⠛⢛⣿⣿⣿⣿⡇⠄⠄⠄⠇⠄⠄
⠄⢀⠁⠄⠄⠄⠄⢻⣷⡀⠄⠄⢀⣀⣤⣤⣴⣶⣶⣿⣿⣿⣿⡗⠄⠄⠄⢸⠄⠄
⠄⡘⠄⠄⠄⠄⠄⠄⠻⣿⣦⣀⣨⣵⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⠄⠄⡆⠄
⢀⠃⠄⠄⠄⠄⠄⠄⢴⣺⣿⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⢣⠄
⠘⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠸⡄''')

class Zombie(Character):
    
    newHealth = ''
    def attack(self, enemy):
        if self.health > 0:
            # Goblin attacks hero
            enemy.health -= self.power
            print(f"The Zombie does {self.power} damage to {enemy}.")
            if enemy.health <= 0:
                print("You are dead.")
    def default(self):
        enemyDic.update({self.name : self.health})
    def restore(self):
        self.health = enemyDic['Zombie']
    
    def appear(self):
        print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠆⠄⠤⡆⠰⢶⡉⣾⡽⢑⡈⣷⠴⣤⣿⡀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣞⢒⡀⢐⡛⢢⠀⣹⠬⠃⣠⣥⣘⣶⣁⣿⡇⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠃⠀⡀⣀⠐⠐⠂⠘⠀⠋⢛⠿⢿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠘⠀⠀⢢⣦⠀⠀⠀⢴⣿⣖⡛⠙⠻⣿⡇⢠⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢻⡇⠀⢠⡖⠁⢹⣷⣤⠀⣼⡿⠋⠉⢗⣾⣿⠁⢨⠈⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⠀⠀⢿⣧⣀⣠⠿⣿⠀⣿⡙⠢⠤⣞⣿⣿⠀⣼⠀⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢹⡆⠀⠘⣷⣍⣯⣴⣿⣤⣿⣿⡖⠤⠯⡿⣿⠀⢻⠀⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⡇⠀⠈⠙⠛⣅⣼⣿⠙⡇⠙⢧⡀⠀⠀⣿⡄⢾⠁⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡇⢸⡗⡖⠒⢊⣿⣿⠀⣧⠀⢾⣯⠣⡀⢻⠇⡙⣖⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢱⣿⣿⡇⢠⣿⣿⣿⠀⣿⡇⢸⣿⠁⠀⢹⢠⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢸⣿⡏⡇⣼⣿⣀⣿⣠⣾⠃⠈⠟⡇⠀⢰⢸⡇⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡇⡇⣷⣿⣿⣿⣿⣾⣧⡀⠀⠁⠠⣼⠀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣇⡇⣿⠟⢿⣋⣿⣶⣿⣣⠀⠀⠐⢻⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡏⡇⣿⢲⣌⡏⡏⣿⣿⣏⣱⠀⠀⣸⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣷⡇⣿⣷⣿⣿⣿⣿⣏⣻⠋⢀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⡷⣿⣯⣽⣿⣿⣿⣿⣿⣆⠼⠐⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠃⢻⣧⣾⣿⡿⢿⣿⣿⡿⠠⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣅⢸⡿⣍⡿⠧⠼⠟⣼⠇⠀⡼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠘⣎⣁⡿⣝⣦⡾⢿⡿⠀⡸⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠘⣿⣿⣿⠛⢧⣼⣗⡰⠃⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⢿⠀⠀⠀⠘⣿⣿⣶⣿⣿⡟⠁⠀⠀⠀⣼⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡉⠀⠀⠪⣸⡇⠀⢀⡀⣿⣿⣿⣿⣿⡇⠀⠀⠀⢠⣿⣟⠀⡈⠙⣯⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡿⡄⠁⢀⠾⠀⢘⣿⡀⡎⠉⣿⣿⣿⣿⢻⣧⡄⡄⢀⣿⣿⢿⡄⢙⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣛⣯⣵⣾⣿⣿⡇⠈⣶⠞⠀⠀⠘⠿⣳⡇⠀⢻⡇⢻⡟⢿⡃⠙⣧⣿⢟⣞⣤⡌⣿⡧⣼⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⣨⢣⠀⠀⠀⠀⠄⠻⡄⣿⠁⣾⣀⣼⣉⣳⡿⣫⣾⠏⠁⣰⣿⢡⣿⡋⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠿⠛⠛⠉⠉⠉⠋⠁⠀⡞⠀⠀⢃⡄⢠⣑⡌⠒⠜⣾⣚⣿⣿⣿⣽⠟⢁⣿⡁⠀⢠⣿⠿⠘⠋⠀⠀⠀⠀⠀⢸⣿⡿⠟⠋⠙⢻⣿
⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠘⢿⡈⡯⠻⡦⣦⠈⣿⣝⣿⠟⢧⠄⢾⣤⣾⣶⣿⡯⡄⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠈⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠈⠑⢿⡄⠙⣦⠀⠈⣿⠃⠀⡗⢦⡸⢉⣿⣿⠏⠘⠀⠀⠀⠀⠀⠀⢀⣤⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠀⢘⡗⣾⡟⢸⣸⣇⣠⣷⠛⠉⡍⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢀⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣂⡀⣰⡟⠁⣿⡇⠈⣿⣟⠁⠈⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠉⠉⠏⠿⣇⠀⣾⠃⢠⣏⢧⡆⠀⠀⠀⣨⣄⣤⣤⣤⡴⣦⣆⠀⠀⠀⠀⠀⠀⠀⣶⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⣿⠀⡿⠀⣾⡏⠸⠁⠀⠀⢠⡿⣻⢿⣂⣻⣟⣦⠿⠃⠀⠀⠀⢀⠀⢠⠁⠀⠀⠀''')

hero = Hero('Hero',10,5)
goblin = Goblin('Goblin', 6,2)
medic = Medic('Medic', 15,2)
shadow = Shadow('Shadow',1,6)
zombie = Zombie('Zombie',6,3)




enemylist = [goblin, shadow, zombie]
allyList = [hero, medic]