import random
from os import system
import survey
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


def slot_machine():
    global hpearned
    global coinsearned
    """
    A simple slot machine mini-game.
    """
    global coinAmount
    global hpCount
    # Define the symbols for the slot machine
    symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "⭐"]

    # Display welcome message
    system("cls||clear")
    print("\n\033[1;37mSLOT MACHINE!!!!!!!\033[0m")
    print("Press Enter to spin...")
    input(">")

    # Spin the reels
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    # Display the result
    print(f"{reel1} | {reel2} | {reel3}")

    # Determine the result
    if reel1 == reel2 == reel3:
        print(
            "\033[1;32mCongratulations! You won! YOU HAVE RECEIVED A HEAVENLY POTION I AND SOME COINS AS YOUR REWARD!\033[0m"
        )
        hpCount += 1
        coinAmount += 200
        hpearned += 1
        coinsearned += 200
    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
        print("\033[1;32mYou got a small win! YOU HAVE RECEIVED SOME COINS AS YOUR REWARDS!\033[0m")
        coinAmount += 100
        coinsearned += 100
    else:
        print("\033[1;31mBetter luck next time!\033[0m")

    sleep(rollCooldown)

    # Offer to play again
    print("Do you want to play again?")
    choice = survey.routines.select(
        options=["YES", "NO", "HELP"],
    )
    if choice == 0:
        slot_machine()  # Recursively call slot_machine to play again

    if choice == 1:
        print("Thanks for playing!")
        input("Press Enter to continue....")

    if choice == 2:
        currencyHelp()


def currencyHelp():
    system("cls||clear")
    print("The game has one type of expendable currency : Coins!")
    sleep(2)
    print("You can earn coins by playing the slot machine.")
    sleep(2)
    print("You will win if either two or all slots match up.")
    input("Press Enter to continue.....")
