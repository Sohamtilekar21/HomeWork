a=[]
print( "Enter 1 if you want to add items to list , 2 to quit")
c=int(input(" 1 OR 2"))
while c==1:
   
    b=int(input("Enter your item"))
    if b>0:
        a.append(b)
  
    print( "Enter 1 if you want to add items to list , 2 to quit")
    c=int(input(" 1 OR 2"))

print(a)
