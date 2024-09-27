import random
from time import sleep

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




def weather():
    global currentWeather
    b = random.randint(1, 5)
    print("\033[1mThe weather seems to change.....\033[0m")
    sleep(1)

    if b == 1:
        print("\033[1;32mWINDY: TREES SWAY TO THE WIND, YOU FEEL REFRESHED.\033[0m")
        currentWeather = "WINDY"

    elif b == 2:
        print(
            "\033[1mSNOWY: COLD WHITE SNOW COVERS YOUR SURROUNDINGS, WAIT IS THE SNOW YELLOW???!!!\033[0m"
        )
        currentWeather = "SNOWY"

    elif b == 3:
        print("\033[1;34mRAINY: VERY WET INDEED!\033[0m")
        currentWeather = "RAINY"

    elif b == 4:
        print(
            "\033[1;33mSUNNY: IT IS NICE AND BRIGHT, YOU WOULD ENJOY IT MORE IF YOU COULD STOP SWEATING SO MUCH.\033[0m"
        )
        currentWeather = "SUNNY"

    sleep(1)
