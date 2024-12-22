import os
import time


def addition():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums)


def subtraction():
    n_1 = float(input("Enter first number: "))
    n_2 = float(input("Enter second number: "))

    return n_1 - n_2


def multiplication():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    result = 1
    for num in nums:
        result *= num
    return result


def division():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if n2 == 0:
        print("Invalid entry")
        return "Invalid entry"
    print(n1 / n2)

    return n1 / n2


def average():
    nums = list(map(int, input("Enter all numbers separated by space: ").split()))
    return sum(nums) / len(nums)


def factorial(num):
    answer = 1
    for i in range(num):
        answer *= i + 1
    return answer

c = 0
while c != "-1":
    print("\nEnter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")
    print("Enter '6' for factorial")
    print("Enter '-1' to exit.\n")

    c = input("Your choice is: ")
    if c == "1":
        res = addition()
    elif c == "2":
        res = subtraction()
    elif c == "3":
        res = multiplication()
    elif c == "4":
        res = division()
        if res == "Invalid entry":
            continue
    elif c == "5":
        res = average()
    elif c == "6":
        num = int(input("enter the number: "))
        if num < 0:
            print("Invalid entry")
            continue
        res = factorial(num)
    elif c == "-1":
        print("Thank you for using the calculator!")
        break
    else:
        print("Sorry, invalid option!")
    print(f"The answer is {res}")
    time.sleep(2)
    os.system("cls||clear")