class animal:
    def __init__(self,name,legs,type):
        self.name=name
        self.legs=legs
        self.type=type
    def show(self):
        print(self.name,"has",self.legs,"legs , and is a ",self.type)
a=animal("Cow",4,"Herbivore")
a.show()
        
