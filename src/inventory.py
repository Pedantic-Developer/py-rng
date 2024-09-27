from time import sleep
from os import system
from tabulate import tabulate
import pickle

rollCount = 0
inv = {}
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


def add(name, quantity):
    """
    Adds an item to the inventory with the specified name and quantity.
    If the item already exists, it updates the quantity.
    """
    if name in inv:
        inv[name] += quantity
    else:
        inv[name] = quantity
    print(f"\033[1;37mAdded {quantity} of '{name}' to your inventory.\033[0m")


def editInventory(name, quantity, minAmt):
    """
    Adds an item to the inventory with the specified name and quantity.
    If the item already exists, it updates the quantity.
    """
    if name in inv:
        if inv[name] - quantity < 0:
            print(f"\033[1;31mYou dont have enough of {name} to proceed.\033[0m ")
            return False
        else:
            inv[name] -= quantity
            print(f"\033[1;31mRemoved {quantity} of {name} from your inventory\033[0m")
            return True
    else:
        print(f"You dont have enough of {name} to proceed")
        input("Press Enter to continue.....")


def devInvEdit():
    global inv
    print("What title would you like to modify?")
    name = input(">")
    print("Set new value:")
    quantity = int(input(">"))
    if name in inv:
        inv[name] = quantity
        print(f"Set '{name}' to quantity : '{quantity}'")
        input("Press Enter to continue")

    else:
        print(f"Adding a new title : {name}, do you want to proceed?")
        a = input(">")
        if a in ["yes", "y"]:
            inv[name] = quantity
        else:
            print("Returning to dev menu.....")


def saveInventory(filename="inventory.pkl"):
    """
    Saves the inventory dictionary to a file.
    """
    with open(filename, "wb") as f:
        pickle.dump(inv, f)

    print(f"Inventory saved to '{filename}'.")


def loadInventory(filename="inventory.pkl"):
    """
    Loads the inventory dictionary from a file.
    """
    global inv
    try:
        with open(filename, "rb") as f:
            inv = pickle.load(f)
        print(f"Inventory loaded from '{filename}'.")

    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")


COLORS = {
    "Common": "\033[94m",  # Blue
    "Uncommon": "\033[93m",  # Yellow
    "Rare": "\033[92m",  # Green
    "Legendary": "\033[95m",  # Magenta
    "Mythical": "\033[91m",  # Red
    "RESET": "\033[0m",  # Reset to default color
}


def populate_inventory(titles):
    """
    Populate the inventory with titles based on the rarity categories.
    Used to initialize the inventory.
    """
    for category, title_list in titles.items():
        for title in title_list:
            add(title, 0)  # Add each title with a default quantity of 0


def display():
    """
    Displays all items in the inventory along with their quantities in a neat table with color coding.
    """
    if not inv:
        print("The inventory is empty.")
    else:
        system("cls||clear")
        print("""\033[1m
 ______  __    __  __     __  ________  __    __  ________   ______   _______   __      __ 
/      |/  \  /  |/  |   /  |/        |/  \  /  |/        | /      \ /       \ /  \    /  |
$$$$$$/ $$  \ $$ |$$ |   $$ |$$$$$$$$/ $$  \ $$ |$$$$$$$$/ /$$$$$$  |$$$$$$$  |$$  \  /$$/ 
  $$ |  $$$  \$$ |$$ |   $$ |$$ |__    $$$  \$$ |   $$ |   $$ |  $$ |$$ |__$$ | $$  \/$$/  
  $$ |  $$$$  $$ |$$  \ /$$/ $$    |   $$$$  $$ |   $$ |   $$ |  $$ |$$    $$<   $$  $$/   
  $$ |  $$ $$ $$ | $$  /$$/  $$$$$/    $$ $$ $$ |   $$ |   $$ |  $$ |$$$$$$$  |   $$$$/    
 _$$ |_ $$ |$$$$ |  $$ $$/   $$ |_____ $$ |$$$$ |   $$ |   $$ \__$$ |$$ |  $$ |    $$ |    
/ $$   |$$ | $$$ |   $$$/    $$       |$$ | $$$ |   $$ |   $$    $$/ $$ |  $$ |    $$ |    
$$$$$$/ $$/   $$/     $/     $$$$$$$$/ $$/   $$/    $$/     $$$$$$/  $$/   $$/     $$/   \033[0m  
                                                                                           
                                                                                           
                                                                                           """)

        # Prepare the table data with color coding
        table_data = []
        for name, quantity in inv.items():
            # Determine the category based on the title
            category = None
            for cat, titles_list in titles.items():
                if name in titles_list:
                    category = cat
                    break
            color = COLORS.get(category, COLORS["RESET"])
            table_data.append([f"{color}{name}{COLORS['RESET']}", quantity])

        headers = ["Item", "Quantity"]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        sleep(0.5)

    input("\nPress Enter to return back to Main Menu..... ")
