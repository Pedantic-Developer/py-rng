import pickle
from time import sleep
import inventory

rollCount = 0
# inventory = {}
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


def save():
    """Saves all current values of all variables to a savefile"""
    global coinAmount
    global hpCount
    global hp2count
    global rollCount
    global obCount
    global playerName
    global data
    global ldequipped
    global deviceCrafted
    data = {
        "hpcount": hpCount,
        "hp2count": hp2count,
        "obcount": obCount,
        "rollcount": rollCount,
        "name": playerName,
        "coinamount": coinAmount,
        "ld": luckDeviceCrafted,
        "ldeq": ldequipped,
        "cd": cdDeviceCrafted,
        "cdeq": cddequipped,
        "vhp": hpearned,
        "vco": coinsearned,
    }
    with open("savefile", "wb") as f:
        pickle.dump(data, f)
    inventory.saveInventory()
    print("\033[1;36mYOU HAVE SAVED SUCCESSFULLY\033[0m")
    sleep(2)


def load():
    """Loads game variables from a savefile."""
    global coinAmount
    global hpCount
    global hp2count
    global rollCount
    global obCount
    global name
    global ldequipped
    global luckDeviceCrafted
    global cdDeviceCrafted
    global cddequipped
    global hpearned
    global coinsearned
    with open("savefile", "rb") as f:
        data = pickle.load(f)
        coinAmount = int(data["coinamount"])
        hpCount = int(data["hpcount"])
        hp2count = int(data["hp2count"])
        rollCount = int(data["rollcount"])
        obCount = int(data["obcount"])
        name = data["name"]
        luckDeviceCrafted = int(data["ld"])
        ldequipped = int(data["ldeq"])
        cdDeviceCrafted = int(data["cd"])
        cddequipped = int(data["cdeq"])
        hpearned = int(data["vhp"])
        coinsearned = int(data["vco"])
    inventory.loadInventory()
    print("\033[1;36mLOADED SUCCESSFULLY\033[0m")

    sleep(2)
