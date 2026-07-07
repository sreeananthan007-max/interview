class insufficientfundserror(Exception):
    pass
class invalidamounterror(Exception):
    pass
class accountlockederror(Exception):
    pass
class atm:
    def __init__(self,pin,balance=5000):
        self.pin=pin
        self.balance=balance
    def verify_pin(self):
        c=0
        while c<3:
            p=input("enter pin: ")
            if p==self.pin:
                print("pin verified")
                return
            else:
                print("wrong pin")
                c=c+1
        raise accountlockederror("account locked")
    def deposit(self):
        try:
            a=float(input("enter amount: "))
            if a<=0:
                raise invalidamounterror("invalid amount")
            self.balance=self.balance+a
            print("deposit successful")
        except ValueError:
            raise invalidamounterror("enter numbers only")
    def withdraw(self):
        try:
            a=float(input("enter amount: "))
            if a<=0:
                raise invalidamounterror("invalid amount")
            if a>self.balance:
                raise insufficientfundserror("insufficient balance")
            self.balance=self.balance-a
            print("withdraw successful")
        except ValueError:
            raise invalidamounterror("enter numbers only")
    def check_balance(self):
        print("balance =",self.balance)
    def run_atm(self):
        try:
            self.verify_pin()
            while True:
                print("1.deposit")
                print("2.withdraw")
                print("3.balance")
                print("4.exit")
                ch=int(input("enter choice: "))
                try:
                    if ch==1:
                        self.deposit()
                    elif ch==2:
                        self.withdraw()
                    elif ch==3:
                        self.check_balance()
                    elif ch==4:
                        print("exit")
                        break
                    else:
                        print("invalid choice")
                except invalidamounterror as e:
                    print(e)
                except insufficientfundserror as e:
                    print(e)
        except accountlockederror as e:
            print(e)
        finally:
            print("thank you for using kerala bank atm")
a=atm("1234")
a.run_atm()