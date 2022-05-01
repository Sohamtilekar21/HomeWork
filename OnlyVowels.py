print("Only Vowels")
a=input("Enter any string :  ")
leng=len(a)
counter=leng
while(counter > 0):
    char1=a[counter-1:counter:]
    char1=char1.lower()
    if ((char1=="a") or (char1=="e") or (char1=="i") or (char1=="o") or (char1=="u")):
        counter-=1
    else:
        print("Not a vowel")
        break
    print(a , " is only vowels ")
    break


