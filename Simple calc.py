def add(a,b):
    sum=a+b
    return sum
def sub(a,b):
    dif=(a-b)
    return dif
def mul(a,b):
    pro=a*b
    return pro
def div(a,b):
    qou=(a/b)
    return qou
a=int(input("Enter your number"))
b=int(input("Enter your second number"))
c=int(input("Enter 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Qoutient\n"))
if (c==1):
    print(add(a,b))
elif (c==2):
    print(sub(a,b))
elif (c==3):
    print(mul(a,b))
elif (c==4):
    print(div(a,b))
else :
    print ("invalid ")
