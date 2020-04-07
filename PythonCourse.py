import module3, module4, module5, parsing

# This is the entry point into all programs. 
# It uses a simple cli (command line interface) which can only be used from inside the running program.
# The current approach is still pretty procedural, though some programs are partly class based.

# These are the available commands for the cli.
cmds = {"ana":"Run Anagram Checker", "ci":"Run ciphertext", "exit":"Exit to menu from everywhere, or kill program from menu", 
        "help":"Show help", "led":"Parse a number as LED digits", "pal":"Run Palindrome Checker", 
        "sud":"Play Sudoku", "ttt":"Play Tic-Tac-Toe", "3.1.2.11":"LAB: the Pretty Vowel Eater", "3.1.2.14":"LAB: Essentials of the while loop", 
        "3.1.2.15":"LAB: Collatz's hypothesis", "3.1.4.6":"LAB: The basics of lists", "3.1.4.13":"LAB: The basics of lists - the Beatles",
       "3.1.6.9":"LAB: Operating with lists - basics", "4.1.3.6":"LAB: A leap year: writing your own functions",
      "4.1.3.7":"LAB: How many days: writing and using your own functions", "4.1.3.8":"LAB: Day of the year: writing and using your own functions",
     "4.1.3.9":"LAB: Prime numbers - how to find them", "-factory":"Run file factory", "-test":"test"}

print("help for help =)")

# This function centralizes command prompts.
def Server():
    inp = input("PythonCourse: ")
    try:
        inp = str(inp).replace(" ", "", -1).lower()
    except:
        return ""
    if not inp in cmds.keys():
        return ""
    return inp

# This should print command specific help.
def _PrintArgsHelp_(cmd):
    print("\n==help==\n")
    if cmd == "led":
        cmdList = [["led (this program)", "Follow instructions for this program"], ["help", "Show help"], ["exit", "Exit to menu"]]
    else:
        cmdList = [["this program", "Follow instructions for this program"], ["help", "Show help"], ["exit", "Exit to menu"]]
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n")

# Just like server, this centralizes command prompts, but argument specific.
def _argServer_(cmd, prompts):
    args = []
    for idx, prompt in enumerate(prompts):
        repeat = True
        while repeat:
            repeat = False
            arg = input(prompt).lower()
            if arg == "help":
                repeat = True
                _PrintArgsHelp_(cmd)
                continue
            if arg == "exit":
                raise Exception("exit")
            args.append(arg)
    return args

# Prints general help for cli commands.
def _PrintHelp():
    cmdList = cmds.items()
    print("\n\n==help==\n")
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n\n")

# TicTacToe
def _ttt_():
    while True:
        module4.TicTacToe.Play()
        again = input("Play again? (y/any)")
        if again.upper() != "Y":
            break

# Ceasar's Cipher (ROT)
def _cipher_():
    while True:
        try:
            args = _argServer_("ci", ["Enter text: ", "Enter shifts: "])
        except:
            print("\n")
            break     
        print(module5.CeasarCipher(args[0], args[1]))

# Palindrome checker.
def _pal_():
    while True:
        try:
            args = _argServer_("pal", ["Check this for being a palindrome: "])
        except:
            print("\n")
            break 
        print(module5.IsPalindrome(args[0]))

# LED digit parser.
def _led_():
    while True:
        try:
            args = _argServer_("led", ["Enter number for led display: "])
        except:
            print("\n")
            break      
        print(module5.LedDisplay(args[0]))

# Anagram checker.
def _ana_():
    while True:
        try:
            args = _argServer_("ana", ["Enter first string: ", "Enter second string: "])
        except:
            print("\n")
            break 
        print(module5.IsAnagram(args[0], args[1]))

# Sudoku.
def _sud_():
    try:
        module5.Sudoku.Play()
    except Exception as e:
        print(e)
        print("\n")
        return

def _test_():
    #csv = factory.csvfactory("sudokus")
    #csv.Readcsv()
    return

# Interface for parsing unit.
def _factory_():
    parsing.Init()

while True:
    choice = Server()
    if choice == "":
        print("Could not recognize your command. Type help for help.")
        continue
    if choice == "exit":
        break
    if choice == "-test":
        _test_()
        continue
    if choice == "help":
        _PrintHelp()
        continue
    elif choice == "ana":
        _ana_()
        continue
    elif choice == "pal":
        _pal_()
        continue
    elif choice == "ttt":
        _ttt_()
        continue
    elif choice == "sud":
        _sud_()
        continue
    elif choice == "ci":
        _cipher_()
        continue
    elif choice == "led":
        _led_()
        continue
    elif choice == "3.1.2.11":
        module3.VowelEate()
        continue
    elif choice == "3.1.2.14":
        module3.EssentialsWhile()
        continue
    elif choice == "3.1.2.15":
        module3.Collarz()
        continue
    elif choice == "3.1.4.6":
        module3.BasicsOfList()
        continue
    elif choice == "3.1.4.13":
        module3.TheBeatles()
        continue
    elif choice == "3.1.6.9":
        module3.OpertingWithLists()
        continue
    elif choice == "4.1.3.6":
        module4.TestisYearLeap()
        continue
    elif choice == "4.1.3.7":
        module4.TestDaysMonth()
        continue
    elif choice == "4.1.3.8":
        module4.dayOfYear()
        continue
    elif choice == "4.1.3.9":
        module4.TestisPrime()
        continue
    elif choice == "-factory":
        _factory_()
        continue