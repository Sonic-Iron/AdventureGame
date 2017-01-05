#-*- coding:UTF-8 -*-
print("Use this in terminal")

#imports
import random, time, os, sys, shutil, getpass, threading, winsound
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
devmode = True

class refs: #All folders - please use this in the future
    class files:
        loc = 'Resources/'
        leaderboard = loc + 'leaderboard.txt'
    class sounds:
        loc = 'Resources/Sounds/'
        start = loc + 'start.py'
        win = loc + 'win.py'
    plugins = 'Plugins/'
    packs = 'Packs/'

def play_sound(address): #Play sound from file
    def launch(data):
        for sound in data:
            winsound.Beep(sound[0], sound[1]) #Freq, duration pair
    file = open(address)
    data = eval(file.read()) #Change from string to list by runnning it
    file.close()
    sound_thread = threading.Thread(name='Sound: ' + address, args=[data], target=launch, daemon=True)
    sound_thread.start() #Start thread so the sounds can play while the game is still running
play_sound(refs.sounds.start) #Play a sound

#Settings loader
file = open('settings.txt', 'r')
f = file.read().split('\n')
file.close()
for line in f:
    try:
        if not line == '':
            line = line.split(':')
            if line[0] == 'colour':
                os.system('color ' + line[1])
            elif line[0] == 'title':
                os.system('title ' + line[1] + '')
            elif line[0] == 'name':
                if line[1] == '@username':
                    name = getpass.getuser()
                else:
                    name = line[1]
    except:
        print('Settings: Error with line "' + line + '"') #Print error message

try: #Check if it has already been set by settings
    print('Name:', name)
except NameError:
    name = input("What is your name?")

#Plugin loader
plugins = {}
for plugin in os.listdir(refs.plugins):
    if not plugin.startswith('$') and plugin.endswith('.py'):
        file = open(refs.plugins + plugin, 'r')
        class new_plugin:
            exec(file.read())
        file.close()
        plugins[plugin] = new_plugin

#difficulty settings
difficulty = None
while not (difficulty == 'E' or difficulty == 'M' or difficulty == 'H'): #Go until the difficulty level is valid
    if not difficulty == None:
        print(difficulty, 'is not a diffulty level')
    difficulty = input("What is the difficulty? Easy[E], Medium[M] or Hard[H]\n").upper()

if difficulty == "E": #Interpret input
    energy = 150
    hunger = 150
    Work_seconds = 3
    sleep_seconds = 4
    monster_attack_rate = 3
    print('Easy difficulty selected')
elif difficulty == "M":
    energy = 100
    hunger = 100
    Work_seconds = 10
    sleep_seconds = 10
    monster_attack_rate = 2
    print('Medium difficulty selected')
elif difficulty == "H":
    energy = 50
    hunger = 50
    Work_seconds  = 15
    sleep_seconds = 15
    monster_attack_rate = 1
    print('Hard difficulty selected')

#setup
os.system("title AdventureGame")

if os.path.exists("__pycache__"): #remove cache
    shutil.rmtree("__pycache__")

#pack selector
files = os.listdir(refs.packs)
allfiles = []
for file in files:
    if file.endswith('.py') and not file == 'AdventureGameDefinitiveEdition.py' and not file.startswith('$'): #Is a python file
        allfiles.append(file)

if len(allfiles) == 0: #No packs - program can't run
    print('No packs')
    while True:
        input('') #Stop the user from progressing

elif len(allfiles) == 1: #Only one pack - choose it
    print('Only one pack (' + allfiles[0][:len(allfiles[0]) - 3] + ') - selecting that pack')
    mychoice = allfiles[0]
    myimport = mychoice
else:
    print('Packs (' + str(len(allfiles)) + '):') #Multiple packs - bring up the UI
    for file_num in range(len(allfiles)):
        print(str(file_num + 1) + ': ' + allfiles[file_num][:len(allfiles[file_num]) - 3])
    mychoice = -1
    while not -1 < mychoice < len(allfiles):
        try:
            mychoice = int(input('Type the number for the pack you want: ')) - 1
        except ValueError:
            mychoice = 0
            print('Autofill selected the first pack in the list for you')
    myimport = refs.packs + allfiles[mychoice]
libraryname = myimport[:len(myimport) - 3]

'''
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


chooseLibrary = "Which server do you want? 1-"+str(len(filelist))+" "
mychoice = input(chooseLibrary)
if mychoice == "":
    mychoice = 1

myimport = filelist[int(mychoice)-1]
lengthoffilename = len(myimport)
libraryname = myimport[0:lengthoffilename-3]

print(libraryname)

myimport = __import__(libraryname) #import data from chosen map
'''

#Map importer
class myimport:
    _file = open(refs.packs + libraryname + '.py', 'r') #_ makes variable hidden in autocomplete
    _contents = _file.read()
    _file.close()
    exec(_contents) #Run as normal code

#Link for names to old code
database = myimport.database
object_database = myimport.object_database
monster_database = myimport.monster_database
#sound_database = myimport.sound_database create #another database
#then just execute the sound you want to play
# so play_soundsound_database["win"] would play the 'win' sound
#is this too complicated though? 
#we would have to include the same names for the packs for the sounds that we make, unlike the monster, place and item databases where we can put what ever we want


for a in database:
    if "dependency" in database[a]:
        for b in database[a]["objects_in_building"]:
            if b not in itemcouldwin:
                itemcouldwin.append(b)
                
win = random.choice(itemcouldwin)

for place in database:
    if "dependency" in database[place]:
        ""
    else:
        if place not in couldstart:
            couldstart.append(place)

current_location = couldstart[random.randint(0,len(couldstart)-1)]


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
    print("You are at the", current_location)
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

    cont = True
    for plugin in plugins:
        try:
            plugin_continue = plugins[plugin].cmd_intercept(cmd)
            if not plugin_continue:
                cont = False
        except AttributeError:
            pass #Do nothing
    if not cont:
        continue #Contradictory, but this takes you back to the start of the loop
    
    if cmd == "look":
        print("Your location is", current_location)
        print(database[current_location]['description'])
        if len(database[current_location]['objects_in_building']) <= 0:
            print("\nThere's nothing else here")
        else:
            togo = None
            for plugin in plugins:
                try:
                    togo = plugins[plugin].format_list(database[current_location]['objects_in_building'])
                    break
                except AttributeError:
                    print(plugin)
            if togo == None:
                print("\nYou can see", database[current_location]['objects_in_building'])
            else:
                print("\nYou can see", togo)
           
    elif cmd == "move":
        print("Where would you like to move to?")
        togo = None
        for plugin in plugins:
            try:
                togo = plugins[plugin].format_list(database[current_location]['directions'])
                break
            except AttributeError:
                print(plugin)
        if togo == None:
            print("\nYou can see", database[current_location]['directions'])
        else:
            print("\nYou can see", togo)
        new_location = input("")
        if new_location not in database[current_location]['directions']: #Can't find location
           print("Can't go there...")
        else:
            if 'dependency' in (database[new_location]): 
                   if database[new_location]['dependency'] not in inventory:
                     print("You need", database[new_location]['dependency'], "to go there.") 
                   else:
                       x = random.randint(0,monster_attack_rate)
                       if x == 0:
                           keeys = list(monster_database.keys())
                           current_monster = random.choice(keeys)
                           print("You get attacked by", current_monster,)
                           print(monster_database[current_monster]["picture"])
                           what_to_do = input("Do you want to run or attack?")
                           if what_to_do == "attack":
                               for item in inventory:
                                #Add up the attack points for any object that has them
                                   if "attack" in object_database[item]:
                                       attack_strength = attack_strength + object_database[item]['attack']
                               print("Attack stength is", attack_strength)         
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
                                   print("You get defeated by the", current_monster, "and get tired")
                                   info()
                           elif what_to_do == "run":
                              energy = energy - 5
                              steps = steps + 1
                              print("You run back to your previous location and get slighly tired")
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
                    print("You get attacked by", current_monster)
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
                            print("You get defeated by the", current_monster, "and get tired")
                            info()
                    elif what_to_do == "run":
                        energy = energy - 5
                        steps = steps + 1
                        print("You run back to your previous location and get slighly tired")
                    else:
                        print("\nYou did not run away or fight the monster so you get defeated by it anyway")
                        energy = energy - monster_database[current_monster]["health"]
                                
                else:
                    current_location = new_location
                    steps += 1
                    energy = energy -10
                    info()
                

    elif cmd.startswith("pick up"):
        if cmd[8:len(cmd)] in database[current_location]["objects_in_building"]:
            picked_up_item = cmd[8:len(cmd)]
            if database[current_location]['type'] == "Selling_point":
                coins = coins - 1 
                inventory.append(picked_up_item)
                database[current_location]['objects_in_building'].remove(picked_up_item)
                print("Your inventory is", inventory)
                info()
            else:
                inventory.append(picked_up_item)
                database[current_location]['objects_in_building'].remove(picked_up_item)
                print("Your inventory is", inventory)    
            if picked_up_item == win:
                wintype = "winner"
                break

    elif cmd.startswith("drop"):
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
    elif cmd == "inventory":
        print(inventory)

    elif database[current_location]["type"] == "Work_point":
        if cmd == ("work"):
            print("You work for", Work_seconds, "hours")
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

    elif cmd == "sleep":
        sleepy = sleep_seconds
        print("You sleep for",sleep_seconds,"hours")
        while sleepy > 0:
            print(sleepy)
            sleepy = sleepy - 1
            time.sleep(1)
        print("You slept for",sleep_seconds,"hours and gained 15 energy")
        energy = energy +15
        info()

    elif cmd == "eat":
        print(inventory)  
        eat = input("What would you like to eat?")
        if eat not in inventory: 
            print("That item is not in your inventory")
        else:
            if object_database[eat]["type"] == "eat":
                print("You eat it, that was very refreshing!")
                hunger = hunger + 15
                inventory.remove(eat)
            else:
                print("That is not an ediable item\n")
                
    elif cmd == 'devmode':
        print('''Devmode help:
Enable by setting devmode to True

Commands:
examine item - see details for item
give item (also get) get an item
teleport (also tp) go to a location''')
    
    elif cmd == "examine item" and devmode:
        print(object_database)
        current_item = input ("Which item would you like to look at?")
        if current_item not in object_database:
            print("That item dosn't exist!")
        else:
            print(object_database[current_item]["description"])
            print("It has",object_database[current_item]["attack_points"]," attack points")

    elif (cmd == "give item" or ("get" in cmd)) and devmode:
        if cmd == "give item":
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
        elif "get " in cmd:
            if cmd[4:] in object_database:
                inventory.append(cmd[4:])
            else:
                print("That item is not avaliable")
        

    elif (cmd == "teleport" or cmd == 'tp') and devmode:
        for a in database:
            print(a)
        where = input("Where would you like to teleport to?")
        if where in database:
            current_location = where
    elif cmd == 'get' and devmode:
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
    
    elif cmd == "highscore":
        readfile=open(refs.files.leaderboard)
        lines=readfile.read().split('\n')
        print("The current highscore is held by", lines[0], "for", lines[1], "seconds, if you beat it you get to be the highscorer for this computer")
        readfile.close()

    elif cmd == 'end' and devmode:
        win_by = input('Exit through [D]eath or [I]tem?\n').lower()
        if win_by == 'd':
            wintype = 'death'
            break
        elif win_by == 'i':
            wintype = 'winner'
            break  
    else:
        print(cmd, 'not recognised')

    #Non commands
    if xp > 10:
        print("You leveled up one level")
        xp = 0 

    while len(inventory) > 5:
        print("You have more than 5 items")
        dropped_item = input("Which item would you like to drop?")
        if dropped_item not in inventory:
            print("That item is not in your inventory")
        else:
            database[current_location]["objects_in_building"].append(dropped_item)
            inventory.remove(dropped_item)

if wintype == "death":
    os.system("cls")
    print("You died!!")
if wintype == "winner":
    os.system("cls")
    play_sound(refs.sounds.win)
    winmessage = "CONGRATULATIONS, you found the " + str(win) + " in " + str(steps) + " steps !!!"
    filler = '*' * len(winmessage)
    print("\n\n" + filler + "\n\n")
    print(winmessage)
    print("\n\n" + filler + "\n\n")
    end = time.time()   
    elapsed = end - start
    file = open(refs.files.leaderboard, 'r')
    contents = file.read().split('\n')
    file.close()
    if elapsed < float(contents[1]):
        print('You got the new high score of',round(elapsed, 3),'seconds')
        file = open(refs.files.leaderboard, 'w')
        file.write(name + '\n' + str(round(elapsed, 3)))
        file.close()
        print('Saved to file')
    else:
        print('Too bad!', contents[0], 'still holds the high score of', contents[1],"seconds")

while True:
    time.sleep(0.5) #Keep window alive
