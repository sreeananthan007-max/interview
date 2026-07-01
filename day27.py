class vehicle:
    def __init__(self,vid,vname,brand,rent):
        self.vid=vid
        self.vname=vname
        self.brand=brand
        self.rent=rent
    def dispaly(self):
        print("vehicle id:",self.vid)
        print("vehicle name:",self.vname)
        print("vehicle brand:",self.brand)
        print("vehicle rent:",self.rent)
class car(vehicle):
    def __init__(self, vid, vname, brand, rent,seat,fuel):
        super().__init__(vid, vname, brand, rent)
        self.seat=seat
        self.fuel=fuel
    def dispaly(self):
        super().dispaly()
        print("seats:",self.seat)
        print("fuel type:",self.fuel)
    def amount(self):
        d=int(input("enter the days"))
        print("total rent amount:",self.rent*d)
class bike(vehicle):
    def __init__(self, vid, vname, brand, rent,cc,helmet):
        super().__init__(vid, vname, brand, rent)
        self.cc=cc
        self.helmet=helmet
    def dispaly(self):
        super().dispaly()
        print("cc:",self.cc)
        print("helmet:",self.helmet)
    def amount(self):
        d=int(input("enter the days"))
        print("total rent amount:",self.rent*d)
c=None
b=None
while True:
    print("1.add car")
    print("2.add bike")
    print("3.display car")
    print("4.display bike")
    print("5.car rent amount")
    print("6.bike rent amount")
    print("7.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        vid=input("enter vehicle id:")
        vname=input("enter vehicle name:")
        brand=input("vehicle brand:")
        rent=int(input("enter rent per day:"))
        seat=int(input("enter no.of seats:"))
        fuel=input("enter fuel type:")
        c=car(vid,vname,brand,rent,seat,fuel)
    elif ch==2:
        vid=input("enter vehicle id:")
        vname=input("enter vehicle name:")
        brand=input("vehicle brand:")
        rent=int(input("enter rent per day:"))
        cc=int(input("enter cc"))
        helmet=int(input("enter no.of helmet"))
        b=bike(vid,vname,brand,rent,cc,helmet)
    elif ch==3:
        if c:
            c.dispaly()
        else:
            print("no car found")
    elif ch==4:
        if b:
            b.dispaly()
        else:
            print("no bike found")
    elif ch==5:
        if c:
            c.amount()
        else:
            print("no car found")
    elif ch==6:
        if b:
            b.amount()
        else:
            print("no car found")
    elif ch==7:
        print("thank you")
        break
    else:
       print("invalid choice") 
                