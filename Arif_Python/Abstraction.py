# from abc import ABC,abstractmethod
# class avengers(ABC):
#     def strength(self):
#         pass

# class captain_america(avengers):
#     def strength(self):
#         print("strength level is 65/100")
# class iron_man(avengers):
#     def strength(self):
#         print("strength level is 75/100")
# class thor(avengers):
#     def strength(self):
#         print("strength level is 95/100")
# class hulk(avengers):
#     def strength(self):
#         print("strength level is 80/100")

# c= captain_america()
# c.strength()

# i= iron_man()
# i.strength()

# t= thor()
# t.strength()

# h= hulk()
# h.strength()

from abc import ABC,abstractmethod
class supercars(ABC):
    def kmph_0to00(self):
        pass

class lamborghini(supercars):
    def kmph_0to00(self):
        print("timing in 2.8sec")

class ferrari(supercars):
    def kmph_0to00(self):
        print("timing in 2.6sec")

class porsche(supercars):
    def kmph_0to00(self):
        print("timing in 3.6sec")

class bugatti(supercars):
    def kmph_0to00(self):
        print("timing in 2.4sec")

l= lamborghini()
l.kmph_0to00()

f= ferrari()
f.kmph_0to00()

p= porsche()
p.kmph_0to00()

b= bugatti()
b.kmph_0to00()
  