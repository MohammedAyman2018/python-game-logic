import time # Importing time module
import random 

# configration
places = ['forest', 'desert', 'house']
forst_animals = ['Bear','Rabbit','Lion','Wolf','Monkey']
desert_animals = ['Alien','Giant Monster','snake','Dog']
home_acts = ['Eat','Drink','sleep', 'watch movie']
weapons = ['sword', 'knife', 'shotgun', 'rock']
game_results = ['win', 'lose']

def game ():
    # Make user choise levels
    print ("Choose a level")
    for place in places:
        print(place)
        
    time.sleep(1)
    levels = input("Choose 1, 2 ,3 \n")

    if (levels == '1'or levels == 'forest'):
        forest()
    elif (levels == "2" or levels == 'desert'):
        desert()
    elif (levels == '3' or levels ==  'house'):
        house()


# make user choose a weapon
def weapon_choose():
    current_weapon = random.choice(weapons)

    print('your weapon is ' + current_weapon)
    request = input('wanna another weapon?')
    if(request == 'yes'):
        weapon_choose()
    elif (request == 'no'):
        return current_weapon
    else:
        print('please type yes or no')
        weapon_choose()
        
# choose a monester randomly
def monester_choose(animals_array):
    currrent_monester = random.choice(animals_array)
    print('there is ' + currrent_monester)

# End game
def result():
    result = random.choice(game_results)
    print('you ' + result)

    if(result == 'win'):
        time.sleep(2)
        choose = input('wanna play again? \n')
        if(choose == 'yes'):
            game()
        elif(choose == 'no'):
            print('Thanks for playing')
            input()
            return
        else:
            print("please type yes or not \n")
    else:
        print('Game Over')
        time.sleep(2)
        choose = input('wanna play again? \n')
        if(choose == 'yes'):
            game()
        elif(choose == 'no'):
            print('Thanks for playing')
            input()
            return
        input()
        
    
# create forest fnction
def forest():
    current_weapon = weapon_choose()
    currrent_monester = monester_choose(forst_animals)
    time.sleep(2)
    result()
    
# create desert fnction
def desert():
    current_weapon = weapon_choose()
    currrent_monester = monester_choose(desert_animals)
    time.sleep(2)
    result()
# create house fnction
def house():
    weapon_choose()
    
# Introduction
print("lorem ipsum lorem ipsum lorem ipsum ")
time.sleep(2)
print("lorem ipsum lorem ipsum lorem ipsum lorem ")

# Get user name
name = input("Enter your name ")
print ("Hello " + name)
game()
