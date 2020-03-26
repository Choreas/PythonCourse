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
