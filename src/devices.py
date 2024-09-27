# :D
from time import sleep
import survey

rollCount = 0
inventory = {}
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
rarity_thresholds = {
    "Common": (0, 75000),
    "Uncommon": (75001, 85000),
    "Rare": (85001, 99000),
    "Legendary": (99001, 99998),
    "Mythical": (99999, 100000),
}


def luckDevice():
    """A device that alters the rarity thresholds to increase chances of getting something rare."""
    global rarity_thresholds
    global ldequipped

    if luckDeviceCrafted == 1:
        if ldequipped == 1:
            print("\033[1mWould you like to unequip the Luck Device?\033[0m")
            ech = survey.routines.select(
                options=["YES", "NO"],
            )
            if ech == 0:
                ldequipped = 0

                rarity_thresholds = {
                    "Common": (0, 75000),
                    "Uncommon": (75001, 85000),
                    "Rare": (85001, 99000),
                    "Legendary": (99001, 99998),
                    "Mythical": (99999, 100000),
                }

                print("\033[1;31mYou have unequipped the Luck Device\033[0m")
                sleep(2)
                return

            if ech == 1:
                pass

        else:
            print("\033[1;32mYou have equipped the Luck Device!\033[0m")
            ldequipped = 1
            rarity_thresholds = {
                "Common": (0, 60000),
                "Uncommon": (60001, 75000),
                "Rare": (75001, 99000),
                "Legendary": (99001, 99880),
                "Mythical": (99881, 100000),
            }

            input("Press Enter to continue.....")

    else:
        print("\033[1;31mYou do not own the Luck Device!\033[0m")
        input("Press Enter to continue.....")


def cdDevice():
    """makes life easier"""
    global rollCooldown
    global cddequipped

    if cdDeviceCrafted == 1:
        if cddequipped == 1:
            print("\033[1mWould you like to uneqip the device?\033[0m")
            ech = survey.routines.select(
                options=["YES", "NO"],
            )
            if ech == 0:
                cddequipped = 0
                print("\033[1;31mYou have unequipped the Device of the Wind\033[0m")
                sleep(2)
                return
            if ech == 1:
                pass

        else:
            print("\033[1;32mYou have equipped the Device of the Wind!\033[0m")
            cddequipped = 1
            rollCooldown = 0.5
            input("Press Enter to continue.....")

    else:
        print("\033[1;31mYou do not own the Device of the Wind!\033[0m")
        input("Press Enter to continue.....")
