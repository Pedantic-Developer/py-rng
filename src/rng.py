import random
import time
from time import sleep
from os import system
import survey._routines
import os
import sys
import survey

import saveload
import crafting
import inventory
import devices
import minigames
import weather


rollCount = 0
coinAmount = 0
hpCount = 0
hp2count = 0
obCount = 0
luckDeviceCrafted = 0
cdDeviceCrafted = 0
ldequipped = 0
cddequipped = 0
rollCooldown = 1.5
hpearned = 0
coinsearned = 0
playerName = ""
name = ""
width = 40
height = 10
ch = ""
currentWeather = ""

# TITLES + POTION TITLES

titles = {
    "Common": [
        "Common",
        "Uncommon",
        "Rare",
        "Divinus",
        "Crystallised",
        "Ash",
        "Wind",
        "Magnetic",
        "Siderum",
        "Hazard",
    ],
    "Uncommon": [
        "Aquatic",
        "Gravitational",
        "Quartz",
        "Lost Soul",
        "Jade",
        "Bounded",
        "StarRider",
        "Stormal",
        "Hazard : RAYS",
    ],
    "Rare": [
        "CELESTIAL",
        "GALAXY",
        "ELECTRIC",
        "ARCANE",
        "VIRTUAL",
        "ASTRAL",
        "Stormal : HURRICANE",
        "Bounded : UNBOUND",
        "EXOTIC",
        "TWILIGHT",
    ],
    "Legendary": [
        "HYPER - VOLT",
        "STARSCOURGE",
        "SAILOR",
        "MATRIX",
        "CHROMATIC",
        "ETHEREAL",
        "TWILIGHT : IRIDESCENT MEMORY",
    ],
    "Mythical": [
        "ARCHANGEL",
        "BLOODLUST",
        "IMPEACHED",
        "ABYSSALHUNTER",
        "SAILOR : DUTCHMAN",
        "EXOTIC : APEX",
        "CHROMATIC : GENESIS",
        "STARSCOURGE : RADIANT",
        "MATRIX : OVERDRIVE",
    ],
}
hp1titles = {
    "Uncommon": [
        "Aquatic",
        "Gravitational",
        "Quartz",
        "Jade",
        "Bounded",
        "StarRider",
        "Stormal",
        "Hazard : RAYS",
    ],
    "Rare": [
        "CELESTIAL",
        "GALAXY",
        "ELECTRIC",
        "ARCANE",
        "VIRTUAL",
        "ASTRAL",
        "Stormal : HURRICANE",
        "Bounded : UNBOUND",
        "EXOTIC",
    ],
}
hp2titles = {
    "Rare": [
        "CELESTIAL",
        "GALAXY",
        "ELECTRIC",
        "ARCANE",
        "VIRTUAL",
        "ASTRAL",
        "Stormal : HURRICANE",
        "Bounded : UNBOUND",
        "EXOTIC",
    ],
    "Legendary": [
        "STARSCOURGE",
        "SAILOR",
        "MATRIX",
        "CHROMATIC",
        "ETHEREAL",
        "TWILIGHT : IRIDESCENT MEMORY",
    ],
}
obtitles = {
    "Legendary": [
        "STARSCOURGE",
        "SAILOR",
        "MATRIX",
        "CHROMATIC",
        "ETHEREAL",
        "TWILIGHT : IRIDESCENT MEMORY",
    ],
    "Mythical": [
        "ARCHANGEL",
        "BLOODLUST",
        "IMPEACHED",
        "ABYSSALHUNTER",
        "SAILOR : DUTCHMAN",
        "EXOTIC : APEX",
        "CHROMATIC : GENESIS",
        "STARSCOURGE : RADIANT",
        "MATRIX : OVERDRIVE",
    ],
}

# RARITY THRESHOLDS

rarity_thresholds = {
    "Common": (0, 75000),
    "Uncommon": (75001, 85000),
    "Rare": (85001, 99000),
    "Legendary": (99001, 99998),
    "Mythical": (99999, 100000),
}

hp1rar = {"Uncommon": (0, 65), "Rare": (66, 100)}

hp2rar = {"Rare": (0, 60), "Legendary": (71, 100)}

obrar = {"Legendary": (0, 60), "Mythical": (61, 100)}

# MENUS


def startMenu():
    global playerName
    global ch
    system("cls||clear")
    print("""\033[1m\033[1;36m 
          :::::::::             :::   :::                      :::::::::                   ::::    :::                   :::::::: 
         :+:    :+:            :+:   :+:                      :+:    :+:                  :+:+:   :+:                  :+:    :+: 
        +:+    +:+             +:+ +:+                       +:+    +:+                  :+:+:+  +:+                  +:+         
       +#++:++#+               +#++:                        +#++:++#:                   +#+ +:+ +#+                  :#:          
      +#+                      +#+                         +#+    +#+                  +#+  +#+#+#                  +#+   +#+#    
     #+#                      #+#                         #+#    #+#                  #+#   #+#+#                  #+#    #+#     
    ###                      ###                         ###    ###                  ###    ####                   ########\033[0m\033[0m
\n""")

    print("Welcome to PY RNG! A Random Number Generator with an element of gambling?")
    print("IF IT IS YOUR FIRST TIME PLAYING, PLEASE DON'T LOAD YOUR SAVE!\n\n")

    while True:
        ent = survey.routines.select(
            options=["\033[1mPLAY\033[0m", "\033[1mQUIT\033[0m"],
        )
        if ent == 0:
            system("cls||clear")
            print("Entering Game...")
            sleep(1)
            print("Would you like to load your save?")

            sav = survey.routines.select(
                options=["YES", "NO"],
            )

            if sav == 0:
                saveload.load()
                mainMenu()

            if sav == 1:
                print("Enter your Name:")
                playerName = input(">")
                print(
                    "Initialize the inventory by checking it as soon as you get to the main menu(only for the first time!)."
                )
                input("Press Enter to continue.....")
                mainMenu()

        if ent == 1:
            system("cls||clear")
            print("Are you sure?")

            sur = survey.routines.select(
                options=["YES", "NO"],
            )

            if sur == 0:
                print("D:")
                sleep(2)
                print("owie")
                sleep(1)
                exit()

            if sur == 1:
                print(":D")
                sleep(2)


def mainMenu():
    while True:
        system("cls||clear")
        print("""\033[1;32m
$$\      $$\           $$\                 $$\      $$\                               
$$$\    $$$ |          \__|                $$$\    $$$ |                              
$$$$\  $$$$ | $$$$$$\  $$\ $$$$$$$\        $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\   $$\ 
$$\$$\$$ $$ | \____$$\ $$ |$$  __$$\       $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |  $$ |
$$ \$$$  $$ | $$$$$$$ |$$ |$$ |  $$ |      $$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |
$$ |\$  /$$ |$$  __$$ |$$ |$$ |  $$ |      $$ |\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$$ |$$ |$$ |  $$ |      $$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  |
\__|     \__| \_______|\__|\__|  \__|      \__|     \__| \_______|\__|  \__| \______/ \033[0m
\n\n\n""")
        ch = survey.routines.select(
            "\033[1mWhat would you like to do?\033[0m",
            options=[
                "\033[1mCHECK ROLL COUNT\033[0m",
                "\033[1mCHECK INVENTORY\033[0m",
                "\033[1mCHECK POTION STORAGE\033[0m",
                "\033[1mEQUIPMENT\033[0m",
                "\033[1mVEGAS?!\033[0m",
                "\033[1mCRAFT\033[0m",
                "\033[1mROLL\033[0m",
                "\033[1mSAVE\033[0m",
                "\033[1mCREDITS\033[0m",
                "\033[1mQUIT\033[0m",
            ],
        )

        if ch == 0:
            print("\033[1;33mYour roll count is:\033[0m", rollCount)
            input("Press Enter to continue...")

        elif ch == 2:
            storage()

        elif ch == 3:
            equipment()

        elif ch == 1:
            # Initialize Inventory
            inventory.populate_inventory(titles)
            # Display the inventory
            inventory.display()

        elif ch == 5:
            craft()

        elif ch == 6:
            while True:
                print("Do you want to roll?")
                z = survey.routines.select(options=["YES", "NO"])

                if z == 0:
                    roll()

                if z == 1:
                    break

        elif ch == 4:
            vegas()

        elif ch == 8:
            display_credits()

        elif ch == 9:
            system("cls||clear")
            print("owie D:")
            sleep(2)
            exit()

        elif ch == 7:
            saveload.save()

        # uncomment for devmenu + legacy main menu :D
        """print("CHECK ROLL COUNT")
        print("CHECK INVENTORY")
        print("CHECK POTION STORAGE")
        print("EQUIPMENT")
        print("VEGAS?!")
        print("CRAFT")
        print("ROLL")
        print("SAVE")
        print("QUIT")
        print("\n")
        print("What would you like to do?")
        ch = input(">").lower()
        
        if ch in ["rc", "rollcount", "count"]:
            print("Your roll count is:", rollCount)
            input("Press Enter to continue...")


        elif ch in ["s", "ps", "storage"]:
            storage()

        elif ch in ["e" , "equip", "equipment"]:
            equipment()

        elif ch in ["inv", "inventory", "i"]:
            populate_inventory(titles)
            # Display the inventory
            display(inventory)

        elif ch in ["c", "craft"]:
            craft()
        
        elif ch in ["r", "roll"]:
            while True:
                print("Do you want to roll?")
                z = input(">")

                if z in ["y", "yes"]:
                    roll()

                elif z in ["n", "no"]:
                    break

        elif ch in ["vegas", "v"]:
            slot_machine()

        elif ch in ["oof", "kill", "exit"]:
            system("cls||clear")
            print("owie D:")
            sleep(2)
            exit() 
        
        elif ch in ["h", "help"]:
            mainMenuHelp()


        elif ch in ["whatareyou?"]:
            system("cls||clear")
            sleep(1)
            sleep(2) 
            print("PY RNG is a game that uses a Random Number Generator to give the player titles or auras based on the rarity of the number generated")
            sleep(2)
            print("or in other words, its just gambling without the money or losing!")
            sleep(3)
            input("Press Enter to continue.....")


        elif ch in ["save"]:
            save()


        elif ch in ["dev"]:
            devMode()

        
        elif ch in ["credits", "cr"]:
            display_credits()


        else:
            print("Please enter a valid option!")"""


# BACK TO MENUS


def storage():
    while True:
        system("cls||clear")
        print("""\033[1m
                   /$$                                                                                    
                  | $$                                                                                    
  /$$$$$$$       /$$$$$$          /$$$$$$         /$$$$$$         /$$$$$$         /$$$$$$         /$$$$$$ 
 /$$_____/      |_  $$_/         /$$__  $$       /$$__  $$       |____  $$       /$$__  $$       /$$__  $$
|  $$$$$$         | $$          | $$  \ $$      | $$  \__/        /$$$$$$$      | $$  \ $$      | $$$$$$$$
 \____  $$        | $$ /$$      | $$  | $$      | $$             /$$__  $$      | $$  | $$      | $$_____/
 /$$$$$$$/        |  $$$$/      |  $$$$$$/      | $$            |  $$$$$$$      |  $$$$$$$      |  $$$$$$$
|_______/          \___/         \______/       |__/             \_______/       \____  $$       \_______/
                                                                                 /$$  \ $$                
                                                                                |  $$$$$$/                
                                                                                 \______/                 \033[0m""")
        print("\033[1;32mYou have", hpCount, "Heavenly I Potion(s)\033[0m")
        print("\033[1;32mYou have", hp2count, "HEAVENLY II POTION(S)\033[0m")
        print("\033[1;32mYou have", obCount, "OBLIVION POTION(S)\033[0m\n\n")
        print("What do you want to use?:")

        cho = survey.routines.select(
            "\033[1mWhat would you like to use?",
            options=[
                "\033[1mHEAVENLY I POTION\033[0m",
                "\033[1mHEAVENLY II POTION\033[0m",
                "\033[1mOBLIVION POTION\033[0m",
                "\033[1mQUIT\033[0m",
            ],
        )

        if cho == 0:
            hpI()

        if cho == 1:
            hpII()

        if cho == 2:
            ob()

        if cho == 3:
            return


def craft():
    system("cls||clear")

    print("""\033[1m\033[94m
 ______     ______     ______     ______   ______   __     __   __     ______    
/\  ___\   /\  == \   /\  __ \   /\  ___\ /\__  _\ /\ \   /\ "-.\ \   /\  ___\   
\ \ \____  \ \  __<   \ \  __ \  \ \  __\ \/_/\ \/ \ \ \  \ \ \-.  \  \ \ \__ \  
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\      \ \_\  \ \_\  \ \_\\"\_\  \ \_____\ 
  \/_____/   \/_/ /_/   \/_/\/_/   \/_/       \/_/   \/_/   \/_/ \/_/   \/_____/ 
                                                                                 \033[0m\033[0m""")
    print("\033[1;32mPOTIONS:\033[0m")
    print("""\033[1;32mHEAVENLY II POTION:
              CONUSMES: 2x HEAVENLY I POTION
                        2x CELESTIAL
                        200x COINS\033[0m""")
    print("\n")
    print("""\033[1;32mOBLIVION POTION:
              CONSUMES: 5x HEAVENLY II POTION
                        1x CHROMATIC
                        1000x COINS\033[0m""")
    print("\n")
    print("\033[1;35mDEVICES:\033[0m")
    print("""\033[1;35mLUCK DEVICE:
              CONSUMES: 100x  Divinus
                        20x  Jade
                        10x   EXOTIC
                        2000x COINS\033[0m""")
    print("\n")
    print("""\033[1;35mTHE DEVICE OF THE WIND:
              CONSUMES: 150x Wind
                        25x  Stormal
                        15x  Stormal : HURRICANE
                        4000x Coins\033[0m""")
    print("\n")
    print("\033[1;33mYou currently have :", coinAmount, "coins. \033[0m")
    print("What would you like to craft?")
    op = survey.routines.select(
        options=[
            "\033[1mHEAVENLY POTION II\033[0m",
            "\033[1mOBLIVION POTION\033[0m",
            "\033[1mLUCK DEVICE\033[0m",
            "\033[1mDEVICE OF THE WIND\033[0m",
            "\033[1mQUIT\033[0m",
        ],
    )

    if op == 0:
        crafting.hpIIcr()

    if op == 1:
        crafting.obcr()

    if op == 2:
        crafting.luckDeviceCr()

    if op == 3:
        crafting.cdDeviceCr()

    if op == 4:
        return


def equipment():
    system("cls||clear")
    print("""\033[1m\033[1;34m$$$$$$$$\                     $$\                                               $$\     
$$  _____|                    \__|                                              $$ |    
$$ |       $$$$$$\  $$\   $$\ $$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  $$$$$$\   
$$$$$\    $$  __$$\ $$ |  $$ |$$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ \_$$  _|  
$$  __|   $$ /  $$ |$$ |  $$ |$$ |$$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  $$ |  $$ |    
$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |  $$ |  $$ |$$\ 
$$$$$$$$\ \$$$$$$$ |\$$$$$$  |$$ |$$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ $$ |  $$ |  \$$$$  |
\________| \____$$ | \______/ \__|$$  ____/ \__| \__| \__| \_______|\__|  \__|   \____/ 
                $$ |              $$ |                                                  
                $$ |              $$ |                                                  
                \__|              \__|                                                  \033[0m\033[0m\n""")
    print("\033[1;33mLUCK DEVICE : A device that boosts the wearer's luck!\033[0m")
    print("\033[1;33mDEVICE OF THE WIND : A device that harnesses the power of the wind, making the wearer faster!\033[0m")
    if cdDeviceCrafted == 0:
        print("YOU DO NOT OWN THE DEVICE OF THE WIND!")
    if luckDeviceCrafted == 0:
        print("YOU DONT OWN THE LUCK DEVICE!")

    print("\n")

    print("\033[1mEQUIPPED:\033[0m")
    if ldequipped == 1:
        print("\033[0;37mLuck Device is Equipped!\033[0m")
    if cddequipped == 1:
        print("\033[0;37mDevice of the Wind is Equipped!\033[0m")

    if ldequipped == 0 and cddequipped == 0:
        print("None")

    print("\n")

    print("What would you like to use?")

    eh = survey.routines.select(
        options=["\033[1mLUCK DEVICE\033[0m", "\033[1mDEVICE OF THE WIND\033[0m", "\033[1mQUIT\033[0m"],
    )

    if eh == 0:
        devices.luckDevice()

    if eh == 1:
        devices.cdDevice()

    if eh == 2:
        return


def vegas():
    system("cls||clear")
    print("""\033[93m\033[1m                                                                           
                                                                           
$$\    $$\        $$$$$$\         $$$$$$\         $$$$$$\         $$$$$$$\ 
\$$\  $$  |      $$  __$$\       $$  __$$\        \____$$\       $$  _____|
 \$$\$$  /       $$$$$$$$ |      $$ /  $$ |       $$$$$$$ |      \$$$$$$\  
  \$$$  /        $$   ____|      $$ |  $$ |      $$  __$$ |       \____$$\ 
   \$  /         \$$$$$$$\       \$$$$$$$ |      \$$$$$$$ |      $$$$$$$  |
    \_/           \_______|       \____$$ |       \_______|      \_______/ 
                                 $$\   $$ |                                
                                 \$$$$$$  |                                
                                  \______/                                 \033[0m\033[0m""")
    print("\n")
    vch = survey.routines.select(
        "\033[1mWhat would you like to do?\033[0m",
        options=["\033[1mSPIN THE REELS!\033[0m", "\033[1mCHECK REWARDS EARNED\033[0m", "\033[1mQUIT\033[0m"],
    )
    if vch == 0:
        minigames.slot_machine()

    if vch == 1:
        print("\033[1;33mSo far you have won\033[0m:")
        print(f"\033[1;33m   COINS\033[0m : {coinsearned}")
        print(f"\033[1;33m   HEAVENLY I POTIONS\033[0m : {hpearned}")
        input("Press Enter to continue.....")

    if vch == 2:
        return


# ALL ROLL FUNCTIONS


def get_random_number():
    return random.randint(1, 100000)


def get_rarity(number):
    for rarity, (low, high) in rarity_thresholds.items():
        if low <= number <= high:
            return rarity
    return "Common"


def get_title(rarity):
    return random.choice(titles[rarity])


def roll():
    global rarity_thresholds
    global rollCooldown
    system("cls||clear")

    print("""\033[1m\033[1;35m
                                 /$$       /$$
                                | $$      | $$
  /$$$$$$         /$$$$$$       | $$      | $$
 /$$__  $$       /$$__  $$      | $$      | $$
| $$  \__/      | $$  \ $$      | $$      | $$
| $$            | $$  | $$      | $$      | $$
| $$            |  $$$$$$/      | $$      | $$
|__/             \______/       |__/      |__/ \033[0m\033[0m
\n\n\n""")
    weatherChange()
    random_number = get_random_number()
    rarity = get_rarity(random_number)
    title = get_title(rarity)

    if title in titles["Mythical"]:
        congratulations()

    print(f"\033[1;33mYou Rolled : {title} \033[0m")

    inventory.add(title, 1)
    global rollCount
    rollCount += 1
    sleep(rollCooldown)


def hpI():
    global hpCount

    def get_random_number():
        return random.randint(1, 100)

    def hp1getrar(number):
        for rarity, (low, high) in hp1rar.items():
            if low <= number <= high:
                return rarity
        return "Common"

    def hp1title(rarity):
        return random.choice(hp1titles[rarity])

    def hp1roll():
        random_number = get_random_number()
        rarity = hp1getrar(random_number)
        title = hp1title(rarity)
        print("You Rolled", title)
        global rollCount
        rollCount += 1
        inventory.add(title, 1)

    if hpCount > 0:
        print("YOU USED ONE HEAVENLY I POTION AND:")
        hp1roll()
        hpCount -= 1
    else:
        print("YOU DO NOT HAVE ANY HEAVENLY I POTIONS")
    input("Press Enter to continue...")


def hpII():
    global hp2count

    def get_random_number():
        return random.randint(1, 100)

    def hp2getrar(number):
        for rarity, (low, high) in hp2rar.items():
            if low <= number <= high:
                return rarity
        return "Common"

    def hp2title(rarity):
        return random.choice(hp2titles[rarity])

    def hp2roll():
        random_number = get_random_number()
        rarity = hp2getrar(random_number)
        title = hp2title(rarity)
        print("You Rolled", title)
        global rollCount
        rollCount += 1
        global hp2count
        hp2count -= 1
        inventory.add(title, 1)

    if int(hp2count) > 0:
        print("\033[1;32mYOU USED ONE HEAVENLY II POTION AND:\033[0m")
        hp2roll()
    else:
        print("\033[1;31mYOU DO NOT HAVE ANY HEAVENLY II POTIONS\033[0m")
    input("Press Enter to continue...")


def ob():
    global obCount

    def get_random_number():
        return random.randint(1, 100)

    def obgetrar(number):
        for rarity, (low, high) in obrar.items():
            if low <= number <= high:
                return rarity
        return "Common"

    def obtitle(rarity):
        return random.choice(obtitles[rarity])

    def obroll():
        random_number = get_random_number()
        rarity = obgetrar(random_number)
        title = obtitle(rarity)
        print("You Rolled", title)
        global rollCount
        rollCount += 1
        inventory.add(title, 1)

    if obCount > 0:
        print("\033[1;32mYOU USED ONE OBLIVION POTION AND:\033[0m")
        congratulations()
        obroll()
        obCount -= 1
    else:
        print("\033[1;31mYOU DO NOT HAVE ANY OBLIVION POTIONS\033[0m")

    input("Press Enter to continue...")


# GIVE FUNCTIONS


def givehp():
    global rollCount
    global hpCount
    if rollCount % 1000 == 0:
        print("YOU HAVE ROLLED A THOUSAND TIMES.....")
        sleep(2)
        print("YOU SHALL RECEIVE A HEAVENLY I POTION FOR YOUR EFFORTS!")
        sleep(2)
        global hpCount
        hpCount += 1


def devInvEdit():
    global inventory
    print("What title would you like to modify?")
    name = input(">")
    print("Set new value:")
    quantity = int(input(">"))
    if name in inventory:
        inventory[name] = quantity
        print(f"Set '{name}' to quantity : '{quantity}'")
        input("Press Enter to continue")

    else:
        print(f"Adding a new title : {name}, do you want to proceed?")
        a = input(">")
        if a in ["yes", "y"]:
            inventory[name] = quantity
        else:
            print("Returning to dev menu.....")


# DEV MENU


def devMode():
    global coinAmount
    global hpCount
    global hp2count
    global obCount

    while True:
        system("cls||clear")

        print("====== DEVELOPER MENU ======")
        print("VIEW INVENTORY")
        print("ADD TITLE TO INVENTORY")
        print("INVENTORY MANIPULATION")
        print("STORAGE MANIPULATION")
        print("VIEW CURRENT RARITY THRESHOLDS")
        print("VIEW CURRENT COOLDODWN TIME")
        print("BACK TO MAIN MENU")
        print("What do you want to do?")
        choi = input(">").lower()

        if choi == "view":
            inventory.populate_inventory(titles)
            # Display the inventory
            inventory.display(inventory)

        elif choi == "add":
            print("What would you like to add?")
            name = input(">")
            print(f"Quantity of {name}?")
            quantity = int(input(">"))
            inventory.add(name, quantity)

        elif choi == "iman":
            devInvEdit()

        if choi == "man":
            print("What would you like to change?")
            print("COIN")
            print("HPI")
            print("HPII")
            print("OB")
            m = input(">").lower()
            if m == "coin" or m == "c":
                print("Enter new value:")
                coinAmount = int(input(">"))

            elif m == "hp":
                print("Enter new value:")
                hpCount = int(input(">"))

            elif m == "hp2":
                print("Enter new value")
                hp2count = int(input(">"))

            elif m == "ob":
                print("Enter new value")
                obCount = int(input(">"))

            else:
                print("Please enter a valid choice.")
                sleep(2)
                devMode()

        elif choi == "rar":
            print(rarity_thresholds)
            input("Press Enter to continue.....")

        elif choi == "cd":
            print(rollCooldown)
            input("Press Enter to continue.....")

        elif choi == "help":
            devMenuHelp()

        elif choi == "mm":
            print("Going back to Main Menu!")
            sleep(2)
            mainMenu()


# ANIMATION STUFF


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_bouncing_text(text, x, y):
    # Create a frame with empty spaces
    frame = [[" " for _ in range(width)] for _ in range(height)]

    # Place the text in the frame
    for i, char in enumerate(text):
        if 0 <= x + i < width and 0 <= y < height:
            frame[y][x + i] = char

    # Print the frame
    for row in frame:
        print("".join(row))
    print("\n" * 2)  # Extra space below the animation


def congratulations():
    text = "Congratulations"
    height = 10
    x = 0
    y = height // 2
    dx = 1
    dy = 1

    for i in range(50):
        clear_screen()
        print_bouncing_text(text, x, y)

        # Update the position
        x += dx
        y += dy

        # Bounce off the walls
        if x + len(text) >= width or x < 0:
            dx *= -1
        if y >= height or y < 0:
            dy *= -1

        time.sleep(0.10)


def print_scrolling_text(text, delay=0.1, width=40):
    """
    Prints scrolling text in a terminal window.

    :param text: The text to be scrolled.
    :param delay: The delay between frames to control the speed of scrolling.
    :param width: The width of the text area to display.
    """
    # Prepare the text to scroll
    lines = text.splitlines()
    scrolling_text = " ".join(lines)
    padding = " " * width
    full_text = padding + scrolling_text + padding

    # Calculate the number of iterations needed
    max_position = len(full_text) - width

    # Scrolling effect loop
    while True:
        for position in range(max_position):
            sys.stdout.write("\r" + full_text[position : position + width])
            sys.stdout.flush()
            time.sleep(delay)
        # Break the loop if needed (e.g., for demonstration purposes)
        break

def weatherChange():
    global currentWeather
    w = False
    if rollCount == 0:
        w = False
    if rollCount % 60 == 0:
        w = True

    if rollCount % 60 != 0:
        w = False

    if w:
        weather.weather()

    print("THE WEATHER CURRENTLY IS:", currentWeather)


def display_credits():
    """
    Displays the credits screen with a scrolling text effect.
    """
    # Prepare the credits text
    system("cls||clear")
    credits_text = """\033[1;36m
CREDITS:
LEAD PROGRAMMER:
AAKASH KRISHNASAMY

SPECIAL THANKS TO:
AADARSH MADAN KOLLAN AND
ILESH KEDHARANATH THIADA\033[0m 
"""
    # Call the scrolling text function
    print_scrolling_text(credits_text, delay=0.1, width=40)

    # End the scrolling and wait for user input
    input("\nPress Enter to continue.....")


# HELP FUNCTIONS


def currencyHelp():
    system("cls||clear")
    print("The game has one type of expendable currency : Coins!")
    sleep(2)
    print("You can earn coins by playing the slot machine.")
    sleep(2)
    print("You will win if either two or all slots match up.")
    input("Press Enter to continue.....")


def mainMenuHelp():
    system("cls||clear")
    print("Type in the first letter or the entire word for the action you want to")
    sleep(2)
    print("(for example : To Check Inventory --> inv or inventory or i).")
    sleep(2)
    print("If the menu refreshes, it means that you have entered an invalid input.")
    sleep(2)
    input("Press Enter to continue.....")


def storageHelp():
    system("cls||clear")
    print(
        "Type in either the numbers to use the potions or their abbreviations to use them"
    )
    sleep(2)
    print("(for example : To use a Heavenly Potion II --> 2 or hp2).")
    sleep(2)
    input("Press Enter to continue.....")


def craftingHelp():
    system("cls||clear")
    print("Type in the abbreviation of whatever you want to craft")
    sleep(2)
    print("(for example : To craft an Oblivion Potion --> op).")
    sleep(2)
    input("Press Enter to continue.....")


def equipmentHelp():
    system("cls|clear")
    print("If you have crafted the devices, they will show up here.")
    sleep(2)
    print("If you want to equip/unequip something, just input the abbreviation of it.")
    sleep(2)
    print("(for example : To equip device of the wind --> dotw)")
    sleep(2)
    input("Press Enter to continue.....")


def devMenuHelp():
    system("cls||clear")
    print("It's a dev menu...")
    sleep(2)
    print("Only Developers are allowed to be here....")
    sleep(2)
    print("you're going to be booted from the game now lol")
    sleep(2)
    print("regretting not saving huh?")
    sleep(2)
    system("cls||clear")
    print(">:-D  muahahaha")
    exit()


# STARTING THE GAME!

startMenu()
