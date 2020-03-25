import random

boardElements = ["+-------+-------+-------+","|       |       |       |"]
fields = [[i + n for i in range(1,4)] for n in range(0,7,3)]

def InitBoard():
    fields = [[i + n for i in range(1,4)] for n in range(0,7,3)]

def DisplayBoard():
    for topSep in range(3):
        print(boardElements[0])
        for gridSep in range(3):
            if gridSep != 1:
                print(boardElements[1])
            else:
                print(boardElements[1][0:4] + str(fields[topSep][0]) + boardElements[1][5:8] + boardElements[1][0:4] + str(fields[topSep][1]) + boardElements[1][5:8] + boardElements[1][0:4] + str(fields[topSep][2]) + boardElements[1][5:9])             
    print(boardElements[0])

def EnterMove(field, val):
    if not field in range(1,10):
        return False
    for x in range(3):
        if field in fields[x]:
            fields[x][fields[x].index(field)] = val
            return True
    return False




def computerTurn():
    while True:
        field = random.randrange(1,10)
        if EnterMove(field, "X"):
            break

def VictoryFor(sign):
    # Check for 3 in a row
    for row in range(3):
        for col in range(3):
            if not fields[row][col] == sign:
                break
            if col == 2:
                return True
    # Check for 3 in a column
    for col in range(3):
        for row in range(3):
            if not fields[row][col] == sign:
                break
            if row == 2:
                return True    
    # Check for 3 diagonally
    for field in range(3):
        if not fields[field][field] == sign:
            break
        if field == 2:
            return True
    for field in range(3):
        if not fields[2 - field][field] == sign:
            break
        if field == 2:
            return True
    return False


while True:
    InitBoard()
    fields[1][1] = "X"
    for x in range(10):
        DisplayBoard()
        userMove = input("Field: ")
        if not userMove.isdigit():
            print("Invalid input.")
            continue
        if not EnterMove(int(userMove), "O"):
            print("Illegal move or invalid input.")
            continue
        DisplayBoard()
        if VictoryFor("O"):
            print("You win!")
            break
        wait = input("Computer's turn...")
        computerTurn()
        DisplayBoard()
        if VictoryFor("X"):
            print("You loose =(")
            break
        if x == 9:
            print("tie")
            break
    again = input("Play again? (y)")
    if again.upper() != "Y":
        break