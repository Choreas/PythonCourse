import TicTacToe

# 4.1.3.6 LAB: A leap year: writing your own functions

def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def TestisYearLeap():
    testData = [1900, 2000, 2016, 1987]
    testResults = [False, True, True, False]
    for i in range(len(testData)):
        yr = testData[i]
        print(yr,"->",end="")
        result = isYearLeap(yr)
        if result == testResults[i]:
                print("OK")
        else:
                print("Failed")

#4.1.3.7 LAB: How many days: writing and using your own functions

def daysInMonth(year, month):
    not_leap_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    if year == isYearLeap:
        date_month = leap_month[month-1]
        return date_month
    else:
        date_month = not_leap_month[month-1]
        return date_month
    

def TestDaysMonth():
    testYears = [1900, 2000, 2016, 1987]
    testMonths = [2, 2, 1, 11]
    testResults = [28, 29, 31, 30]
    for i in range(len(testYears)):
            yr = testYears[i]
            mo = testMonths[i]
            print(yr, mo, "->", end="")
            result = daysInMonth(yr, mo)
            if result == testResults[i]:
                    print("OK")
            else:
                    print("Failed")

#4.1.3.8 LAB: Day of the year: writing and using your own functions
def dayOfYear():
    not_leap_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    for i in range(month-1):
         
        if isYearLeap(year):
            day += leap_month[i]
        else:
            day += not_leap_month[i]
    print("Day of the year ", day)
    
#4.1.3.9 LAB: Prime numbers - how to find them

def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
       
    return True

def TestisPrime():
    a = 0
    a = int(input("Enter a number and the program will list the primary number from 2 to your number: "))
    for i in range(1, a):
        if isPrime(i + 1):
            print(i + 1, end=" ")
    print()