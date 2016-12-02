# Jon Ham
# CECS 174

#################
import random

invalid = True


##################

# Displays empty board
def displayBoard():
    print("  A B C D E")
    board = []

    for i in range(0, 5):
        board.append(["-"] * 6)

    board[0][0] = "1"
    board[1][0] = "2"
    board[2][0] = "3"
    board[3][0] = "4"
    board[4][0] = "5"

    for j in board:
        print(" ".join(j))


######################################################################################################
# displays random board
def resetBoard():
    board_2 = []
    for k in range(0, 5):
        board_2.append(["-"] * 6)
    randomRow = random.randint(0, 3)
    randomCol = random.randint(1, 4)
    board_2[0][0] = "1"
    board_2[1][0] = "2"
    board_2[2][0] = "3"
    board_2[3][0] = "4"
    board_2[4][0] = "5"
    # set random coordinates
    board_2[randomRow][randomCol] = "*"
    board_2[randomRow + 1][randomCol + 1] = "*"
    board_2[randomRow][randomCol + 1] = "*"
    board_2[randomRow + 1][randomCol] = "*"
    return board_2


######################################################################################################
def displayMenu():
    print()
    print("Menu\n"
          "1. Fire Shot\n"
          "2. Show Solution\n"
          "3. Quit")


######################################################################################################
def getMenuInput():
    invalid_2 = True
    while invalid_2:
        user_input = input("Enter your selection: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input < 1 or user_input > 3:
                print("Invalid entry")
                print()
            else:
                invalid_2 = False
        else:
            print("Invalid Entry")
            print()
        return user_input


######################################################################################################
def getRow():
    invalid_row = True
    while invalid_row:
        user_row = input("Enter a Row Number: ")
        if user_row.isdigit():
            user_row = int(user_row)
            if user_row < 1 or user_row > 5:
                print("Invalid Entry")
                print()
            else:
                # necessary because index is from 0-4 not 1-5
                user_row -= 1
                invalid_row = False
                return user_row
        else:
            print("Invalid Entry")
            print()


######################################################################################################
def getCol():
    invalid_col = True
    while invalid_col:
        user_col = input("Enter a Column Letter: ")
        if user_col.isdigit():
            print("Invalid Entry")
            print()
        elif user_col < "a" or user_col > "e":
            print("Invalid Entry")
            print()
        else:
            # convert Column letter to int
            if user_col == "a":
                user_col = 1
            elif user_col == "b":
                user_col = 2
            elif user_col == "c":
                user_col = 3
            elif user_col == "d":
                user_col = 4
            elif user_col == "e":
                user_col = 5
            invalid_col = False
            return user_col


######################################################################################################
def fireShot(user_row, user_col, board_2, board):
    print()
    if board_2[user_row][user_col] == "*":
        print("  A B C D E")

        board[user_row][user_col] = "*"
        for i in board:
            print(" ".join(i))
        return board
    elif board[user_row][user_col] == "X" or board[user_row][user_col] == "*":
        print("Coordinate already entered.")
        print("  A B C D E")
        for i in board:
            print(" ".join(i))
        return board
    else:
        print("  A B C D E")

        board[user_row][user_col] = "X"
        for i in board:
            print(" ".join(i))
        return board


######################################################################################################
while invalid:
    displayBoard()
    invalid_cont = True
    board_2 = resetBoard()

    board = []
    for i in range(0, 5):
        board.append(["-"] * 6)

    board[0][0] = "1"
    board[1][0] = "2"
    board[2][0] = "3"
    board[3][0] = "4"
    board[4][0] = "5"
    while invalid_cont:
        displayMenu()
        user_input = getMenuInput()
        if user_input == 1:
            user_row = getRow()
            user_col = getCol()
            board = fireShot(user_row, user_col, board_2, board)
            # win condition
            count = 0
            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    if board[i][j] == "*":
                        count += 1
            print(count)
            if count == 4:
                print("You win!")
                print()
                print("New game")
                invalid_cont = False
        # show solution
        elif user_input == 2:
            print()
            print("Solution: ")
            print(" A B C D E")
            for i in board_2:
                print(" ".join(i))
            print()
            print("New Game!")
            invalid_cont = False
        # quit
        elif user_input == 3:
            print("Goodbye!")
            invalid_cont = False
            invalid = False

