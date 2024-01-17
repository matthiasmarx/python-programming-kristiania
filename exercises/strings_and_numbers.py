import math
from tabulate import tabulate


x = 2.5
y = -1.5
m = 18
n = 4

print("-----------------------------------------")
print("Exercise 1:")
print("x: ", x, " | y: ", y, " | m: ", m, " | n: ", n)
print("-----------------------------------------")


def exercise1_a():
    result = x + n * y - (x + n) * y
    return result


def exercise1_b():
    result = m // n + m % n
    return result


def exercise1_c():
    result = 5 * x - n / 5
    return result


def exercise1_d():
    result = 1 - (1 - (1 - (1 - (1 - n))))
    return result


def exercise1_e():
    result = math.sqrt(math.sqrt(n))
    return result


print("Exercise 1a: x + n * y - (x + n) * y = ", exercise1_a())
print("Exercise 1b: m // n + m % n = ", exercise1_b())
print("Exercise 1c: 5 * x - n / 5 = ", exercise1_c())
print("Exercise 1d: 1 - (1 - (1 - (1 - (1 - n)))) = ", exercise1_d())
print("Exercise 1e: math.sqrt(math.sqrt(n)) = ", exercise1_e())


n = 17
m = 18

print("-----------------------------------------")
print("Exercise 2:")
print("n: ", n, " | m: ", m)
print("-----------------------------------------")


def exercise2_a():
    result = n // 10 + n % 10
    return result


def exercise2_b():
    result = n % 2 + m % 2
    return result


def exercise2_c():
    result = (m + n) // 2
    return result


def exercise2_d():
    result = (m + n) / 2.0
    return result


def exercise2_e():
    result = int(0.5 * (m + n))
    return result


def exercise2_f():
    result = int(round(0.5 * (m + n)))
    return result


print("Exercise 2a: n // 10 + n % 10 =", exercise2_a())
print("Exercise 2b: n % 2 + m % 2 =", exercise2_b())
print("Exercise 2c: (m + n) // 2 =", exercise2_c())
print("Exercise 2d: (m + n) / 2.0 =", exercise2_d())
print("Exercise 2e: int(0.5 * (m + n)) =", exercise2_e())


s = "Hello"
t = "World"

print("-----------------------------------------")
print("Exercise 3:")
print("s: ", s, " | t: ", t)
print("-----------------------------------------")


def exercise3_a():
    result = len(s) + len(t)
    return result


def exercise3_b():
    result = s[1] + s[2]
    return result


def exercise3_c():
    result = s[len(s) // 2]
    return result


def exercise3_d():
    result = s + t
    return result


def exercise3_e():
    result = t + s
    return result


def exercise3_f():
    result = s * 2
    return result


print("Exercise 3a: len(s) + len(t) =", exercise3_a())
print("Exercise 3b: s[1] + s[2] =", exercise3_b())
print("Exercise 3c: s[len(s) // 2] =", exercise3_c())
print("Exercise 3d: s + t =", exercise3_d())
print("Exercise 3e: t + s =", exercise3_e())
print("Exercise 3f: s * 2 =", exercise3_f())


print("-----------------------------------------")
print("Exercise 4 + 5:")
print("-----------------------------------------")




def littleProgramThatAsksTheUser():
    print("Please enter a number: ")
    userInput1 = input()
    print("Please enter another number: ")
    userInput2 = input()
    print("-----------------------------------------")
    print(tabulate([["Number 1", userInput1], ["Number 2", userInput2], ["---------","---------"], ["Sum", int(userInput1) + int(userInput2)], ["Difference", int(userInput1) - int(userInput2)], ["Product", int(userInput1) * int(userInput2)], ["Average", (int(userInput1) + int(userInput2)) / 2], ["Distance", abs(int(userInput1) - int(userInput2))], ["Maximum", max(int(userInput1), int(userInput2))], ["Minimum", min(int(userInput1), int(userInput2))]], headers=["Operation", "Result"]))
    print("-----------------------------------------")


littleProgramThatAsksTheUser()


print("-----------------------------------------")
print("Exercise 6:")
print("-----------------------------------------")


def areaAndPerimeterOfARectangle():
    print("Please enter the width of the rectangle: ")
    width = input()
    print("Please enter the height of the rectangle: ")
    height = input()
    print("-----------------------------------------")

    print("Area:      %.2f" % (float(width) * float(height)))
    print("Perimeter: %.2f" % (2 * (float(width) + float(height))))
    print("-----------------------------------------")


areaAndPerimeterOfARectangle()


def seperateANumber():
    print("Please enter a number with more than one digit: ")
    number = input()
    output= ""
    print("-----------------------------------------")
    for i in number:
        output += i + " "
    print(output)


seperateANumber()
