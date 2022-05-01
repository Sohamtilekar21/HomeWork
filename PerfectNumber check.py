#PERFECT NUMBER CHECKER
f=0
a=int(input("Enter the number to check whether its a perfect number or not :"))
for i in range(1,a):
    if a%i==0:
        f+=i
if a==f:
    print("Perfect number ")
else :
    print("Not")
