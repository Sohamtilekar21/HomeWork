p=float(input("Enter principal Amount : "))
r=float(input("Enter Rate of interest : "))
t=float(input("Enter time in Years    : "))

def SI_CALC(p,r,t):
    si=(p*r*t)/100
    amt=p+si
    print(si ,"is simpple interest")
    print(si+p,"is total amt")
SI_CALC(p,r,t)
 
