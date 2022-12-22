from colorama import Fore, Back, Style
import sys
sys.path.insert(1 , "game/")


print(Fore.CYAN + "???:" " What is you're name traveller?")
from player.playername import inputplayername


print( Fore.CYAN + "???: " "HAHAHA. " + inputplayername + "? so it is you? I expect great things from you peasant.")
print( Fore.CYAN + "???: " + " I will see you soon young traveller...\n Now wake up!")
print( Fore.MAGENTA + "narator: You are in a tavern. You look around and see a few tables with some empty seats")
print( Fore.MAGENTA + "narator: You see a man behind the bar. He is about 6 feet with grey hair and a slim fesyke")
print( Fore.MAGENTA + "narator: You walk to the man and start speaking.")
from NPC import barkeeper

print( Fore.MAGENTA + "narator: While leaving the bar you follow the icey path up-hill towards the town ")
print( Fore.MAGENTA + "narator: It is freezing and to keep yourself warm you use you're ability to control fire as a way to warm up yourself ")
print( Fore.MAGENTA + "narator: You get close to the town and notice that the houses are frozen over and you can see parts of what used to be a busy town ")
print( Fore.MAGENTA + "narator: But there is something still living in the town")

#iceslime fight

print( Fore.MAGENTA + "narator: You killed the iceslime and think to yourself how many enemy's are there? ")
print( Fore.MAGENTA + "narator: you see a church tower sticking out over the other buildings and decide to go to it so you can explore more of the center of the town ")
print( Fore.MAGENTA + "narator: While closing in at the church there is a dead man laying at the front door ")
print( Fore.MAGENTA + "narator: He has a arrow in his back with a green vapor coming from it ")

#darkelf fight

print (Fore.MAGENTA + "narator: After the fight with the elf all you can think to yourself is")
print (Fore.YELLOW + "player: How does he corrupt them all? how did this get so badly out of hand")
print (Fore.MAGENTA + "narator: you hear a very loud HO HO HO! from the town hall")
print (Fore.MAGENTA + "narator: While walking to the town hall there is one last foe who shall needed to be defeated")

#jackfrost fight

print( Fore.CYAN + "???: " "HAHAHA. " + inputplayername + " I told you I would see you soon.")
print (Fore.YELLOW + "player: With terror you look at the monster Krampus as he asks you")
print( Fore.CYAN + "Krampus: " + inputplayername + " Did you really think santa the all holy would do this?")
print( Fore.CYAN + "???: " + inputplayername + " as long as santa is under my control there shall be war on mankind")

#bossfight