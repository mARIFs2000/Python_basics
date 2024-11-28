class Cars:
    def __init__(self,Fname,Lname):
        self.firstname = Fname
        self.lastname = Lname 
    def printname(self):
        print(self.Fname, self.Lname)
    mycar = printname("Innova","Crysta")
    mycar.printname()