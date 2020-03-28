import module4, module5, argparse

cmds = {"-ana":"Run Anagram Checker", "-ci":"Run ciphertext", "exit":"Exit to menu from everywhere, or kill program from menu", "-help":"Show help", "-pal":"Run Palindrome Checker", 
        "-sud":"Check a solution for a sudoku", "-ttt":"Play Tic-Tac-Toe", "-test":"test"}
print("-help for help =)")

def Server():
    inp = input("PythonCourse: ")
    try:
        inp = str(inp)
    except:
        return ""
    if not inp in cmds.keys():
        return ""
    return inp.lower()

def _PrintHelp():
    cmdList = cmds.items()
    print("\n\n==help==\n")
    for item in cmdList:
        print((item[0] + ": " + item[1]))
    print("\n\n")

def _ttt_():
    while True:
        module4.TicTacToe.Play()
        again = input("Play again? (y/any)")
        if again.upper() != "Y":
            break

def _cipher_():
    while True:
        txt = input("Enter text: ")
        if txt.upper() == "EXIT":
            break
        shifts = input("Enter shifts: ")
        if shifts.upper() == "EXIT":
            break
        print(module5.CeasarCipher(txt, shifts))

def _pal_():
    while True:
        arg = input("Check this for being a palindrome: ")
        if arg.upper() == "EXIT":
            break
        print(module5.IsPalindrome(arg))

def _ana_():
    while True:
        arg1 = input("Enter first string: ")
        if arg1.upper() == "EXIT":
            break
        arg2 = input("Enter second string: ")
        if arg2.upper() == "EXIT":
            break
        print(module5.IsAnagram(arg1, arg2))

def _sud_():
    module5.Sudoku.Play()

def _test_():
    while True:
        arg = input("Enter string: ")
        if arg.upper() == "EXIT":
            break
        module5.Sudoku._DisplayBoard(arg)

while True:
    choice = Server()
    if choice == "":
        print("Could not recognize your command. Type -help for help.")
        continue
    if choice == "exit":
        break
    if choice == "-test":
        _test_()
        continue
    if choice == "-help":
        _PrintHelp()
        continue
    elif choice == "-ana":
        _ana_()
        continue
    elif choice == "-pal":
        _pal_()
        continue
    elif choice == "-ttt":
        _ttt_()
        continue
    elif choice == "-sud":
        _sud_()
        continue
    elif choice == "-ci":
        _cipher_()
        continue
#Sudoku
#Testcases
#False
#195743862431865927876192543387459216612387495549216738763524189928671354254938671
#True
#295743861431865927876192543387459216612387495549216738763524189928671354154938672
