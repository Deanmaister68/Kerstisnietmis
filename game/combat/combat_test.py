import sys
sys.path.insert(1 , "game/")
playername= str (input("What is your name? >"))






while True:
    start =input("you wanne fight? y/n ")

    if start == "y":
        from combat1 import main
    else:
        print("to bad.")

    print('tester')
