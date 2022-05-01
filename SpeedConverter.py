print("Speed Converter")
a=float(input("Enter Speed Here"))
b=int(input("Choose 1 to convert into m/s , 2 for km/hr"))
if b==1:
    print((a*5)/18)
elif b==2:
    print((a*18)/5)
else :
    print ("Invalid")
