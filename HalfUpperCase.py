print("Enter any word to display First Half in Upper Case")
a=input()
leng=(len(a))
if (leng%2==0):
    firstPart=(a[0:int(float((len(a)/2))):])
    secondPart=(a[int(float((len(a)/2))):len(a):1])
    print(firstPart.upper()+secondPart.lower())
else :
    print("enter word with even letters")
    

