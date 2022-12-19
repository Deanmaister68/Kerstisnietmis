#enemy NPC ice slime's

from colorama import Fore, Back, Style



print (Fore.MAGENTA + "narrator:" + Fore.WHITE + "you see a very strange blob of What looks like slime")
fightslime = input ("\nyou see it killing a rat whit a stream of ice extending from it. its blocking you're path to go further. will you kill it?")
if fightslime == "yes":
    import sys
    sys.path.insert(1 , "game/combat/")
    from combat import combat1
else:
    print ("you ignore the slime and do not gain anything from it.")