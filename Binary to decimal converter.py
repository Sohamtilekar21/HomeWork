while True:
    print ("Decimal to binary conversion")
    print("Choose 1 for decimal to binary , 2 for binary to decimal")
    a=int(input("Enter your number"))
    if a==1:
        n=int(input("Enter decimal number :"))
        m=bin(n)
        print(m)
        break
    elif a==2:
        n=str(int(input("Enter binary number :")))
        m=int(n,2)
        print(m)
        break
    else:
        print("choose valid number")
