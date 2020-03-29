from random import randrange
from time import sleep

# List comprehension that creates the structure of "fields". Fields contains the values for all cells of the board.
def _InitFields():
    return [[i + n for i in range(1,4)] for n in range(0,7,3)]

# Renders the game's board.
def _DisplayBoard(fields):
    boardElements = ["+-------+-------+-------+", "|       |       |       |"]
    fieldNums = {1:"①", 2:"②", 3:"③", 4:"④", 5:"⑤", 6:"⑥", 7:"⑦", 8:"⑧", 9:"⑨"}
    for _ in range(5):
        print("\n")
    for topSep in range(3):
        print(boardElements[0])
        for gridSep in range(3):
            if gridSep != 1:
                print(boardElements[1])
            else:
                fieldVals = []
                for value in fields[topSep]:
                    if str(value).isdigit():
                        fieldVals.append(fieldNums.get(value))
                    else:
                        fieldVals.append(value)
                print(boardElements[1][0:4] + str(fieldVals[0]) + boardElements[1][5:8] + 
                      boardElements[1][0:4] + str(fieldVals[1]) + boardElements[1][5:8] + 
                      boardElements[1][0:4] + str(fieldVals[2]) + boardElements[1][5:9])
    print(boardElements[0])

# This executes anyone's turns.
# Since empty cells are identified by their number in fields, checking for an empty cell is simply done
# by "if field in fields[x]". Because if it was empty, fields would contain the cell's number, here "field".
def _EnterMove(fields, field, val):
    if not field in range(1,10):
        return False
    for x in range(3):
        if field in fields[x]:
            fields[x][fields[x].index(field)] = val
            return True
    return False

# This executes the computer's turns.
# Checks for single move wins or human player opportunities that must be blocked.
# Otherwise uses randrange to fill a random cell.
def _ComputerTurn(fields):
    chance = _CheckForChance(fields, "X")
    if chance > 0:
        _EnterMove(fields, chance, "X")
        return
    humanChance = _CheckForChance(fields, "O")
    if humanChance > 0:
        _EnterMove(fields, humanChance, "X")
        return
    while True:
        field = randrange(1,10)
        if _EnterMove(fields, field, "X"):
            break

# This checks whether there are three in a row/column/diagonally.
# It simply counts through each row / column / diagonal line and if it finds three in any, returns true.
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

# This is used to give the computer basic intelligence, so it can determine whether it can win in one move,
# but also whether the player could win, so the computer can block that opportunity.
# Uses the same logic as _VictoryFor, though it can't use early exits as empty cells are no reason to exit early.
# It's basically just that and more counting.
def _CheckForChance(fields, sign):
    chanceFld = 0
    # Check for 3 in a row
    for row in range(3):
        signCount = 0
        for col in range(3):
            if fields[row][col] == sign:
                signCount += 1
            elif not fields[row][col] == sign and not str(fields[row][col]).isdigit():
                break
            if str(fields[row][col]).isdigit():
                chanceFld = col
            if col == 2 and signCount == 2:
                return _getFieldFromIdx(row, chanceFld)
    # Check for 3 in a column
    for col in range(3):
        signCount = 0
        for row in range(3):
            if fields[row][col] == sign:
                signCount += 1
            elif not fields[row][col] == sign and not str(fields[row][col]).isdigit():
                break
            if str(fields[row][col]).isdigit():
                chanceFld = row
            if row == 2 and signCount == 2:
                return _getFieldFromIdx(chanceFld, col)   
    # Check for 3 diagonally
    signCount = 0
    for field in range(3):        
        if fields[field][field] == sign:
            signCount += 1
        elif not fields[field][field] == sign and not str(fields[field][field]).isdigit():
            break
        if str(fields[field][field]).isdigit():
            chanceFld = field
        if field == 2 and signCount == 2:
            return _getFieldFromIdx(chanceFld, chanceFld)
    signCount = 0
    for field in range(3):
        if fields[2 - field][field] == sign:
            signCount += 1
        elif not fields[2 - field][field] == sign and not str(fields[2 - field][field]).isdigit():
            break
        if str(fields[2 - field][field]).isdigit():
            chanceFld = field
        if field == 2 and signCount == 2:
            return _getFieldFromIdx(2 - chanceFld, chanceFld)
    return 0

# Since the program expects a single integer for cell selection, this is used to determine a cells
# combined index in the fields list.
def _getFieldFromIdx(row, col):
    col += 1
    rowVals = {0:0, 1:3, 2:6}
    return col + rowVals.get(row)

# Display three dots and wait 1.5 seconds before computer moves to give it some taste.
def _WaitForComp():
    print("Waiting for computer")
    for x in range(3):
        print(".")
        sleep(0.5)

# Entry point. This is a procedural approach centralizing the game's process.
def Play():
    # First initialize fields (values X, O or empty cell).
    # Then let the computer do its first move and display the board.
    # Then start the process.
    fields = _InitFields()
    _ComputerTurn(fields)
    currentTurn = 1
    _DisplayBoard(fields)
    while currentTurn <= 9:
        if currentTurn >= 9:
            print("\n\n\n===Tie===")
            break
        userMove = input("Choose your field (1-9): ")
        if userMove.upper() == "EXIT":
            break
        if not userMove.isdigit():
            print("Invalid input.")
            continue
        if not _EnterMove(fields, int(userMove), "O"):
            print("Illegal move or invalid input.")
            continue
        currentTurn += 1
        if _VictoryFor(fields, "O"):
            print("You win!")
            break
        _DisplayBoard(fields)
        if currentTurn < 8:
            _WaitForComp()
        _ComputerTurn(fields)
        if _VictoryFor(fields, "X"):
            print("You loose =(")
            break
        currentTurn += 1
        _DisplayBoard(fields)
    _DisplayBoard(fields)
    print("===========FIN===========")  