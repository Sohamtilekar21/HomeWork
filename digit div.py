
a=int(input("Enter number to check if divisible by all its digits : "))
temp=a
dig=1
c=0
while temp%dig==0 and a>0:
    while(a>0):
        dig=a%10
        a=a//10
        if temp%dig==0:
            c+=1                               
        else:
            exit
temp=(str(temp))
if len(temp)==c:
    print( temp ,"is divisible by all its digits")
else:
    print ( temp ,"is not divisible by all of its digits")

