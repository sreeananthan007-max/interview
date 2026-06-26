# class student:
#    def __init__(self,sid,name,course):
#      self.sid=sid
#      self.name=name
#      self.course=course
#    def display(self):
#       print("student id:",self.sid)
#       print("name:",self.name)
#       print("course",self.course)
# s1=student(1,"manu","java")
# s2=student(2,"akhil","python")
# s3=student(3,"amal","c++")
# s1.display()
# s2.display()
# s3.display()
#===========================================================================================================================
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class doctor(person):
#     def __init__(self, name, age,spe,exp):
#         super().__init__(name, age)        
#         self.spe=spe
#         self.exp=exp
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("specialized:",self.spe)
#         print("experince:",self.exp)
# p=doctor("manu",46,"ortho","10 years")
# p.display()
#===========================================================================================================================
class payment:
    def pay(self):
        print("payment is done")
class creditcard(payment):
    def pay(self):
        print("payment using credit card")
class upi(payment):
    def pay(self):
        print("payment using upi")
class cash(payment):
    def pay(self):
        print("payment using cash")
p1=creditcard()
p2=upi()
p3=cash()
p1.pay()
p2.pay()
p3.pay()