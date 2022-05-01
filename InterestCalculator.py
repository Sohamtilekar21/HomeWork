print("Interest Calculator")
a=int(input("Choose \n 1 For Simple Interest \n 2 For Compound Interest"))
if a==1:
    p=float(input("Enter principal Amount : "))
    r=float(input("Enter Rate of interest : "))
    t=float(input("Enter time in Years    : "))
    print("Simple Interest is   ",(p*r*t)/100)
    print("Total Amount is      ", p+((p*r*t)/100))
elif a==2: 
     p=float(input("Enter principal        : "))
     r=float(input("Enter Rate of interest : "))
     t=float(input("Enter time in Years    : "))
     compIntTotal=(p*(((100+r)/100))**t)
     print("Compound Interest is    ", (compIntTotal - p)) 
     print("Total Amount is         " , compIntTotal )
else :
    print("Invalid")
    
