# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print("car started")
# class bike(vehicle):
#     def start(self):
#         print("bike started")
# c=car()
# b=bike()
# c.start()
# b.start()        
#============================================================================================================================
# class bankaccount:
#     def __init__(self,ano,bal):
#        self.__ano=ano
#        self.__bal=bal
#     def dep(self,amount):
#         self.__bal+=amount
#         print("deposited amount:",amount)
#     def wid(self,amount):
#         if amount<=self.__bal:
#             self.__bal-=amount
#             print("widrawn",amount)
#         else:
#             print("insufficent balance")
#     def balance(self):
#         print("balance:",self.__bal)
# b=bankaccount(6767,5000)
# b.dep(10000)
# b.wid(500)
# b.balance()
#============================================================================================================================
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.__salary)
class permanent_employee(employee):
    def display(self):
        print("permanent employee")
        super().display()
class contract_employee(employee):
    def display(self):
        print("contract employee")
        super().display()
p=permanent_employee("rahul",20000)
c=contract_employee("manu",10000)
p.display()
c.display()
        