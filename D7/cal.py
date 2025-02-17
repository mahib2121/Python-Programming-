def summitino(num1, sing, num2):
    reslt = num1 + num2
    print(reslt)


def subtruction(num1, sing, num2):
    reslt = num1 - num2
    print(reslt)


def multi(num1, sing, num2):
    reslt = num1 * num2
    print(reslt)


def dev(num1, sing, num2):
    reslt = num1 / num2
    print(reslt)


while True:
    num1 = float(input("Enter Number 1 : "))
    sing = input("Enter Symbol for calculation: ")
    num2 = float(input("Enter NUmber 2 : "))
    if sing == "+":
        summitino(num1, sing, num2)
    elif sing == "-":
        subtruction(num1, sing, num2)
    elif sing == "*":
        multi(num1, sing, num2)
    elif sing == "/":
        dev(num1, sing, num2)
    else:
        print("Enter valid Number")
        break
