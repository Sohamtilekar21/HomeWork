print("Temperature Converter")
a=float(input("Enter Temperature here "))
b=int(input("Choose 1 for farenheit to celsius , 2 for celsius to farenheit"))
if b==2:
    print((a*9/5)+32)
elif b==1:
    print((a-32)*5/9)
else:
    print("Invalid")
