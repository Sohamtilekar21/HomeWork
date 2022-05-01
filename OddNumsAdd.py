a=int(input("Enter number till which you want sum of odd numbers"))
b=1
counter = 2
while (counter<a+1):
    if(counter%2==1):
        b=b+counter
        counter+=1
    else:
        counter+=1
print(b)
        
        
