class atm:
    def __init__(self):
        self.accno="12345"
        self.pin="6767"
        self.bal=50000
    def login(self):
        count=0
        if count<3:
            a=input("enter account no:")
            b=input("enter pin")    
            if a==self.accno and b==self.pin:
                print("login successfull")
                while True:
                     print("1.balance enquiry")
                     print("2.deposit money")
                     print("3.withdraw money")
                     print("4.change pin")
                     print("5.exit")
                     ch=int(input("enter choice"))
                     if ch==1:
                         print("balance=",self.bal)
                     elif ch==2:
                         amount=int(input("enter amount"))
                         self.bal=self.bal+amount
                         print("balance=",self.bal)
                     elif ch==3:
                          amount=int(input("enter amount"))
                          if amount<=self.bal:
                              self.bal=self.bal-amount
                              print("balance=",self.bal)
                          else:
                              print("insufficent balance")
                     elif ch==4:
                         npin=input("enter new pin")
                         if len(npin)==4 and npin.isdigit():
                             self.pin=npin
                             print("pin changed")
                         else:
                             print("pin must be 4 digit")
                     else:
                         print("invalid choice")
                         break
            else:
             count=count+1
             print("wrong pin")
a=atm()
a.login()
                     

