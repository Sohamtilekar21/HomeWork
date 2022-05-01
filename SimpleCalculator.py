a=int(input("Enter your number"))
b=int(input("Enter your second number"))
c=int(input("Enter 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Qoutient\n 5 for Remainder\n 6 for Exponents"))
if (c==1):
    print(a+b)
elif (c==2):
    print(a-b)
elif (c==3):
    print(a*b)
elif (c==4):
    print(a/b)
elif (c==5):
    print(a%b)
elif (c==6):
    print(a**b)
else :
    print ("invalid ")
