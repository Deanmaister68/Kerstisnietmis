from colorama import Fore, Back, Style

print(Fore.BLUE + "Barkeeper:" + Fore.WHITE + " Welcome to the Frozen Casket traveller. How can I be of service?")

drinks = input(Fore.BLUE + "Barkeeper:" + Fore.WHITE + " Would you like an ale? " + Fore.CYAN + "\nanswer ")
if drinks == "yes":
    print("\n" + Fore.BLUE + "Barkeeper:" + Fore.WHITE + " Here you go!")
else:
    print("\n" + Fore.BLUE + "Barkeeper:" + Fore.WHITE + " Not someone who likes a nice ale are ya.")
    
print(Fore.BLUE + "Barkeeper:" + Fore.WHITE + " Well traveller, what is you're story?")

print("\n" + Fore.YELLOW + Input_playername + Fore.WHITE +  ": One day I was going for a walk in the woods till I heard a scream  coming from the house where me and my family lived. When I came back, I saw a horrific sight of my wife and children slaughtert by the orders of the evil king. Filled with rage I picked up an iron sword my father left me and started my quest of revenge. ")

barkeepgift = input("\n" + Fore.BLUE + "Barkeeper:" + Fore.WHITE + "Im sorry for your los traveller. may i give you a gift? " + Fore.CYAN + "\nanswer ")
if barkeepgift == "yes":
    print(Fore.MAGENTA + "narrator:" + Fore.WHITE + " you received an healing item" + Fore.GREEN + "(green goo) " + Fore.WHITE + " use it to regenerate +5 procent of health")
else:
    print("I geus i will keep this healing item for myself than")

print(Fore.MAGENTA + "narrator:" + Fore.WHITE + "After you thank the barkeeper you move on with you're quest")