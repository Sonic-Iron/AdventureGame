print("Do not put in a false answer for the pack, it will crash")
print("Use this in terminal")

#will need to use this code later
#
#  s = Sound() 
#  s.read('sound.mp3') 
#  s.play()


#imports
import random
import time
import os,sys
import shutil
import os.path

#variables
win = 0
level = 0    
steps = 0
coins = 10
xp = 1
inventory = []
Num_Iron = 0
attack_strength = 0
brought_item = 0
sword_durability = 10
collectables = ["squashed monster in a bottle","broken sword"]
#admin
itemcouldwin = []
couldstart = []
path = "./"
os.system("color a")
devmode = True

#Plugin loader
plugins = {}
for plugin in os.listdir('Plugins'):
    if not plugin[0] == '$' and plugin.endswith('.py'):
        file = open('Plugins/' + plugin, 'r')
        class new_plugin:
            exec(file.read())
        file.close()
        plugins[plugin] = new_plugin

#difficulty settings
difficulty = input("What is the difficulty? Easy[E], medium[M] or Hard[H]\n")
if difficulty == "E":
    energy = 150
    hunger = 150
    Work_seconds = 3
    sleep_seconds = 4
    monster_attack_rate = 3
if difficulty == "M":
    energy = 100
    hunger = 100
    Work_seconds = 10
    sleep_seconds = 10
    monster_attack_rate = 2
if difficulty == "H":
    energy = 50
    hunger = 50
    Work_seconds  = 15
    sleep_seconds = 15
    monster_attack_rate = 1
else:
    energy = 100
    hunger = 100
    Work_seconds = 10
    sleep_seconds = 10
    monster_attack_rate = 2


#setup
os.system("title AdventureGame")

if os.path.exists("__pycache__"): #remove cache
    shutil.rmtree("__pycache__")

dirs = os.listdir(path)

filelist = list()
i=0
for file in dirs:
    if file == "AdventureGameDefinitiveEdition.py":
        ""
    elif file == "files":
        ""
    else:
        filelist.append(i)
        filelist[i] = file
        i=i+1
        print(i,".",file[0:len(file)-3])


chooseLibrary = "Which pack do you want? 1-"+str(len(filelist))+" "
mychoice = input(chooseLibrary)
if mychoice == "":
    mychoice = 1

myimport = filelist[int(mychoice)-1]
lengthoffilename = len(myimport)
libraryname = myimport[0:lengthoffilename-3]


print(libraryname)

myimport = __import__(libraryname) #import data from chosen map

database = myimport.default_database()
object_database = myimport.default_object_database()
monster_database = myimport.default_monster_database()


for a in database:
    if "dependency" in database[a]:
        for b in database[a]["objects_in_building"]:
            if b not in itemcouldwin:
                itemcouldwin.append(b)
            
x = random.choice(itemcouldwin)
win = x

for a in database:
    if "dependency" in database[a]:
        ""
    else:
        if a not in couldstart:
            couldstart.append(a)

x = random.randint(0,len(couldstart)-1)
current_location = couldstart[x]


def info():
    print("you have :\n\t",level,"\tlevels.\n\t",coins,"\tcoins.\n\t",hunger," \thunger.\n\t",energy," \tenergy. \n\t",xp," \txp.\n\t",steps," \tsteps.")


def helper(): #help tool
        print("You can 'look', 'move', 'health','drop item','pick up', 'inventory','work','sleep")
        knowabout = input("What would you like to know about?")
        if knowabout == "look":
              print("use this to see what is in your environment")
        elif knowabout == "move":
              print("use this is move to difference location")
        elif knowabout == "health":
              print("use this is see your stats- hunger, coins, etc, etc...")
        elif knowabout == "drop item":
              print("to drop an item type ' drop [an item in your inventory]")
        elif knowabout == "pick up":
            print("to pick up an item type ' drop [an item in your current location]")
        elif knowabout == "inventory":
            print("Your inventory is what you are  carrying, type 'inventory to see it'")
        elif knowabout == "work":
            print("You can only work at a business, you can get money to buy food")
        elif knowabout == "sleep":
            print("You can sleep at your house, gain energy by doing it, the length of time it takes is based on your difficulty")

os.system("cls")

     
current_monster = "none"
print("Welcome to CommandQuest. Type an instructon to move around the map and interact with the game.  If you are not sure what to do, just type 'help' and follow the instructions") 
print("\nYou are on a mission to find the",win,"in the shortest number of steps, if you beat the time of the highscorer then you will be the new highscorer\n\n")
input("press ENTER")
while True:
    start = time.time()
    print("You are at the ",current_location)
    cmd = input("\nEnter a command : ")

    for a in inventory: #check inventory for collectables
        for b in collectables:
            if b in a:
                energy = energy + 5
                
    if cmd == "" or cmd == "help":
        helper()

        
    if cmd == "health": #show info for player
        info()


    if energy < 0:
        wintype = "death"
        break


    if hunger < 0:
        wintype = "death"
        break        

    if cmd == "look":
        print("Your location is ",current_location)
        print(database[current_location]['description'])
        if len(database[current_location]['objects_in_building']) <= 0:
            print("\nThere's nothing else here")
        else:
            print("\nYou can see ",database[current_location]['objects_in_building'])
           
    if cmd == "move":
        print("Where would you like to move to?")
        print(database[current_location]["directions"])
        new_location = input("")
        if new_location not in database[current_location]['directions']: #Can't find location
           print("Can't go there...")
        else:
            if 'dependency' in (database[new_location]): 
                   if database[new_location]['dependency'] not in inventory:
                     print("You need ",database[new_location]['dependency'],"to go there.") 
                   else:
                       x = random.randint(0,monster_attack_rate)
                       if x == 0:
                           keeys = list(monster_database.keys())
                           current_monster = random.choice(keeys)
                           print("You get attacked by",current_monster,)
                           print(monster_database[current_monster]["picture"])
                           what_to_do = input("Do you want to run or attack?")
                           if what_to_do == "attack":
                               for item in inventory:
                                #Add up the attack points for any object that has them
                                   if "attack" in object_database[item]:
                                       attack_strength = attack_strength + object_database[item]['attack']
                               print("Attack stength is ",attack_strength)         
                               if attack_strength > (monster_database[current_monster]["health"]):                 
                                   xp = xp + 1  
                                   print("You defeated the monster")
                                   energy = energy - monster_database[current_monster]["health"]
                                   steps += 1
                                   info()
                               else:
                                   energy = energy - monster_database[current_monster]["health"]
                                   current_location = new_location
                                   steps += 1
                                   print("You get defeated by the",current_monster,"and get tired")
                                   info()
                           elif what_to_do == "run":
                              energy = energy - 5
                              steps = steps + 1
                              print("You run back to your previous location and get slighly tried")
                           else:
                               print("\nYou did not run away or fight the monster so you get defeated by it anyway")
                               energy = energy - monster_database[current_monster]["health"]
                                
                       else:
                           current_location = new_location
                           steps += 1
                           energy = energy -10
                           info()
            else:
                x = random.randint(0,monster_attack_rate)
                if x == 0:
                    keeys = list(monster_database.keys())
                    current_monster = random.choice(keeys)
                    print("You get attacked by ",current_monster,)
                    print(monster_database[current_monster]["picture"])
                    what_to_do = input("Do you want to run or attack?")
                    if what_to_do == "attack":
                        attack_strength = 0 
                        for item in inventory:
                        #Add up the attack points for any object that has them
                            if "attack in object_database[item]":
                                attack_strength = attack_strength + object_database[item]['attack']
                        print("Attack stength is ",attack_strength)
                        if attack_strength > (monster_database[current_monster]["health"]):                 
                            xp = xp + 1  
                            print("You defeated the monster")
                            current_location = new_location
                            steps += 1
                            info()
                        else:
                            energy = energy - monster_database[current_monster]["health"]
                            current_location = new_location
                            steps += 1
                            print("You get defeated by the", current_monster, "and get trired")
                            info()
                    elif what_to_do == "run":
                        energy = energy - 5
                        steps = steps + 1
                        print("You run back to your previous location and get slighly tried")
                    else:
                        print("\nYou did not run away or fight the monster so you get defeated by it anyway")
                        energy = energy - monster_database[current_monster]["health"]
                                
                else:
                    current_location = new_location
                    steps += 1
                    energy = energy -10
                    info()
                

    if cmd[0:8] == "pick up ":
        if cmd[8:len(cmd)] in database[current_location]["objects_in_building"]:
            picked_up_item = cmd[8:len(cmd)]
            if database[current_location]['type'] == "Selling_point":
                coins = coins - 1 
                inventory.append(picked_up_item)
                database[current_location]['objects_in_building'].remove(picked_up_item)
                print("Your inventory is",inventory)
                info()
            else:
                inventory.append(picked_up_item)
                database[current_location]['objects_in_building'].remove(picked_up_item)
                print("Your inventory is",inventory)    
            if picked_up_item == win:
                wintype = "winner"
                break

    if cmd[0:4] == "drop":
        dropitem = cmd[5:len(cmd)]
        if dropitem in object_database:
            if dropitem in inventory:
                print("You drop the",dropitem)
                inventory.remove(dropitem)
                database[current_location]["objects_in_building"].append(dropitem)
            else:
                print("That item is not in your inventory!")
        else:
            print("That item does not exist!")
       

    while len(inventory) > 5:
        print("You have more than 5 items")
        dropped_item = input("Which item would you like to drop?")
        if dropped_item not in inventory:
            print("That item is not in your inventory")
        else:
            database[current_location]["objects_in_building"].append(dropped_item)
            inventory.remove(dropped_item)

    if cmd == "inventory":
        print(inventory)



    if database[current_location]["type"] == "Work_point":
        if cmd == ("work"):
            print("You work for",Work_seconds,"hours")
            oldworksecs = Work_seconds
            while Work_seconds  > 0:
                print(Work_seconds)
                Work_seconds = Work_seconds - 1
                time.sleep(1)
            print("You worked for 1 coin")
            coins = coins + 1
            hunger = hunger - 10
            Work_seconds = oldworksecs
            info()



    if cmd == "sleep":
        sleepy = sleep_seconds
        print("You sleep for",sleep_seconds,"hours")
        while sleepy > 0:
            print(sleepy)
            sleepy = sleepy - 1
            time.sleep(1)
        print("You slept for",sleep_seconds,"hours and gained 15 energy")
        energy = energy +15
        info()

    if cmd == "eat":
        print(inventory)  
        eat = input("What would you like to eat?")
        if eat not in inventory: 
            print("That item is not in your inventory")
        else:
            if object_database[eat]["type"] == "eat":
                print("You eat it, that was very refreashing")
                hunger = hunger + 15
                inventory.remove(eat)
            else:
                print("That is not a food\n")
                
    if cmd == 'devmode':
        print('''Devmode help:
Enable by setting devmode to True

Commands:
examine item - see details for item
give item (also get) get an item
teleport (also tp) go to a location''')
    
    if cmd == "examine item" and devmode:
        print(object_database)
        current_item = input ("Which item would you like to look at?")
        if current_item not in object_database:
            print("That item dosn't exist!")
        else:
            print(object_database[current_item]["description"])
            print("It has",object_database[current_item]["attack_points"]," attack points")


    if xp > 10:
        print("You leveled up one level")

    if cmd == "give item" and devmode:
        for c in object_database:
            print(c)
        I =input("Which item would you like to have?")
        if I in object_database:
            for a in range(3):
                print("Giving.")
                time.sleep(0.5)
                os.system("cls")
                print("Giving..")
                time.sleep(0.5)
                os.system("cls")
                print("Giving...")
                time.sleep(0.5)
                os.system("cls")
            time.sleep(0.2)
            inventory.append(I)

    if (cmd == "teleport" or cmd == 'tp') and devmode:
        for a in database:
            print(a)
        where = input("Where would you like to teleport to?")
        if where in database:
            current_location = where
    if cmd == 'get' and devmode:
        for o in object_database.keys():
            print(o)
        get = input('Which item would you like to get? ')
        if get in object_database:
            if get in inventory:
                print('You already have one!')
            else:
                inventory.append(get)
        else:
            print("Couldn't get item")
    
    if cmd == "highscore":
        readfile=open('./files/leaderboard.txt')
        lines=readfile.readlines()
        print("The current highscore is by...\n",(lines[0]),"and their score is...\n",(lines[1]),"seconds,\n if you beat it you get to be the highscorer for this computer \n")
        readfile.close()

         

if wintype == "death":
    os.system("cls")
    print("You died")
    time.sleep(10)
if wintype == "winner":
    os.system("cls")
    print("\n\n*******************************************************\n\n")
    print("CONGRATULATIONS, you found the",win," in ",steps,"steps !!!")
    print("\n\n*******************************************************\n\n")
    end = time.time()   
    readfile=open('./files/leaderboard.txt')
    lines=readfile.readlines()
    elapsed = end - start
    if float(elapsed) < float(lines[1]):
        name = lines[0]
        time = lines[1]
        print("You have beaten the highscorer of ",name,", they had a score of ",time,"seconds")
        name = input("What is your name?")
        file = open("./files/leaderboard.txt" ,"w")
        file.write(name + "\n" + str(round(elapsed, 3)))
        file.close()
        readfile.close()
    else:
        print("Sorry, you did not beat the current highscorer,",(lines[0]))
    readfile.close()
    time.sleep(10)
