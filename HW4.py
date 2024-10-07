# Michael Herrmann
# COMP 4600
# February 16, 2022
#
# Tic-Tak-Toe
# 2 players should be able to play the game (both sitting at the same computer)
# • The board should be printed out every time a player makes a move
# • You should be able to accept input of the player position and then place a symbol
#   on the board
#       |       |
#   1   |   2   |   3
#       |       |
# -------------------------
#       |       |
#   4   |   5   |   6
#       |       |
# -------------------------
#       |       |
#   7   |   8   |   9
#       |       |

# Global list used to keep track of what has been used
boardValues = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Print the table and see if we have a winner, if we have a winner say winner and exit
def print_table(user_choice, user_symbol, player):
    # Convert the user symbol to uppercase
    user_symbol = user_symbol.upper()

    # See if space is available where user wants to go
    for num in range(len(boardValues)):
        if user_choice == boardValues[num]:
            boardValues[num] = user_symbol

    # Print the board
    print("      |       |")
    print(" ", boardValues[0], "  |  ", boardValues[1], "  |  ", boardValues[2])
    print("      |       |")
    print("-----------------------")
    print("      |       |")
    print(" ", boardValues[3], "  |  ", boardValues[4], "  |  ", boardValues[5])
    print("      |       |")
    print("-----------------------")
    print("      |       |")
    print(" ", boardValues[6], "  |  ", boardValues[7], "  |  ", boardValues[8])
    print("      |       |")

    # Checks to see if we have a winner, if we do say winner and exit program
    if (
            boardValues[0] == boardValues[1] and boardValues[0] == boardValues[2] or
            boardValues[0] == boardValues[3] and boardValues[0] == boardValues[6] or
            boardValues[0] == boardValues[4] and boardValues[0] == boardValues[8] or
            boardValues[1] == boardValues[4] and boardValues[1] == boardValues[7] or
            boardValues[2] == boardValues[4] and boardValues[2] == boardValues[6] or
            boardValues[2] == boardValues[5] and boardValues[2] == boardValues[8] or
            boardValues[3] == boardValues[4] and boardValues[3] == boardValues[5] or
            boardValues[6] == boardValues[7] and boardValues[6] == boardValues[8]
    ):
        print(player, "is the WINNER!")
        exit(1)


# Start of the "main" program
print_table(0, 'o', "Default")
# Count used to see if
tie = True

# Allows each player to go 4 times
for i in range(1, 5):
    player1Choice = input("Select a spot player 1: ")
    print_table(player1Choice, 'x', "Player 1")
    player2Choice = input("Select a spot player 2: ")
    print_table(player2Choice, 'o', "Player 2")

if tie:
    print("We have a TIE")
    exit(1)
