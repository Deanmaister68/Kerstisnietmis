# Turn Based Battle Simulator

# Player and computer take turns to attack each other with different moves
# until one is defeated. 
import random
import sys
sys.path.insert(1 , "game/main")



def main():
    """Main function that will welcome the player to combat."""



    print("\nHow to play.\n\nPlayers take turn to choose a move. Moves can either deal moderate damage")
    print("with a low range, deal high damage but over a wide")
    print("range, or they can heal. (Note: Moves can miss, including Heal!)")



    

    # Set up the play again loop

    player_health = 100
    computer_health = 110

        # determine whose turn it is
    turn = random.randint(1,2) # heads or tails
    if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nPlayer will go first.")
    else:
            player_turn = False
            computer_turn = True
            print("\nDark elf will go first.")


    print("\nPlayer health: ", player_health, "Dark elf health: ", computer_health)

        # set up the main game loop
    while (player_health != 0 or computer_health != 0):

            heal_up = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            moves = {"Sword slash": random.randint(18, 25),
                     "Firebolt": random.randint(10, 35),
                     "Heal": random.randint(20, 25),
                     "Punch": random.randint(20, 27),
                     "poison bow": random.randint(15, 40),
                     "Heal": random.randint(20, 25)}

            if player_turn:
                print("\nPlease select a move:\n1. Sword slash (Deal damage between 18-25)\n2. Firebolt (Deal damage between 10-35)\n3. Heal (Restore between 20-25 health)\n")

                player_move = input("> ").lower()

                move_miss = random.randint(1,10) # 10% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0 # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "Sword slash"):
                        player_move = moves["Sword slash"]
                        print("\nYou used sword slash. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "firebolt "):
                        player_move = moves["Firebolt"]
                        print("\nYou used firebolt. It dealt ", player_move, " damage.")
                    elif player_move in ("3", "heal"):
                        heal_up = True # heal activated
                        player_move = moves["Heal"]
                        print("\nYou used Heal. It healed for ", player_move, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,10)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0 # the computer misses and deals no damage
                    print("The Dark elf missed!")
                else:
                    if computer_health > 30: 
                        if player_health > 75:
                            computer_move = moves["Punch"]
                            print("\nThe Dark elf used Punch. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75: # computer decides whether to go big or play it safe
                            imoves = ["Punch", "poison bow"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe Dark elf used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 35:
                            computer_move = moves["poison bow"] # FINISH HIM!
                            print("\nThe Dark elf used poison bow. It dealt ", computer_move, " damage.")                       
                    else: # if the computer has less than 30 health, there is a 30% chance they will heal
                        heal_or_fight = random.randint(3,10) 
                        if heal_or_fight == 1:
                            heal_up = True
                            computer_move = moves["Heal"]
                            print("\nThe Dark elf used Heal. It healed for ", computer_move, " health.")
                        else:
                            if player_health > 75:
                                computer_move = moves["Punch"]
                                print("\nThe Dark elf used Punch. It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Punch", "poison bow"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\nThe Dark elf used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 35:
                                computer_move = moves["poison bow"] # FINISH HIM!
                                print("\nThe Dark elf used poison bow. It dealt ", computer_move, " damage.")

            if heal_up:
                if player_turn:
                    player_health += player_move
                    if player_health > 100:
                        player_health = 100 # cap max health at 100. No over healing!
                else:
                    computer_health += computer_move
                    if computer_health > 100:
                        computer_health = 100
            else:
                if player_turn:
                    computer_health -= player_move
                    if computer_health < 0:
                        computer_health = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Dark elf"
                        break

            print("\nPlayer health: ", player_health, "Dark elf health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

    if winner == "Player":
            print("\nPlayer health: ", player_health, "Dark elf health: ", computer_health)
            print("\nCongratulations! You have won.")
    else:   #DONT FORGET TO AJUST THIS TO LET IT SHOW SLOWER AND SHOW COLOUR!!!!! 
            print("\nPlayer health: ", player_health, "Dark elf health: ", computer_health)
            print("\nSorry, but your opponent wiped the floor with you. Better luck next time.")
            print("................................................................................")
            print("................................................................................")
            print("................................................................................")
            print("???: Sow you lost... I thought you" "were thougher than this but weaklings dissepoint")
            print("???: But you wil get an other chance...")
            print("???: Restart your world and you will get your second chance... Dont waste it...")
            sys.exit()
main()