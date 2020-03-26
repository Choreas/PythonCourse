from random import randrange
from time import sleep

def _InitFields():
    return [[i + n for i in range(1,4)] for n in range(0,7,3)]

def _DisplayBoard(fields):
    boardElements = ["+-------+-------+-------+", "|       |       |       |"]
    for topSep in range(3):
        print(boardElements[0])
        for gridSep in range(3):
            if gridSep != 1:
                print(boardElements[1])
            else:
                fieldVals = []
                for n in range(3):
                    if str(fields[topSep][n]).isdigit():
                        fieldVals.append(" ")
                    else:
                        fieldVals.append(fields[topSep][n])
                print(boardElements[1][0:4] + str(fieldVals[0]) + boardElements[1][5:8] + boardElements[1][0:4] + str(fieldVals[1]) + boardElements[1][5:8] + boardElements[1][0:4] + str(fieldVals[2]) + boardElements[1][5:9])             
                #print(boardElements[1][0:4] + str(fields[topSep][0]) + boardElements[1][5:8] + boardElements[1][0:4] + str(fields[topSep][1]) + boardElements[1][5:8] + boardElements[1][0:4] + str(fields[topSep][2]) + boardElements[1][5:9])             
    print(boardElements[0])

def _EnterMove(fields, field, val):
    if not field in range(1,10):
        return False
    for x in range(3):
        if field in fields[x]:
            fields[x][fields[x].index(field)] = val
            return True
    return False


def _ComputerTurn(fields):
    while True:
        field = randrange(1,10)
        if _EnterMove(fields, field, "X"):
            break

def _VictoryFor(fields, sign):
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

def _WaitForComp():
    print("Waiting for computer")
    for x in range(3):
        print(".")
        sleep(0.5)

def Play():    
    fields = _InitFields()
    fields[1][1] = "X"
    currentTurn = 1
    _DisplayBoard(fields)
    while currentTurn <= 9:
        userMove = input("Choose your field (1-9): ")
        if not userMove.isdigit():
            print("Invalid input.")
            continue
        if not _EnterMove(fields, int(userMove), "O"):
            print("Illegal move or invalid input.")
            continue
        if _VictoryFor(fields, "O"):
            print("You win!")
            break
        _WaitForComp()
        _ComputerTurn(fields)
        if _VictoryFor(fields, "X"):
            print("You loose =(")
            break
        if currentTurn == 9:
            print("tie")
            break
        currentTurn += 1
        _DisplayBoard(fields)
    _DisplayBoard(fields)
    print("===========FIN===========")
        