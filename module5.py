import Sudoku

# The list contains each layer for each digit from top to bottom and consists of true and false values for
# turned on resp. turned off leds.
def _ParseLed(num):
    leds = [{1:[False, False, True], 2:[True, True, True], 3:[True, True, True], 4:[True, False, True], 5:[True, True, True], 6:[True, True, True], 7:[True, True, True], 8:[True, True, True], 9:[True, True, True], 0:[True, True, True]},
            {1:[False, False, True], 2:[False, False, True], 3:[False, False, True], 4:[True, False, True], 5:[True, False, False], 6:[True, False, False], 7:[False, False, True], 8:[True, False, True], 9:[True, False, True], 0:[True, False, True]},
            {1:[False, False, True], 2:[True, True, True], 3:[True, True, True], 4:[True, True, True], 5:[True, True, True], 6:[True, True, True], 7:[False, False, True], 8:[True, True, True], 9:[True, True, True], 0:[True, False, True]},
            {1:[False, False, True], 2:[True, False, False], 3:[False, False, True], 4:[False, False, True], 5:[False, False, True], 6:[True, False, True], 7:[False, False, True], 8:[True, False, True], 9:[False, False, True], 0:[True, False, True]},
            {1:[False, False, True], 2:[True, True, True], 3:[True, True, True], 4:[False, False, True], 5:[True, True, True], 6:[True, True, True], 7:[False, False, True], 8:[True, True, True], 9:[True, True, True], 0:[True, True, True]}]

    try:
        num = int(num)
    except:
        return "Error: Invalid format (expected int)"
    if num < 0:
        return "Error: Enter a positive integer"

    led = ""
    numStr = str(num)
    for x in range(5):    
        for n in numStr:
            for on in leds[x].get(int(n)):
                if on:
                    led += "#"
                else:
                    led += " "
            led += " "
        led += " \n"
    return led

# Interface function for LED digit parser.
# Might be useless and could as well be part of the main function.
def LedDisplay(num):
    return _ParseLed(num)

# Uses codepage values (ascii) to add to single characters.
def CeasarCipher(strng, shifts):
    try:
        shifts = int(shifts)
    except:
        return "Error: second parameter must be integer."
    shifts = shifts % 26
    if shifts == 0:
        return strng
    res = ""
    for code in strng.encode('ascii'):
        if code >= 65 and code <= 90:
            code += shifts
            if code > 90:
                code = 65 + (code - 90) - 1
        elif code >= 97 and code <= 122:
            code += shifts
            if code > 122:
                code = 97 + (code - 122) - 1
        res += chr(code)
    return res

# Uses ord() to compare characters from start resp. end of two strings until the center is reached
# to find palindromes.
def IsPalindrome(strng):
    try:
        strng = _simplifyString(strng)
    except Exception as e:
        return e.args[0]
    strnglen = len(strng)
    for x in range(strnglen // 2):
        if not ord(strng[x]) == ord(strng[strnglen - x - 1]):
            return "Your string is no emordnilap."
    return "That is a palindrome!"

# Checks if two strings are anagrams by popping characters (removing them one by one and catching the exception
# for a character not being available).
def IsAnagram(sample, strng):
    try:
        sample = _simplifyString(sample)
        strng = _simplifyString(strng)
    except Exception as e:
        return e.args[0]
    if sample == strng:
        return "Your strings resemble each other like an egg another."
    strnglen = len(strng)
    samplelen = len(sample)
    if not strnglen == samplelen:
        return "Mangorana"
    sampleChars = list(sample)
    strngChars = list(strng)
    for char in sampleChars:
        try:
            idx = strngChars.remove(char)
        except:
            return "Mangorana"
    return "You have an anagaram here =)"

# Makes sure parameter is string, else makes it string.
# Sets it to lowercase and makes sure there are only characters and its length is > 1.
def _simplifyString(strng):
    try:
        strng = str(strng)
    except:
        raise Exception("Error: Could not parse this string.")
    strng = strng.replace(" ", "", -1).upper()
    if not strng.isalpha():
        raise Exception("Error: Your string must be alpha.")
    if not len(strng) > 1:
        raise Exception("Error: Only one character? That's called cheating.")
    return strng