n1 = int(input("Enter Your Number 1: "))
n2 = int(input("Enter Your Number 2: "))
op = input("Enter Operation (+, -, *, /): ")

match op:
    case '+':
        print(n1 + n2)
    case '-':
        print(n1 - n2)
    case '*':
        print(n1 * n2)
    case '/':
        if n2 == 0:
            print("Error: not allowed.")
        else:
            print(n1 / n2)

