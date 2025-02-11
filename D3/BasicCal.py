n1 =int (input("Enter Your Number 1 "))
n2 = int (input ("Enter Your NUmber 2 "))

op = input ("Enter Operation  + ,  - , * ,  / ")
if op == '+':
    print (n1+n2)
    
elif op == '-':
    print (n1-n2)
elif op == '*':
    print (n1*n2)

elif op == '/':
    if n2 == 0 :
        print ("Enter valid number")
        print ("Progarm Close")
    else :    print(n1/n2)


    
    