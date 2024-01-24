# Recursive Function
def askForNumberInRange(number):
    number = int(number)
    if number < 1:
        print("The number you entered is < 1")
        askForNumberInRange(input("Enter a number between 1 and 10: "))
    elif number > 10:
        print("Enter a number you entered is > 10")
        askForNumberInRange(input("Enter a number between 1 and 10: "))
    else:
        print("The number you entered is", number)

try:
    print("----")
    number = int(input("Enter a number between 1 and 10: "))
    askForNumberInRange(number)
except ValueError:
    print("Input not valid. ->Skipped program!")




def generateLetterGrade(grade):
    message = "The letter grade is";

    if grade < 60:
        print(message, "F")
    elif grade < 70:
        print(message, "D")
    elif grade < 80:
        print(message, "C")
    elif grade < 90:
        print(message, "B")
    elif grade <= 100:
        print(message, "A")
    else:
        print("The input is not a valid amount of points. Please enter a number between 0 and 100!")
        generateLetterGrade()


try:
    grade = int(input("Enter the score (0 - 100): "))
    generateLetterGrade(grade)

except ValueError:
    print("Cannot handle this value. Skipped program!")







def findMiddleCharacterOfWord(word):
    string = str(word)
    length = len(string)
    if length % 2 == 0:
        # EVEN -> get the two in the middle
        firstChar = string[length // 2 - 1]
        secondChar = string[length // 2]
        print(f"The middle chars of the word {string} are \"{firstChar}{secondChar}\"")

    else:
        char = string[length // 2]
        print(f"The middle character of the word {string} is \"{char}\"")


try:
    word = input("Enter a word to get the middle character: ")
    findMiddleCharacterOfWord(word)

except IndexError:
    print("You need to enter a word! -> Skipped program!")


def calculator(a, b, operator):
    if operator == '*':
        result = a * b
        print(f"{a} * {b} = {result}")
    elif operator == '/':
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}")
        else:
            print("Division by zero is not allowed.")
    elif operator == '+':
        result = a + b
        print(f"{a} + {b} = {result}")
    elif operator == '-':
        result = a - b
        print(f"{a} - {b} = {result}")
    else:
        print("Invalid operator or operator is not in the list")


try:
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operator = input("Enter the operator (*, /, +, or -): ")

    calculator(a, b, operator)

except ValueError:
    print("Invalid input. Please enter valid numeric values. ->  Skipped program!")




def unitConverter(value, unit):
    KG_IN_LBS = 0.453592

    if unit == "K":
        result = round(value / KG_IN_LBS, 2)
        print(f"You are {result} lbs(s)")
    elif unit == "L":
        result = round(value * KG_IN_LBS, 2)
        print(f"You are {result} kilo(s)")
    else:
        print("Unit cannot be converted, sry!")

try:
    value = float(input("Weight: "))
    unit = str(input("(L)bs or (K)g:"))
    unitConverter(value, unit)
except ValueError:
    print("You need to write something! -> Skipped program!")


