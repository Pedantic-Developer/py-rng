import random
import time
from time import sleep
import os
from crafting import *
from devices import *
from minigames import *
from saveload import *
from inventory import *
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
        weather()

    print("THE WEATHER CURRENTLY IS:", currentWeather)


def weather():
    global currentWeather
    b = random.randint(1, 5)
    print("The weather seems to change.....")
    sleep(1)

    if b == 1:
        print("WINDY: TREES SWAY TO THE WIND, YOU FEEL REFRESHED.")
        currentWeather = "WINDY"

    elif b == 2:
        print("SNOWY: COLD WHITE SNOW COVERS YOUR SURROUNDINGS, WAIT IS THE SNOW YELLOW???!!!")
        currentWeather = "SNOWY"

    elif b == 3:
        print("RAINY: VERY WET INDEED!")
        currentWeather = "RAINY"

    elif b == 4:
        print("SUNNY: IT IS NICE AND BRIGHT, YOU WOULD ENJOY IT MORE IF YOU COULD STOP SWEATING SO MUCH.")
        currentWeather = "SUNNY"

    sleep(1)