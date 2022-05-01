x=int(input("Enter"))

def a(x):
    
    x=abs(x)
    b=x%10
    if b<10 and x>0:
        return 1
    return (1 + a(x/10))

print(a(x))
