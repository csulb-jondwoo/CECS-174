#Jon Ham
#CECS 174

import random
invalid = True
money = 100
win = 0
lose = 0
percent = 0
played = 0

#begin loop
print("The Shell Game:")
while (invalid):
    print("1. Play \n2. Quit")
    userInput = input("Enter Option: ")
    #validate user input
    if userInput.isdigit():
        userInput = int(userInput)
        if userInput < 1 or userInput > 2:
            print("Invalid Input. Please try again")
        #play game
        elif userInput == 1:
            print("You have $"+str(money))
            #quit game due to no money
            if int(money) <= 0:
                print("You have lost all your money.")
                print("Thanks for playing!")
                print()
                print("Statistics - ")
                print("Games Played: ", played)
                print("Games Won: ", win)
                print("Games Lost: ", lose)
                percentage = (win / played) * 100
                print("You won", percentage, "% of the games.")
                invalid = False
            #continue game
            else:
                played += 1
                userBet = input("How much do you wanna bet? ")
                #validate user bet
                if userBet.isdigit():
                    userBet = int(userBet)
                    if userBet < 0 or userBet > int(money):
                        print("Invalid input. Please try again.")
                    #continue game
                    else:
                        print("   --\t\t--\t\t --")
                        print(" /\t  \   /\t   \   /\t\ ")
                        print("/   1  \ /\t 2  \ /\t  3  \ ")
                        compShell = random.randint(1, 3)
                        userGuess = input("Guess where the pebble is: ")
                        #validate user guess
                        if userGuess.isdigit():
                            userGuess = int(userGuess)
                            if userGuess < 1 or userGuess > 3:
                                print("Invalid input. Please try again.")
                            #continue game
                            else:
                                #placing shell randomly
                                if compShell == 1:
                                    print("   --\t\t--\t\t --")
                                    print(" /\t  \   /\t   \   /\t\ ")
                                    print("/   o  \ /\t    \ /\t     \ ")
                                elif compShell == 2:
                                    print("   --\t\t--\t\t --")
                                    print(" /\t  \   /\t   \   /\t\ ")
                                    print("/      \ /\t o  \ /\t     \ ")
                                elif compShell == 3:
                                    print("   --\t\t--\t\t --")
                                    print(" /\t  \   /\t   \   /\t\ ")
                                    print("/      \ /\t    \ /\t  o  \ ")
                                #win
                                if userGuess == compShell:
                                    print("You got lucky this time. \nYou win $"+str(userBet))
                                    money = int(money) + int(userBet)
                                    win += 1
                                #lose
                                else:
                                    print("Sorry, it was under shell",compShell)
                                    print("You lose $"+str(userBet))
                                    money = int(money) - int(userBet)
                                    lose += 1
        #quit game
        elif userInput == 2:
            #calculate stats if played more than once.
            if played > 0:
                print("Thanks for playing!")
                print()
                print("Statistics - ")
                print("Games Played: ",played)
                print("Games Won: ",win)
                print("Games Lost: ",lose)
                percentage = (win / played) * 100
                print("You won",int(percentage),"% of the games.")
                invalid = False
            #prints stats of 0.
            else:
                print("Thanks for playing!")
                print()
                print("Statistics - ")
                print("Games Played: 0")
                print("Games Won: 0")
                print("Games Lost: 0")
                print("You won 0% of the games.")
                invalid = False
    else:
        print("Invalid input. Please try again.")