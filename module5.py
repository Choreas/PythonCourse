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

def LedDisplay():
    num = input("Enter a positve integer for LED display: ")
    return _ParseLed(num)

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

def IsPalindrome(strng):
    try:
        strng = str(strng)
    except:
        return "Error: Could not parse this string."
    strng = strng.replace(" ", "", -1).upper()
    strnglen = len(strng)
    if not strng.isalpha():
        return "Error: Your string must be a true Alpha."
    if not strnglen > 1:
        return "Error: Only one character? That's called cheating."
    for x in range(strnglen // 2):
        if not ord(strng[x]) == ord(strng[strnglen - x - 1]):
            return "Your string is no emordnilap."
    return "That is a palindrome!"