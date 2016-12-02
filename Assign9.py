#Jon Ham
#CECS 174
###############################################################################################################################################################################################
import random
score = 0
question = 1
capitals = { "Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas":"Little Rock", "California":"Sacramento", "Colorado":"Denver", "Connecticut":"Hartford",
             "Delaware":"Dover", "Florida":"Tallahassee", "Georgia":"Atlanta", "Hawaii":"Honolulu", "Idaho":"Boise", "Illinois":"Springfield", "Indiana":"Indianapolis", "Iowa":"Des Moines",
             "Kansas":"Topeka", "Kentucky":"Frankfort", "Louisiana":"Baton Rouge", "Maine":"Augusta", "Maryland":"Annapolis", "Massachusetts":"Boston", "Michigan":"Lansing",
             "Minnesota":"St. Paul", "Mississippi":"Jackson", "Missouri":"Jefferson City", "Montana":"Helena", "Nebraska":"Lincoln", "Nevada":"Carson City", "New Hampshire":"Concord",
             "New Jersey":"Trenton", "New Mexico":"Santa Fe", "New York":"Albany", "North Carolina":"Raleigh", "North Dakota":"Bismarck", "Ohio":"Columbus", "Oklahoma":"Oklahoma City",
             "Oregon":"Salem", "Pennsylvania":"Harrisburg", "Rhode Island":"Providence", "South Carolina":"Columbia", "South Dakota":"Pierre", "Tennessee":"Nashville", "Texas":"Austin",
             "Utah":"Salt Lake City", "Vermont":"Montpelier", "Virginia":"Richmond", "Washington":"Olympia", "West Virginia":"Charleston", "Wisconsin":"Madison", "Wyoming":"Cheyenne" }

print("-State Capitals Quiz-")
###############################################################################################################################################################################################
## Gets random state
def getState(capitals):
    #convert capitals to list
    keys = list(capitals)
    #randomize list
    random.shuffle(keys)
    #print first element
    random_state = keys[:1]
    return random_state


## Gets 3 random capitals
def incorrectChoices(capitals):
    random_capital1 = " "
    random_capital2 = " "
    random_capital3 = " "
    #each variable can never equal each other
    while not (random_capital1 != random_capital2 != random_capital1):
        #converts capital values to list and assign to variable
        random_capital1 = random.choice(list(capitals.values()))
        random_capital2 = random.choice(list(capitals.values()))
        random_capital3 = random.choice(list(capitals.values()))
    return random_capital1, random_capital2, random_capital3


## Randomize choices
def randomizeChoices(capital1, capital2, capital3, random_state, capitals):
    #Convert list to str
    random_state = " ".join(random_state)
    correct_choice = capitals[random_state]
    #make list from given capitals and randomize
    list = [capital1, capital2, capital3, correct_choice]
    random.shuffle(list)
    random_list = list
    return random_list


## invalidations
def check_input():
    invalid_answer = True
    while invalid_answer:
        user_input = input("Enter your selection: ")
        if user_input.isalpha():
            #how to account for uppercase?
            if user_input < "a" or user_input > "d":
                print("Invalid Entry")
                print()
            else:
                invalid_answer = False
        else:
            print("Invalid Entry")
            print()
        return user_input

## check user's answer
def checkCorrect(user_input, random_state, capitals, random_capitals,):
    #convert random_state list to str
    random_state = "".join(random_state)
    #Convert user_input to capital
    if user_input == "a":
        user_input = random_capitals[0]
        if user_input == capitals[random_state]:
            print("Correct!")
            print()
            return True
        else:
            print("Incorrect")
            print("The answer is:",capitals[random_state])
            print()
            return False
    elif user_input == "b":
        user_input = random_capitals[1]
        if user_input == capitals[random_state]:
            print("Correct!")
            print()
            return True
        else:
            print("Incorrect")
            print("The answer is:",capitals[random_state])
            print()
            return False
    elif user_input == "c":
        user_input = random_capitals[2]
        if user_input == capitals[random_state]:
            print("Correct!")
            print()
            return True
        else:
            print("Incorrect")
            print("The answer is:",capitals[random_state])
            print()
            return False
    elif user_input == "d":
        user_input = random_capitals[3]
        if user_input == capitals[random_state]:
            print("Correct!")
            print()
            return True
        else:
            print("Incorrect")
            print("The answer is:",capitals[random_state])
            print()
            return False


###############################################################################################################################################################################################
while question < 11:
    random_state = getState(capitals)
    print(str(question)+". The capital of", " ".join(random_state), "is: ")
    capital1, capital2, capital3 = incorrectChoices(capitals)
    random_capitals = randomizeChoices(capital1, capital2, capital3, random_state, capitals)
    print("\t", end=" ")
    print("A.", random_capitals[0], end="")
    print("\t\tB.", random_capitals[1], end="")
    print("\t\tC.", random_capitals[2], end="")
    print("\t\tD.", random_capitals[3])
    user_input = check_input()
    invalid_2 = True
    while invalid_2:
        correct = checkCorrect(user_input, random_state, capitals, random_capitals)
        if correct == True:
            score += 1
            invalid_2 = False
        else:
            score = score
            invalid_2 = False
    question += 1
print("Your score is:",score)

##fix invalidation to stay at current q
##fix Uppercase selections

