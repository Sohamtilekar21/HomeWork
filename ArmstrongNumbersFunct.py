
a=int(input("Enter the number"))
def Astnr(a):
    temp=a
    b=0
    while a>0:
        c=a%10
        b=b+(c**3)
        a=a//10
    print(bool(b==temp))
Astnr(a)






