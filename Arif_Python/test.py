class Home_alone:
    def __iter__(self):
        self.u=3
        self.u+=4
        
        return self
 
    
    def __next__(self):
        x=self.u
        self.u*=5
        return x 
myclass=Home_alone()
my=iter(myclass)

print(next(my))
print(next(my))
print(next(my))
print(next(my))

