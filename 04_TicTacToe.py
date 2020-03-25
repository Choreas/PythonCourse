
boardElements = ["+-------+-------+-------+","|       |       |       |"]
fields = [[i + n for i in range(1,4)] for n in range(0,7,3)]
print(fields)

def DisplayBoard():
    for topSep in range(3):
        print(boardElements[0])
        for gridSep in range(3):
            if gridSep != 1:
                print(boardElements[1])
            else:
                print(boardElements[1][0])             
    print(boardElements[0])   

DisplayBoard()
##def EnterMove(board):
###
### the function accepts the board current status, asks the user about their move, 
### checks the input and updates the board according to the user's decision
###
##
##def MakeListOfFreeFields(board):
###
### the function browses the board and builds a list of all the free squares; 
### the list consists of tuples, while each tuple is a pair of row and column numbers
###
##
##def VictoryFor(board, sign):
###
### the function analyzes the board status in order to check if 
### the player using 'O's or 'X's has won the game
###
##
##def DrawMove(board):
###
### the function draws the computer's move and updates the board
###
##
##
