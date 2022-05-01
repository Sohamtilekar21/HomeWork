class person:
    def __init__(self, name , age):
        self.name=name
        self.age=age
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
class student(person):
    def __init__(self,name,age,course):
        person.__init__(self,name,age)
        self.course=course
    def show(self):
        person.display(self)
        print("Course :",self.course)
a=person('Om',20)
a.display()
print()
b=student('Soham',16,'Science')
b.show()
        
