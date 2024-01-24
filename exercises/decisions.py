
# Recursive Function
def askForNumberInRange():
    print("----")
    number = int(input("Enter a number between 1 and 10: "))

    if number < 1:
        print("The number you entered is < 1")
        askForNumberInRange()
    elif number > 10:
        print("Enter a number you entered is > 10")
        askForNumberInRange()
    else:
        print("The number you entered is", number)


askForNumberInRange()


def generateLetterGrade():
    message = "The letter grade is";

    grade = int(input("Enter the score (0 - 100): "))

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


generateLetterGrade()

def findMiddleCharactersInString():
    string = str(input("Enter a word to get the middle character: "))
    length = len(string)

    if length % 2 == 0:
        # EVEN -> get the two in the middle
        firstChar = string[length // 2 - 1]
        secondChar = string[length // 2]
        print(f"The middle chars of the word {string} are \"{firstChar}{secondChar}\"")

    else:
        char = string[length // 2]
        print(f"The middle character of the word {string} is \"{char}\"")


findMiddleCharactersInString()