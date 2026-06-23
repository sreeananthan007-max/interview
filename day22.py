#Duck typing polymorphism
#============================================================================================================================
# class Dog:
#     def s(self):
#         print("Bark")
# class Cat:
#     def s(self):
#         print("Meow")
# def sound(animal):
#     animal.s()
# d=Dog()
# c=Cat()
# sound(d)
# sound(c)
#============================================================================================================================
#Method over riding
#============================================================================================================================
# class animal:
#     def sound(self):
#         print("animal makes sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class cat(animal):
#     def sound(self):
#         print("cat meows")
# d = dog()
# c = cat()
# d.sound()
# c.sound()
#============================================================================================================================
#OPERATOR OVERLOADING
#============================================================================================================================
# class student:
#     def __init__(self, mark):
#         self.marks=mark
#     def __add__(self,other):                 
#         return self.marks+other.marks
# s1 = student(80)
# s2 = student(90)
# print(s1 + s2)
#============================================================================================================================
#polymorphism with inheritance
#============================================================================================================================
class shape:
    def area(self):
        pass
class circle(shape):
    def area(self):
        print("Area of Circle")
class rectangle(shape):
    def area(self):
        print("Area of Rectangle")
shapes = [circle(),rectangle()]
for s in shapes:
    s.area()
