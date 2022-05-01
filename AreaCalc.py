print("area Caluculator")
def square():
    b=int(input("Enter side : "))
    
    print("area of square is  ",b*b)
    
def rectangle():
    b=int(input("Enter length: "))
    c=int(input("Enter breadth: "))
    print("area of rectangle is ",c*b)
    
def circle():
    b=int(input("Enter Radius: "))
    print("area of circle is ",22/7*b*b)
    


def triangle():
    b=int(input("Enter base: "))
    f=int(input("Enter Height: "))
    print("area of triangle is ",1/2*f*b)
    
    
a=int(input("Enter \n\t 1 for sqyare\n\t 2 for rectangle\n\t 3 for circle\n\t 4 for triangle"))
if (a==1):
    square()
elif (a==2):
    rectangle()
elif (a==3):
    circle()
elif (a==4):
    triangle()

else :
    print ("invalid ")
