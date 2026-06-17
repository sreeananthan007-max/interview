# class atm:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def dep(self,amount,):
#         self.balance += amount
#         print("amount deposited=",amount)
#     def wid(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("amount withdrawn=",amount)
#         else:
#             print("inssuficent balance")
#     def display(self):
#         print("balance=",self.balance)
#     def __del__(self):
#         print("thank you for banking")
# name=input("enter name")
# balance=int(input("enter balance"))
# acc=atm(name,balance)
# while True:
#     print("1.deposit")
#     print("2.withdraw")
#     print("3.check balance")
#     print("4.exit")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         amount=int(input("enter the deposit amount"))
#         acc.dep(amount)
#     elif choice==2:
#         amount=int(input("enter the withdraw amount"))
#         acc.wid(amount)
#     elif choice==3:
#         acc.display()
#     elif choice==4:
#         del acc
#         break
#     else:
#         print("invalid choice")

#--------------------------------------------------------------------------------------------------------------------------------
class hospital:
    def __init__(self,name,age,fee):
        self.name=name
        self.age=age
        self.fee=fee
    def bill(self):
        if self.age>=60:
            b=self.fee-(self.fee*0.20)
        else:
            b=self.fee
        return b
    def dis(self):
        print("name=",self.name)
        print("age=",self.age)
        print("fee=",self.fee)
        print("final bill=",self.bill())
    def __del__(self):
        print("patient record removal")
name=input("enter name")
age=int(input("enter age"))
fee=int(input("enter fee"))
p=hospital(name,age,fee)
print("--------------------------------------------patient details-----------------------------------------------------------")
p.dis()
del p