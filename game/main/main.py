from colorama import Fore, Back, Style
import sys
sys.path.insert(1 , "game/")


print(Fore.CYAN + "???:" " What is you're name traveller?")
from player.playername import inputplayername


print( Fore.CYAN + "???: " "HAHAHA. " + inputplayername + "? so it is you? I expect great things from you peasant.")
print( Fore.CYAN + "???: " + " I will so you soon young traveller...\n Now wake up!")
print( Fore.MAGENTA + "narator: You are in a tavern. You look around and see a few tables with some empty seats")
print( Fore.MAGENTA + "narator: You see a man behind the bar. He is about 6 feet with grey hair and a slim fesyke")
print( Fore.MAGENTA + "narator: You walk to the man and start speaking.")
from NPC import barkeeper


