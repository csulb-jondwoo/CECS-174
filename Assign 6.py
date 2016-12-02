#Jon Ham
#CECS 174
invalid = True

while invalid:
    def menu():
        print("MacDoogle’s:\n"
              "1. Hamburger = $1.50\n"
              "2. Soda      = $1.15\n"
              "3. Fries     = $1.25\n"
              "4. Complete Order")
        return

    def userSelect():
        userInput = input("Enter your selection: ")
        invalid_2 = True
        while invalid_2:
            if userInput.isdigit():
                userInput = int(userInput)
                if userInput < 1 or userInput > 4:
                    print("Invalid entry.")
                else:
                    invalid_2 = False
        print()
        return userInput
