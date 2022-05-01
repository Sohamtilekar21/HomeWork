a=int(input("Enter number till which you want sum of even numbers"))
b=0
counter = 2
while (counter<a):
    if(counter%2==0):
        b=b+counter
        counter+=1
    else:
        counter+=1
print(b)
        
        
