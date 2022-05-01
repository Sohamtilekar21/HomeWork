class Stud:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
    def show(self):
        print("name:",self.name)
        print("roll no:",self.roll_no)
        
a=Stud("Soham",1234)
a.show()
