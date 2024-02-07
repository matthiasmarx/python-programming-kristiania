RATE = 0.05
INITIAL_BALANCE = 10000


def printBalanceTable(years):
    balance = INITIAL_BALANCE
    for year in range(1, years+1):
        interest = balance * RATE
        balance = balance + interest
        print(f"{year}   {balance: .2f}")



try:
    years = int(input("For how hany years, do you want to see the balance?  --> "))
    printBalanceTable(years)

except ValueError:
    print("Invalid input. Skipped!")


def exercise2_generateTexts(text):
    print("----------------")
    print("Uppercase letters:", end=" ")
    for char in text:
        if char.isupper():
            print(char, end=", ")

    print("")
    print("Every second letter:", end=" ")
    for i in range(0, len(text), 2):
        print(text[i], end=", ")

    print("")
    print("Every second letter:", end=" ")
    for char in text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            print("_", end="")
        else:
            print(char, end="")

    print("")
    print("Amount of digits:", end=" ")
    digitCounter = 0
    for char in text:
        if char.isdigit():
            digitCounter += 1
    print(digitCounter)

    print("Amount of vowels:", end=" ")
    vowelCounter = 0
    for char in text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowelCounter += 1
    print(vowelCounter)

    print("----------------")


try:
    text = input("Enter a word: ")
    exercise2_generateTexts(text)

except ValueError:
    print("Invalid input. Skipped!")



def spellAWordTheOtherWayRound(word):
    for i in range(len(word) - 1, -1, -1):
        print(word[i], end="")

try:
    word = input("Enter a word: ")
    spellAWordTheOtherWayRound(word)

except ValueError:
    print("Invalid input. Skipped!")



def starSign():
    for i in range(6):
        for j in range(i):
            print("*", end="")
        print("")

starSign()


def printOutTheCharF():
    print("---------------")
    for i in range(5):
        if i == 0 or i == 2:
            for j in range(6):
                print("X", end="")
            print("")
        else:
            print("XX")
    print("---------------")


printOutTheCharF()