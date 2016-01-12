import time
import random
gold = 0
fishList = ['sockeye', 'sockeye', 'sockeye', 'chum', 'chum', 'chum', 'chum', 'pink', 'pink', 'king', 'coho', 'other', 'empty', 'storm']
fishDict = dict(sockeye = 0, chum=0, pink=0, king=0, coho = 0)

def main():
    start()

def start():
    print("Hello and Welcome to my game!")
    name = input("What's your name?    ")
    print("Welcome, {}.".format(name))
    print("The objective of this game is to fish for salmon. You win when you have 100 gold.")
    print("After collecting the salmon you sell them. Various types of salmon sell for different prices.")
    print("King are worth the most, then coho, sockeye, and chums. Pinks are worth the least.")
    choiceStart()
    fishing()

def ranFish():
    global gold
    fish =  fishList[random.randint(0,len(fishList)-1)]
    if fish == "empty":
        return "You came back empty handed..."
    if fish == 'other':
        return "You caught a crab. It pinched you and you dropped it back into the water. You came back empty handed..."
    if fish == 'storm':
        gold -= 2
        return "There was a storm. Your fishing pole got destroyed... You had to buy another one for 2 gold."
    else:
        fishDict[fish] = fishDict[fish] + 1
        return "You caught a {}!".format(fish)

def fishing():
    pick = ""
    while pick != "Y" and pick != "N":
        pick = input("Do you want to go fishing? Y/N    ").upper()
        if pick == "Y":
            time.sleep(1)
            print(ranFish())
            print("You currently have {} sockeyes, {} pinks, {} cohos, {} kings, and {} chums."\
            .format(fishDict['sockeye'], fishDict['pink'], fishDict['coho'], fishDict['king'], fishDict['chum']))
            fishing()
        if pick == "N":
            sellChoice()

def wincondition():
    global gold
    if gold >= 50:
        print("You win!\n")
        choiceRestart()
    else:
        fishing()

def begin():
    print("Let's get started!")

def sellChoice():
    sell = ""
    while sell != "Y" and sell != "N":
        print("You currently have {} in gold as well as {} sockeyes, {} pinks, {} cohos, {} kings, and {} chums."\
            .format(gold, fishDict['sockeye'], fishDict['pink'], fishDict['coho'], fishDict['king'], fishDict['chum']))
        sell = input("Do you want to sell your fish? Y/N    ").upper()
        if sell == "Y":
            selling()
        if sell == "N":
            fishing()

def selling():
    global gold
    gold += \
            + (fishDict['sockeye'] * 5)\
            + (fishDict['chum'] * 2)\
            + (fishDict['coho'] * 10)\
            + (fishDict['king'] * 15)\
            + (fishDict['pink'] * 1)
    fishDict['sockeye'] = 0
    fishDict['chum'] = 0
    fishDict['king'] = 0
    fishDict['coho'] = 0
    fishDict['pink'] = 0
    print("You now have {} in gold.".format(gold))
    wincondition()

def choiceStart():
    choice = ""
    while choice != "Y" and choice !="N":
        choice = input("Do you want to play? Y/N:    ").upper()
        if choice == "Y":
            begin()
        if choice == "N":
            print("Okay, bye...")

def choiceRestart():
    choice = ""
    while choice != "Y" and choice !="N":
        choice = input("Do you want to play again? Y/N:    ").upper()
        if choice == "Y":
            begin()
        if choice == "N":
            print("Okay, bye...")

if __name__ == '__main__': main()