#:D
from time import sleep
from os import system
import inventory

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


def hpIIcr():
    global hp2count
    global hpCount
    global coinAmount
    global inventory
    name = "CELESTIAL"
    if hpCount >= 2 and inventory.editInventory(name, 2, 2) and coinAmount >= 200:
        print("You have crafted: ONE HEAVENLY II POTION!")
        sleep(2)
        hp2count += 1
        coinAmount -= 200
        hpCount -= 2
        print("Press Enter to continue.....")

    else:
        print("You do not have the necessary materials to craft a HEAVENLY II POTION!")
        sleep(2)
        input("Press Enter to continue.....")


def obcr():
    global coinAmount
    global hp2count
    global obCount
    global inventory
    name = "CHROMATIC"
    if hp2count >= 5 and inventory.editInventory(name, 1, 1) and coinAmount >= 1000:
        print("You have crafted: ONE OBLIVION POTION!")
        sleep(2)
        obCount += 1
        coinAmount -= 1000
        hp2count -= 5
        print("Press Enter to continue.....")

    else:
        print("You do not have the necessary materials to craft an OBLIVION POTION!")
        sleep(2)
        input("Press Enter to continue.....")


def luckDeviceCr():
    global luckDeviceCrafted
    global coinAmount
    global inventory

    if luckDeviceCrafted == 1:
        print("You already own the Luck Device!")
        input("Press Enter to continue.....")

    else:
        system("cls|clear")
        name = "Divinus"
        if inventory.editInventory(name, 100, 100) and coinAmount >= 2000:
            name = "Jade"
            coinAmount -= 2000
            if inventory.editInventory(name, 20, 20):
                name = "EXOTIC"
                if inventory.editInventory(name, 10, 10):
                    print("You have crafeted the Luck Device!")
                    luckDeviceCrafted = 1
                    input("Press Enter to continue.....")


def cdDeviceCr():
    global cdDeviceCrafted
    global coinAmount
    global inventory

    if cdDeviceCrafted == 1:
        print("You alraedy own the Device of the Wind!")
        input("Press Enter to continue.....")

    else:
        system("cls|clear")
        name = "Wind"
        if inventory.editInventory(name, 150, 150) and coinAmount >= 4000:
            name = "Stormal"
            coinAmount -= 4000
            if inventory.editInventory(name, 30, 30):
                name = "Stormal : HURRICANE"
                if inventory.editInventory(name, 15, 15):
                    print("You have crafted the Device of the Wind")
                    cdDeviceCrafted = 1
                    input("Press Enter to continue.....")
