a=int(input("Enter :"))
c=0

if a>=10 :
    c=2
else:
    c=1
while a//10>9:
    c+=1
    a=a//10
print(c)
