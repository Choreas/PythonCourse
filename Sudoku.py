cmds = {"check":"Check your solution", "exit":"Exit to menu. NOTE: no saving", "help":"Show help", "show":"Show board", 
        "[input]":"Row + Column + Value (format: 123)"}

def _Server():
    inp = input("Sudoku: ")
    inp = inp.replace(" ", "", -1)
    if not inp in cmds.keys() and not inp.isdigit():
        return ""
    return inp.lower()

def _DisplayBoard(fieldsList):
    try:
        fields = _validateFields_(fieldsList)
    except Exception as e:
        print("Internal error " + e.args[0])
        return e.args[0]
    boardElements = ["+", "-", "=", "|", "‖", " "]
    gridNums = {1:"①", 2:"②", 3:"③", 4:"④", 5:"⑤", 6:"⑥", 7:"⑦", 8:"⑧", 9:"⑨"}
    boardWidth = 2
    for _ in range(5):
        print("\n")
    topLine = " " + boardElements[0]
    for linePart in range(9):
        topLine += boardElements[1]*boardWidth + gridNums.get(linePart + 1) + boardElements[1]*boardWidth + boardElements[0]
    print(topLine)
    for boardPart in range(9):

        vertLine = gridNums.get(boardPart + 1) + boardElements[3]
        for colN in range(9):
            verSep = boardElements[3]
            if (colN + 1) % 3 == 0:
                if not colN + 1 == 9:
                    verSep = boardElements[4]
            field = fields[boardPart*9 + colN]
            if field == "0":
                field = " "
            vertLine += boardElements[5]*boardWidth + field + boardElements[5]*boardWidth + verSep
        print(vertLine)

        horSep = boardElements[1]
        if (boardPart + 1) % 3 == 0:
            if not boardPart + 1 == 9:
                horSep = boardElements[2]
        horLine = " " + boardElements[0]
        for _ in range(9):
            horLine += horSep*(boardWidth*2) + horSep + boardElements[0]
        print(horLine)

def CheckSolution(fieldsList):
    try:
        fields = _validateFields_(fieldsList)
    except Exception as e:
        return e.args[0]
    if fields.count("0") > 0:
        return "Incomplete"
    cols = [[] for n in range(9)] 
    row = []
    grids = [[] for n in range(9)]

    for idx, val in enumerate(fields):
        rownum = ((idx // 9))
        colnum = ((idx % 9))
        gridnum = (((idx % 9) // 3) + (((idx // 9) // 3) * 3))
        if row.count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Row")       
        if cols[colnum].count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Column")
        if grids[gridnum].count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Grid")
        row.append(val)
        cols[colnum].append(val)
        grids[gridnum].append(val)
        if idx % 9 == 8:
            row.clear()
    return "Correct"

def _Wrong(row, col, grid, val, source):
    return ("(First) incorrect value.\nRow: " + str(row + 1) + "\nCol: " + 
            str(col + 1) + "\nGrid: " + str(grid + 1) + "\nValue: " + str(val) +
            "\nSource: " + source)

def _validateFields_(fieldsList):
    fields = ""
    try:
        fields = fields.join(fieldsList)
    except:
        raise Exception("Error: Could not parse solution to string.")
    fields = fields.replace(" ", "", -1)
    if not fields.isdigit():
        raise Exception("Error: Solution can only contain integers.")
    if not len(fields) == 81:
        raise Exception("Error: There are 81 fields, so your solution must contain exactly 81 values.")
    return fields

def _PrintHelp():
    cmdList = cmds.items()
    print("\n\n==help==\n")
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n\n")

def _validateMove_(move):
    move = move.replace(" ", "", -1)
    if not move.isdigit():
        raise Exception("Error: Enter your input like this: 123 (row, column, value)")   
    try:
        move = list(move)
    except:
        raise Exception("Error: move could not be pared to list.")
    if not len(move) == 3:
        raise Exception("Error: Enter your input like this: 123 (row, column, value)")
    if int(move[0]) == 0 or int(move[1]) == 0:
        raise Exception("Error: You cannot specify zero (0) for row and column.")
    
    return move

def _executeMove_(fields, fixed, move):
    try:
        move = _validateMove_(move)
    except Exception as e:
        raise Exception(e.args[0])
    row = int(move[0])
    col = int(move[1])
    val = int(move[2])

    if fixed[(row-1)*9 + (col-1)] != "0":
        raise Exception("This field is fixed.")
    fields[(row-1)*9 + (col-1)] = move[2]
    return fields

def Play():    
    fixed =  "300601005002000400100000020000408010600000007070905000090000000008000500200109006"
    fields = list(fixed)
    _DisplayBoard(fields)
    while True:
        inp = _Server()
        if inp == "":
            print("Could not understand your input. help for help.")
            continue
        if inp == "help":
            _PrintHelp()
            continue
        if inp == "show":
            _DisplayBoard(fields)
            continue
        if inp == "exit":
            ex = input("Progress isn't saved. Are you sure? (y/any): ")
            if ex.upper() == "Y":
                break
            continue
        if inp == "check":
            status = CheckSolution(fields)
            if status == "Correct":
                print(status)
                break
            print(status)
            continue
        try:
            fields = _executeMove_(fields, fixed, inp)
            _DisplayBoard(fields)
        except Exception as e:
            print(e.args[0])
            continue
        continue