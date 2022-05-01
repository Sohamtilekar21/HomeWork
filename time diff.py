print ("Time 1 ")
a=int(input("Enter hours in 24 hour format :"))
if a==0:
    a=24
b=int(input("Enter minutes :"))
print()
print ("Time 2 ")
c=int(input("Enter hours in 24 hour format :"))
if c==0:
    c=24
d=int(input("Enter minutes :"))
a=(a*60)+b
c=(c*60)+d
z=a-c
print()
print("Difference is ",z," Minutes")

