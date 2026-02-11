#Add a static method in problem 2, to greet the user with hello.
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
    @staticmethod #Here, static method use garepaxi self use garna parena
    def hello():
        print("Hello!!!")  
                
        
n= int(input("Enter number:"))    
a = calculator(n)
a.hello()
a.square()
a.cube()
a.root()

       
     
        