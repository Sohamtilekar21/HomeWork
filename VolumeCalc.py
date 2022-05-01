print("Volume Caluculator")
def cuboid():
    b=int(input("Enter Length  : "))
    c=int(input("Enter Breadth : "))
    d=int(input("Enter Height  : "))
    print("Volume of Cuboid is  ",b*c*d)
    
def cube():
    b=int(input("Enter Side: "))
    print("Volume of Cube is ",b*b*b)
    
def sphere():
    b=int(input("Enter Radius: "))
    print("Volume of Sphere is ",4/3*22/7*b*b*b)
    
def hemisph():
    b=int(input("Enter Radius: "))
    print("Volume of HemiSphere is ",2/3*22/7*b*b*b)

def cone():
    b=int(input("Enter Radius: "))
    f=int(input("Enter Height: "))
    print("Volume of Cone is ",1/3*22/7*f*b*b)
    
    
a=int(input("Enter \n\t 1 for Cuboid\n\t 2 for Cube\n\t 3 for Sphere\n\t 4 for Hemishpere\n\t 5 for Cone\n\t"))
if (a==1):
    cuboid()
elif (a==2):
    cube()
elif (a==3):
    sphere()
elif (a==4):
    hemisph()
elif (a==5):
    cone()
else :
    print ("invalid ")
