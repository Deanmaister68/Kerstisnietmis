#player name input in file is voor testing. ER UIT HALEN BIJ HET AFMAKEN VAN FILE!!!
Input_playername = ("dave")

from colorama import Fore, Back, Style

print(Fore.GREEN + "Barkeeper: Welcome to the Frozen Casket traveller. How can I be of service?")

drinks = input("Barkeeper: Would you like an ale? ")
if drinks == "yes":
    print("Barkeeper: Here you go!")
else:
    print("Barkeeper: Not someone who likes a nice ale are ya.")
    
print("Barkeeper: Well traveller, what is you're story?")

print(Fore.YELLOW + Input_playername + ": One day I was going for a walk in the woods till I heard a scream  coming from the house where me and hmy family lived. When I came back, I saw a horrific sight of my wife and children slaughtert by the orders of the evil king. Filled with rage I picked up an iron sword my father left me and started my quest of revenge. ")
