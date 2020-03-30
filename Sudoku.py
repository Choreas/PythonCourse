import factory

# I definetely spent most time with this because it gives great opportunity to develop into any direction.
# I built it using a procedural approach and finally implemented load and save capabilities in a class based
# manner. There is much room for improvements so you could use it to play and test and code as you like.

# Cli arguments.
cmds = {"check":"Check your solution", "exit":"Exit to menu.", 
        "help":"Show help", "reset":"Reset state of current game",
        "select":"Select a new sudoku", 
        "save":"Save your progress", 
        "show":"Show board", 
        "[input]":"Row + Column + Value (format: 123)"}

# Cli input centralizer.
def _Server():
    inp = input("Sudoku: ")
    inp = inp.replace(" ", "", -1).lower()
    if not inp in cmds.keys() and not inp.isdigit():
        return ""
    return inp

# Renders game grid. It takes the fields (cell values) and the internal number of the sudoku itself, just to print it.
def _DisplayBoard(fieldsList, sudNo):
    try:
        # Rendering function needs string.
        fields = _validateFields_(fieldsList)
    except Exception as e:
        print("Internal error " + e.args[0])
        return e.args[0]
    # Single elements of the board in contrast to tictactoe, where I hardcoded most of the elements in long strings.
    # If you changed the position of this list's elements, you would see funny effects ;)
    boardElements = ["+", "-", "=", "|", "‖", " "]
    # Unicode numbers to make it easier for the player to count the cells.
    gridNums = {1:"①", 2:"②", 3:"③", 4:"④", 5:"⑤", 6:"⑥", 7:"⑦", 8:"⑧", 9:"⑨"}
    boardWidth = 2
    # This loop simply puts some linebreaks. I noticed putting them in a single string has some weird effect.
    for _ in range(4):
        print("\n")
    # Just print internal sudoku number on top.
    print(" #" + sudNo)
    # Initialize the following board element string with an initial element.
    topLine = " " + boardElements[0]
    # This loop runs only once, it will produce the most upper board line. This is singled out because the unicode
    # numbers (gridnums) must be included.
    for linePart in range(9):
        topLine += boardElements[1]*boardWidth + gridNums.get(linePart + 1) + boardElements[1]*boardWidth + boardElements[0]
    print(topLine)
    # Now the main rendering takes place. This loop will print one line after each other, like this:
    # 1a) Build cells: | 1 | 6 | 9 ||  ...  1b) build horizontal separator: +---+---+--- ... etc..
    for boardPart in range(9):
        vertLine = gridNums.get(boardPart + 1) + boardElements[3]
        for colN in range(9):
            verSep = boardElements[3]
            if (colN + 1) % 3 == 0:
                # This will produce special separators in case a 3x3 grid has to be empathized.
                if not colN + 1 == 9:
                    verSep = boardElements[4]
            field = fields[boardPart*9 + colN]
            # field takes the value of the needed cell value and will be blank if value is 0,
            # because 0 is used for unfilled cells in our fieldsList.
            if field == "0":
                field = " "
            vertLine += boardElements[5]*boardWidth + field + boardElements[5]*boardWidth + verSep
        print(vertLine)

        horSep = boardElements[1]
        if (boardPart + 1) % 3 == 0:
            # This will produce special separators in case a 3x3 grid has to be empathized.
            if not boardPart + 1 == 9:
                horSep = boardElements[2]
        horLine = " " + boardElements[0]
        for _ in range(9):
            horLine += horSep*(boardWidth*2) + horSep + boardElements[0]
        print(horLine)

# Heartpiece of the program, checks for valid solutions.
def CheckSolution(fieldsList):
    try:
        fields = _validateFields_(fieldsList)
    except Exception as e:
        return e.args[0]
    if fields.count("0") > 0:
        return "Incomplete"
    # Initialize lists to store values for columns, rows and grids.
    cols = [[] for n in range(9)] 
    row = []
    grids = [[] for n in range(9)]

    # Iterates over each value once and stores each value in the corresponding list at the right index for
    # column, row and grid.
    for idx, val in enumerate(fields):
        # These calculations determine the correct row, column and grid of the current value.
        rownum = ((idx // 9))
        colnum = ((idx % 9))
        gridnum = (((idx % 9) // 3) + (((idx // 9) // 3) * 3))
        # Now it checks whether there already is the same value stored in either row, column or grid.
        if row.count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Row")       
        if cols[colnum].count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Column")
        if grids[gridnum].count(val) > 0:
            return _Wrong(rownum, colnum, gridnum, val, "Grid")
        # Now append.
        row.append(val)
        cols[colnum].append(val)
        grids[gridnum].append(val)
        # Note: since we iterate row for row, we don't need a multi dimensional list for rows.
        # That's why the list is cleared for each 9nth value.
        if idx % 9 == 8:
            row.clear()
    return "Correct"

# Parses a message for incorrect solutions.
def _Wrong(row, col, grid, val, source):
    return ("(First) incorrect value.\nRow: " + str(row + 1) + "\nCol: " + 
            str(col + 1) + "\nGrid: " + str(grid + 1) + "\nValue: " + str(val) +
            "\nSource: " + source)

# Makes a string from fieldsList, because many functions expect a string. 
# Also validates some information, like whether all 81 values are included.
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

# Cli help.
def _PrintHelp():
    cmdList = cmds.items()
    print("\n\n==help==\n")
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n\n")

# Takes user input and checks its format.
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

# A move is an input operation to change any cell's value.
# It takes fields (all values), fixed (the start values of this game) and the intended change (move).
def _executeMove_(fields, fixed, move):
    try:
        move = _validateMove_(move)
    except Exception as e:
        raise Exception(e.args[0])
    # Gets all elements from move. See corresponding cli command.
    row = int(move[0])
    col = int(move[1])
    val = int(move[2])

    # Makes sure the user doesn't try to change fixed values.
    if fixed[(row-1)*9 + (col-1)] != "0":
        raise Exception("This field is fixed.")
    fields[(row-1)*9 + (col-1)] = move[2]
    return fields

# Entry point. Procedurally executes game process.
def Play():   
    # These objects are used to load and save game states and fetch game templates from memory.
    sudokuLibrary = factory.sudokuTemplate("sudokuTemplates")
    saveState = factory.sudokuSavestate()
    # Number of current sudoku. At start set to last saved game, fetched from savestate object.
    sudNo = str(int(saveState.recentSud) + 1)
    # Standard values for this game.
    fixed = sudokuLibrary.GetSudoku(sudNo)
    try:
        # Tries to fetch saved game state.
        fields = list(saveState.GetState(sudNo))
        print("Load successful for saved game")
    except:
        print("No saved state found, starting new game.")
        fields = list(fixed)
    _DisplayBoard(fields, sudNo)
    while True:
        inp = _Server()
        if inp == "":
            print("Could not understand your input. help for help.")
            continue
        if inp == "help":
            _PrintHelp()
            continue
        if inp == "show":
            _DisplayBoard(fields, sudNo)
            continue
        if inp == "reset":
            ex = input("Are you sure about resetting your current progress? (y/any): ")
            if ex.upper() == "Y":
                fields = list(fixed)
                _DisplayBoard(fields, sudNo)
            continue
        if inp == "exit":
            try:
                saveState.SaveState(sudNo, _validateFields_(fields))
                print("Feel calm, your progress has been saved.\n")
            except:
                print("Your progress was NOT saved!\n")
            ex = input("Make sure your progress was saved. Quit now? (y/any): ")
            if ex.upper() == "Y":
                break
            continue
        if inp == "check":
            status = CheckSolution(fields)
            print(status)
            continue
        if inp == "save":
            try:
                saveState.SaveState(sudNo, _validateFields_(fields))
                print("Progress saved.\n")
            except:
                print("Saving failed!\n")
            continue
        if inp == "select":
            try:
                # Before loading new game, tries to save current state.
                saveState.SaveState(sudNo, _validateFields_(fields))
                print("Feel calm, your progress has been saved.")
            except:
                print("Your progress was not saved!\n")
            print("There are " + str(sudokuLibrary.count) + " sudokus available.")
            choice = input("Which one do you want?: ")
            try:
                fixed = sudokuLibrary.GetSudoku(choice)
                # If template is found, set sudNo to new number.
                sudNo = choice
                try:
                    fields = list(saveState.GetState(sudNo))
                    print("Load successful for saved game")
                except:
                    print("No saved state found, starting new game.")
                    fields = list(fixed)
                _DisplayBoard(fields, sudNo)
            except Exception as e:
                print(e.args[0])
            continue
        try:
            fields = _executeMove_(fields, fixed, inp)
            _DisplayBoard(fields, sudNo)
        except Exception as e:
            print(e.args[0])
            continue
        continue