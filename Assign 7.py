#Jon Ham
#CECS 174

import random
invalid = True

def menu_choice():
    print("Menu:\n"
          "  1. Play Game\n"
          "  2. Show Score\n"
          "  3. Quit")
    user_selection = input("Enter selection: ")
    invalid_2 = True
    while invalid_2:
        if user_selection.isdigit():
            user_selection = int(user_selection)
            invalid_2 = False
            if user_selection < 1 or user_selection > 3:
                print("Invalid Entry.")
                print()
            else:
                invalid_2 = False
                print()
        else:
            print("Invalid Entry.")
    return user_selection

def weapon_choice():
    print("Choose your weapon:\n"
          "  R. Rock\n"
          "  P. Paper\n"
          "  S. Scissors\n"
          "  L. Lizard\n"
          "  K. Spock")
    user_selection = input("Weapon: ")
    invalid_3 = True
    while invalid_3:
        if user_selection.isalpha():
            invalid_3 = False
            if user_selection != "R" and user_selection != "P" and user_selection != "S" and user_selection != "L" and user_selection != "K":
                print("Invalid Entry")
                print()
            else:
                invalid_3 = False
                print()
        else:
            print("Invalid Entry.")
            print()
    return user_selection

def comp_choice():
    comp_weapon = random.randint(1,5)
    if comp_weapon == 1:
        comp_weapon = "Rock"
    elif comp_weapon == 2:
        comp_weapon = "Paper"
    elif comp_weapon == 3:
        comp_weapon = "Scissors"
    elif comp_weapon == 4:
        comp_weapon = "Lizard"
    elif comp_weapon == 5:
        comp_weapon = "Spock"
    return comp_weapon

def compare(user_weapon, comp_weapon):
    print("You chose", user_weapon)
    print("Computer chose", comp_weapon)
    if user_weapon == "Rock" and comp_weapon == "Rock":
        return "Tie"
    elif user_weapon == "Paper" and comp_weapon == "Rock":
        return "You win!"
    elif user_weapon == "Scissors" and comp_weapon == "Rock":
        return "Computer wins"
    elif user_weapon == "Lizard" and comp_weapon == "Rock":
        return "Computer wins"
    elif user_weapon == "Spock" and comp_weapon == "Rock":
        return "You win!"

    elif user_weapon == "Rock" and comp_weapon == "Paper":
        return "You Win!"
    elif user_weapon == "Paper" and comp_weapon == "Paper":
        return "Tie"
    elif user_weapon == "Scissors" and comp_weapon == "Paper":
        return "Computer wins"
    elif user_weapon == "Lizard" and comp_weapon == "Paper":
        return "You win!"
    elif user_weapon == "Spock" and comp_weapon == "Paper":
        return "Computer wins"

    elif user_weapon == "Rock" and comp_weapon == "Scissors":
        return "You Win!"
    elif user_weapon == "Paper" and comp_weapon == "Scissors":
        return "Computer wins"
    elif user_weapon == "Scissors" and comp_weapon == "Scissors":
        return "Tie"
    elif user_weapon == "Lizard" and comp_weapon == "Scissors":
        return "Computer wins!"
    elif user_weapon == "Spock" and comp_weapon == "Scissors":
        return "You win!"

    elif user_weapon == "Rock" and comp_weapon == "Lizard":
        return "You Win!"
    elif user_weapon == "Paper" and comp_weapon == "Lizard":
        return "Computer wins"
    elif user_weapon == "Scissors" and comp_weapon == "Lizard":
        return "You Win!"
    elif user_weapon == "Lizard" and comp_weapon == "Lizard":
        return "Tie"
    elif user_weapon == "Spock" and comp_weapon == "Lizard":
        return "Computer wins"

    elif user_weapon == "Rock" and comp_weapon == "Spock":
        return "Computer wins"
    elif user_weapon == "Paper" and comp_weapon == "Spock":
        return "You win!"
    elif user_weapon == "Scissors" and comp_weapon == "Spock":
        return "Computer wins"
    elif user_weapon == "Lizard" and comp_weapon == "Spock":
        return "You win!"
    elif user_weapon == "Spock" and comp_weapon == "Spock":
        return "Tie"

def show_score():
    print("FIXME")
    #pass in count_user
    #pass in count_comp

def quit():
    print("FIXME")
    #pass in count_user
    #pass in count_comp

while invalid:
    user_menu_choice = menu_choice()
    if user_menu_choice == 1:
        user_weapon_choice = weapon_choice()
        if user_weapon_choice == "R":
            user_weapon_choice = "Rock"
        elif user_weapon_choice == "P":
            user_weapon_choice = "Paper"
        elif user_weapon_choice == "S":
            user_weapon_choice = "Scissors"
        elif user_weapon_choice == "L":
            user_weapon_choice = "Lizard"
        elif user_weapon_choice == "K":
            user_weapon_choice = "Spock"
        comp_weapon = comp_choice()
        print(compare(user_weapon_choice, comp_weapon))
        print()
    elif user_menu_choice == 2:
        print("FIXME")
    elif user_menu_choice == 3:
        print("FIXME")
        invalid = False
