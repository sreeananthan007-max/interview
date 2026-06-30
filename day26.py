# class employee:
#     def __init__(self,empid,name,basic,hra,da,tax):
#         self.empid=empid
#         self.name=name
#         self.basic=basic
#         self.hra=hra
#         self.da=da
#         self.tax=tax
#     def grosss(self):
#         return self.basic+self.hra+self.da
#     def net(self):
#         gross=self.grosss()
#         tax_a=self.gross*self.tax/100
#         return gross-tax_a
#     def display(self):
#         print("empolyee id:",self.empid)        
#         print("name:",self.name)
#         print("basic salary:",self.basic)
#         print("hra:",self.hra)
#         print("da:",self.da)
#         print("tax:",self.tax) 
# employees=[]
# while True:
#     print("1.add employee")
#     print("2.display all employee")
#     print("3.search by id")
#     print("4.update details")
#     print("5.calculate gross salary")
#     print("6.calculate net salary")
#     print("7.employee wit highest salary")
#     print("8.exit")
#     ch=int(input("enter choice"))
#     if ch==1:
#         empid=int(input("enter id:"))
#         name=(input("enter name:"))
#         basic=float(input("enter basic salary:"))
#         har=float(input("hra:"))
#         da=float(input("enter da:"))
#         tax=float(input("enter tax:"))
#         emp=employee(empid,name,basic,har,da,tax)
#         employees.append(emp)
#         print("employee added")
#     elif ch==2:
#         if len(employees)==0:
#             print("employee not found")
#         else:
#             for emp in employees:
#                 emp.display()
#     elif ch==3:
#         searchid=int(input("enter id:"))
#         found=False
#         for emp in employees:
#             if emp.empid==searchid:
#                 emp.display()
#                 found=True        
#                 break
#         if not found:
#             print("employee not found")
#     elif ch==4:
#         searchid=int(input("enter id:"))
#         found=False
#         for emp in employees:
#             if emp.empid==searchid:
#                 emp.basic=float(input("enter new basic salary:"))
#                 emp.hra = float(input("enter new hra:"))
#                 emp.da = float(input("enter new da:"))
#                 emp.tax = float(input("enter new tax:"))
#                 print("salary details Updated")
#                 found=True
#                 break
#         if not found:
#             print("employee not found")
#     elif ch==5:
#         searchid=int(input("enter employee id:"))
#         found = False
#         for emp in employees:
#             if emp.empid==searchid:
#                 print("Gross Salary =",emp.grosss())
#                 found=True
#                 break
#         if not found:
#             print("employee not found")
#     elif ch==6:
#         searchid=int(input("enter employee iD:"))
#         found=False
#         for emp in employees:
#             if emp.empid==searchid:
#                 print("net salary =",emp.net())
#                 found=True
#                 break
#         if not found:
#             print("employee not found.")
#     elif ch==7:
#         if len(employees)==0:
#             print("no employees found.")
#         else:
#             highest=employees[0]
#             for emp in employees:
#                 if emp.net() > highest.net():
#                     highest=emp

#             print("employee with highest net salary")
#             highest.display()
#             print("Net Salary =",highest.net())

#     elif ch == 8:
#         print("Thank You!")
#         break

#     else:
#         print("Invalid Choice.")
#===============================================================================================================================
class student:
    def __init__(self,roll,name,course,m1,m2,m3,m4,m5):
        self.roll=roll
        self.name=name
        self.course=course
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def total(self):
        return self.m1+self.m2+self.m3+self.m4+self.m5
    def average(self):
        return self.total()/5
    def grade(self):
        avg=self.average()
        if avg>=90:
            return "a"
        elif avg>=75:
            return "b"
        elif avg>=50:
            return "c"
        else:
            return "fail"
    def display(self):
        print("roll no:",self.roll)
        print("name:",self.name)
        print("course:",self.course)
        print("marks:",self.m1,self.m2,self.m3,self.m4,self.m5)
students=[]
while True:
    print("1.add student")
    print("2.display student")
    print("3.total marks")
    print("4.average marks")
    print("5.grade")
    print("6.topper")
    print("7.failed students")
    print("8.sort students")
    print("9.exit")
    ch=int(input("enter choice:"))
    if ch==1:
        roll=int(input("enter roll no:"))
        name=input("enter name:")
        course=input("enter course:")
        m1=int(input("enter mark1:"))
        m2=int(input("enter mark2:"))
        m3=int(input("enter mark3:"))
        m4=int(input("enter mark4:"))
        m5=int(input("enter mark5:"))
        s=student(roll,name,course,m1,m2,m3,m4,m5)
        students.append(s)
    elif ch==2:
        for s in students:
            s.display()
    elif ch==3:
        roll=int(input("enter roll no:"))
        for s in students:
            if s.roll==roll:
                print(s.total())
    elif ch==4:
        roll=int(input("enter roll no:"))
        for s in students:
            if s.roll==roll:
                print(s.average())
    elif ch==5:
        roll=int(input("enter roll no:"))
        for s in students:
            if s.roll==roll:
                print(s.grade())
    elif ch==6:
        top=students[0]
        for s in students:
            if s.average()>top.average():
                top=s
        top.display()
    elif ch==7:
        for s in students:
            if s.average()<50:
                s.display()
    elif ch==8:
        students.sort(key=lambda x:x.average(),reverse=True)
        for s in students:
            print(s.roll,s.name,s.average())
    elif ch==9:
        break
    else:
        print("invalid choice")