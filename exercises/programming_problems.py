import datetime
import math
from tabulate import tabulate


def exercise1_KgToPound():
    kg = float(input("Enter a weight in kg: "))
    pound = kg * 2.2
    print("The weight in pounds is: ", pound)


def exercise2_calculateTheAge():
    age = int(input("Enter your year of birth: "))
    todaysYear = datetime.datetime.now().year

    print("Your age is: ", todaysYear - age)


def exercise3_calculateDataOfArticle():
    print("Please enter a radius of a circle: ")
    radius = float(input())
    print(tabulate([
        ["Area", math.pi * radius ** 2],
        ["Circumference", 2 * math.pi * radius],
        ["Volume", 4/3 * math.pi * radius ** 3],
        ["Surface", 4 * math.pi * radius ** 2]
    ], ["Data", "Result"]))


exercise1_KgToPound()
exercise2_calculateTheAge()
exercise3_calculateDataOfArticle()