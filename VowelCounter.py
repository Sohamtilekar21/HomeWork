print("Vowel Counter")
a=input("Enter your sentence : ")
vc=0
ac=int(len(a))
while(ac>0):
    char1=a[(ac-1):(ac):]
    ac=ac-1
    if ((char1=="a") or (char1=="e") or (char1=="i") or (char1=="o") or (char1=="u")):
        vc=vc+1
print(vc , " is the number of vowels in " , a)
