print("Odd Numbers within given range")
a=int(input("Enter range start"))
b=int(input("Emter range end"))
for i in range(a,b+1):
    if i%2==1:
        print(i)
