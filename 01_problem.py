#Create a class "Programmer" for storing information of few programmers working at Microsoft

class Programmer:
    company = "Apple"
    def __init__(self, name, salary, pincode):
        self.name= name
        self.salary= salary
        self.pincode= pincode
p = Programmer("Harry", 100000, 3356)     
print(p.name, p.salary, p.pincode)   
        