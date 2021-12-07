# the big bang theory - Rock, Paper, Scissors, Lizard, Spock

import os
import random
from time import sleep

def game(choice):
    computer_player = random.randint(1,5)
    print(">Rock")
    print(">Paper")
    print(">Scissors")
    print(">Lizard")
    print(">Spock")
    sleep(1)
    print(f"computer = {computer_player}-{options[computer_player]}, player = {choice}-{options[choice]}")
    sleep(1)
    if computer_player == choice:
        print("It's a draw")
        sleep(2)
    else:
        if choice == 1:
            if computer_player == 4:
                print(f"{rules[2]} - You Win!")
            elif computer_player == 3:
                print(f"{rules[9]} - You Win!")    
            elif computer_player == 2:
                print(f"{rules[1]} - I Won!")
            elif computer_player == 5:
                print(f"{rules[8]} - I Won!")
        elif choice == 2:
            if computer_player == 1:
                print(f"{rules[1]} - You Win!")
            elif computer_player == 5:
                print(f"{rules[7]} - You Win!")    
            elif computer_player == 3:
                print(f"{rules[0]} - I Won!")
            elif computer_player == 4:
                print(f"{rules[6]} - I Won!")
        elif choice == 3:
            if computer_player == 2:
                print(f"{rules[0]} - You Win!")
            elif computer_player == 4:
                print(f"{rules[5]} - You Win!")    
            elif computer_player == 5:
                print(f"{rules[4]} - I Won!")
            elif computer_player == 1:
                print(f"{rules[9]} - I Won!")
        elif choice == 4:
            if computer_player == 2:
                print(f"{rules[6]} - You Win!")
            elif computer_player == 5:
                print(f"{rules[3]} - You Win!")    
            elif computer_player == 3:
                print(f"{rules[5]} - I Won!")
            elif computer_player == 1:
                print(f"{rules[2]} - I Won!")        
        elif choice == 5:
            if computer_player == 3:
                print(f"{rules[4]} - You Win!")
            elif computer_player == 1:
                print(f"{rules[8]} - You Win!")    
            elif computer_player == 2:
                print(f"{rules[7]} - I Won!")
            elif computer_player == 4:
                print(f"{rules[3]} - I Won!")
        sleep(2)        
       
    print("Let's Play again!")
    sleep(2)
    main()

def main():
    os.system('clear')
    print("Welcome to RPLS v1.0 - Rock, Paper, Scissors, Lizard, Spock \n")
    print("Choose one:")
    print("1-Rock\n2-Paper\n3-Scissors\n4-Lizard\n5-Spock\n\n0-exit")
    try:
        choice = int(input(">>"))
    except:
        print("Please, choose a number.")
        sleep(2)
        return    
    if choice > 0 and choice <=5:
        game(choice)
    elif choice == 0:
        print("Come back Soon!")
        keep = "exit"
        return keep
    else:
        print("Please, choose a number.")
        sleep(2)
        return

rules = ['Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock vaporizes Rock', 'Rock crushes Scissors']

options = ["","Rock","Paper","Scissors","Lizard","Spock"]

keep = None

while keep != "exit":
    keep = main()
