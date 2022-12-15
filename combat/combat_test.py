#test for combat input to main file
playername= 8
if __name__ == "__main__":
    


    start =input("you wanne fight? y/n ")

    if start == "y":
        from combat1 import main
    else:
        print("to bad.")

    print('tester')
# conlusion it worked
