#main.py

import pets
import random

print("Virtual Turtle")
print("                            ___-------___\n"
      "                        _-~~             ~~-_\n"
      "                      _-~                    /~-_\n"
"   /^\__/^\         /~  \                   /    \ \n"
" /|  O|| O|        /      \_______________/        \ \n"
"| |___||__|      /       /                \          \ \n"
"|          \    /      /                    \          \ \n"
"|   (_______) /______/                        \_________ \ \n"
"|         / /         \                      /            \ \n"
" \         \^\\         \                  /               \     /\n"
"   \         ||           \______________/      _-_       //\__//\n"
"     \       ||------_-~~-_ ------------- \ --/~   ~\    || __/\n"
"       ~-----||====/~     |==================|       |/~~~~~\n"
"        (_(__/  ./     /                    \_\      \.\n"
"             (_(___/                         \_____)_)\n")

turtle = pets.Pet(input("What do you want to name your turtle? "), random.randint(1,2))
name = turtle.get_name()
print("Your turtle's name is now",name+".")
print()

def print_attributes():
    print("Attributes")
    print("-----------")
    print("Hunger:\t\t ", "+ " + format("-" * turtle.get_hunger(), "10s") + " +")
    print("Cleanliness: ", "+ " + format("-" * turtle.get_cleanliness(), "10s") + " +")
    print("Affinity:\t ", "+ " + format("-" * turtle.get_affinity(), "10s") + " +")
    print("Loyalty:\t ", "+ " + format("-" * turtle.get_loyalty(), "10s") + " +")
    print("Happiness:\t ", "+ " + format("-" * turtle.get_happiness(), "10s") + " +")

def menu():
    print()
    print("Virtual Turtle")
    print("--------------")
    print("1. Feed your turtle\n"
          "2. Clean your turtle\n"
          "3. Play with your turtle\n"
          "4. Train your turtle\n"
          "5. Pet your turtle\n"
          "6. Quit")
    print()

def food_menu():
    print("1. Breakfast\n"
          "2. Lunch\n"
          "3. Dinner")
    print()

def check_inputs():
    user_input = 0
    invalid_input = True
    while invalid_input:
        user_input = input("Enter your selection: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input < 1 or user_input > 6:
                print("Input not within range.")
                print()
            else:
                invalid_input = False
        else:
            print("Input is not a digit.")
            print()
    return user_input

def check_food_inputs():
    invalid_input = True
    while invalid_input:
        user_input = input("Enter your selection: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input < 1 or user_input > 3:
                print("Input not within range.")
                print()
            else:
                invalid_input = False
        else:
            print("Input is not a digit.")
            print()
        return user_input
##########################################################################################################################################################################
invalid = True
while invalid:
    print_attributes()
    menu()
    user_input = check_inputs()
    random_action = random.randint(0,1)
    invalid_random_action = True
    while invalid_random_action:
        if user_input == 1:
            invalid_food_choice = True
            while invalid_food_choice:
                food_menu()
                food_input = check_food_inputs()
                if food_input == 1:
                    if random_action == 1:
                        print(name,"did not eat the food.")
                        print()
                        invalid_food_choice = False
                        invalid_random_action = False
                    else:
                        turtle.feed()
                        turtle.check_values()
                        if turtle.get_hunger() == 3:
                            print(name,"is getting full.")
                            print()
                        elif turtle.get_hunger() == 2:
                            print(name,"is full. Stop feeding",turtle.get_gender()+"!")
                            print()
                        elif turtle.get_hunger() == 1:
                            print(name,"is suffering from over eating.")
                            print()
                        elif turtle.get_hunger() == 0:
                            print(name,"has died. Do not force feed your pet.")
                            print()
                            invalid_food_choice = False
                            invalid = False
                        else:
                            while turtle.get_hunger() > 3:
                                print(name,"thanks you for the food :-).")
                                print()
                                break
                        invalid_random_action = False
                        invalid_food_choice = False
                        print()
                elif food_input == 2:
                    if random_action == 1:
                        print(name,"did not eat the food.")
                        print()
                        invalid_food_choice = False
                        invalid_random_action = False
                    else:
                        turtle.feed()
                        turtle.feed()
                        turtle.check_values()
                        if turtle.get_hunger() == 3:
                            print(name,"is getting full.")
                            print()
                        elif turtle.get_hunger() == 2:
                            print(name,"is full. Stop feeding",turtle.get_gender()+"!")
                            print()
                        elif turtle.get_hunger() == 1:
                            print(name,"is suffering from over eating.")
                            print()
                        elif turtle.get_hunger() == 0:
                            print(name,"has died. Do not force feed your pet.")
                            print()
                            invalid_food_choice = False
                            invalid = False
                        else:
                            while turtle.get_hunger() > 3:
                                print(name,"thanks you for the food :-).")
                                print()
                                break
                        invalid_random_action = False
                        invalid_food_choice = False
                        print()
                elif food_input == 3:
                    if random_action == 1:
                        print(name,"did not eat the food.")
                        print()
                        invalid_food_choice = False
                        invalid_random_action = False
                    else:
                        turtle.feed()
                        turtle.feed()
                        turtle.feed()
                        turtle.check_values()
                        if turtle.get_hunger() == 3:
                            print(name,"is getting full.")
                            print()
                        elif turtle.get_hunger() == 2:
                            print(name,"is full. Stop feeding",turtle.get_gender()+"!")
                            print()
                        elif turtle.get_hunger() == 1:
                            print(name,"is suffering from over eating.")
                            print()
                        elif turtle.get_hunger() == 0:
                            print(name,"has died. Do not force feed your pet.")
                            print()
                            invalid_food_choice = False
                            invalid = False
                        else:
                            while turtle.get_hunger() > 3:
                                print(name,"thanks you for the food :-).")
                                print()
                                break
                        invalid_random_action = False
                        invalid_food_choice = False
                        print()
        elif user_input == 2:
            if random_action == 1:
                print(name,"does not want to be cleaned right now.")
                print()
                invalid_random_action = False
            else:
                turtle.clean()
                turtle.check_values()
                while turtle.get_cleanliness() > 2 and turtle.get_cleanliness() != 10 and turtle.get_cleanliness() > 3:
                    print(name,"loves the feeling of dirt and grime being washed away.")
                    print()
                    break
                while turtle.get_cleanliness() == 10 and turtle.get_happiness() > 3:
                    print(name,"is already squeaky clean!")
                    print()
                    break
                if turtle.get_happiness() == 3:
                    print(name,"is getting tired of being cleaned.")
                    print()
                elif turtle.get_happiness() == 2:
                    print(name,"is getting annoyed.")
                    print()
                elif turtle.get_happiness() == 1:
                    print(name,"is fighting back but you continue to wash",turtle.get_gender(),"anyway.")
                    print()
                elif turtle.get_happiness() == 0:
                    print(name,"ran away. Do not over clean your pet.")
                    print()
                    invalid = False
                invalid_random_action = False
                print()

        elif user_input == 3:
            if random_action == 1:
                print(name,"does not want to play right now.")
                print()
                invalid_random_action = False
            else:
                turtle.play()
                turtle.check_values()
                while turtle.get_hunger() < 7 and turtle.get_cleanliness() > 2:
                    print(name,"loves playing with you!")
                    print()
                    break
                if turtle.get_cleanliness() == 2:
                    print(name,"has fleas! Clean",turtle.get_gender(),"more often!")
                    print()
                elif turtle.get_cleanliness() == 1:
                    print(name,"is suffering from a virus.")
                    print()
                elif turtle.get_cleanliness() == 0:
                    print(name,"has died. Do not neglect hygiene!")
                    print()
                    invalid = False
                invalid_random_action = False
                print()

                if turtle.get_hunger() == 7:
                    print(name,"is getting hungry.")
                    print()
                elif turtle.get_hunger() == 8:
                    print(name,"has no energy to play.")
                    print()
                elif turtle.get_hunger() == 9:
                    print(name,"is starving.")
                    print()
                elif turtle.get_hunger() == 10:
                    print(name,"has died. Do not forget to feed your pet.")
                    print()
                    invalid = False
                invalid_random_action = False
                print()

                print()
        elif user_input == 4:
            if random_action == 1:
                print(name,"does not want to listen right now.")
                print()
                invalid_random_action = False
            else:
                turtle.train()
                turtle.check_values()
                while turtle.get_cleanliness() > 2 and turtle.get_happiness() > 3:
                    print(name,"learns very well.")
                    print()
                    break

                if turtle.get_cleanliness() == 2:
                    print(name,"has fleas! Clean",turtle.get_gender(),"more often!")
                    print()
                elif turtle.get_cleanliness() == 1:
                    print(name,"is suffering from a virus.")
                    print()
                elif turtle.get_cleanliness() == 0:
                    print(name,"has died. Do not neglect hygiene!")
                    print()
                    invalid = False
                invalid_random_action = False
                print()

                if turtle.get_happiness() == 3:
                    print(name,"is getting tired training.")
                    print()
                elif turtle.get_happiness() == 2:
                    print(name,"is getting annoyed.")
                    print()
                elif turtle.get_happiness() == 1:
                    print(name,"is fighting back but you continue to train",turtle.get_gender(),"anyway.")
                    print()
                elif turtle.get_happiness() == 0:
                    print(name,"ran away. Do not force your pet to listen.")
                    print()
                    invalid = False
                invalid_random_action = False
                print()

        elif user_input == 5:
            if random_action == 1:
                print(name,"does not want to be touched right now.")
                print()
                invalid_random_action = False
            else:
                turtle.pet()
                turtle.check_values()
                while turtle.get_cleanliness() > 2:
                    print(name,"loves the soft touch of your hand.")
                    print()
                    break
                if turtle.get_cleanliness() == 2:
                    print(name,"has fleas! Clean",turtle.get_gender(),"more often!")
                    print()
                elif turtle.get_cleanliness() == 1:
                    print(name,"is suffering from a virus.")
                    print()
                elif turtle.get_cleanliness() == 0:
                    print(name,"has died. Do not neglect hygiene!")
                    print()
                    invalid = False
                invalid_random_action = False
                print()

        elif user_input == 6:
            print("Goodbye!")
            invalid = False
            print()


