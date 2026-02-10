#Write a class "calculator" capable of finding square, cube and square root of a number
class calculator:
    # print(input("Enter number:"))
    
    def __init__(self,n):
        self.n= n
    def square(self):
        print(f"The square  is: {self.n*self.n}")    
    def cube(self):
        print(f"The cube  is: {self.n*self.n*self.n}")    
    def root(self):
        print(f"The square root is: {self.n**1/2}")    
                
        
n= int(input("Enter number:"))    
a = calculator(n)
a.square()
a.cube()
a.root()

       
     
        