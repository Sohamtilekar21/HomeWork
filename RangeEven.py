print("Even Numbers within given range : ")
a=int(input("Enter range start        : "))
b=int(input("Emter range end          : "))
while(a<=b):
    if a%2==0:
        print(a)
        a+=2
    else:
        a+=1
