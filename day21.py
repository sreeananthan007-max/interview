# class person:
#     def __init__(self,name):
#        self.name=name
# class student(person):
#     def __init__(self, name,rollno):
#         super().__init__(name)    
#         self.rollno=rollno
#     def display(self):
#         print("name=",self.name)
#         print("rollno=",self.rollno)
# class teacher(person):
#     def __init__(self, name,sub):
#         super().__init__(name)
#         self.sub=sub
#     def display(self):
#         print("name=",self.name)
#         print("sub=",self.sub)
# s=student("rahul",67)
# t=teacher("rose","computer")
# s.display()
# t.display()
#-----------------------------------------------------------------------------------------------------------------------------
class employee:
    def __init__(self,name):
        self.name=name
class developer(employee):
    def __init__(self,name,lang):
        employee.__init__(self,name)
        self.lang=lang
class tester(employee):
    def __init__(self,name,tool):
        employee.__init__(self,name)
        self.tool=tool
class teamlead(developer,tester):
    def __init__(self,name,lang,tool):
        developer.__init__(self,name,lang)
        tester.__init__(self,name,tool)
    def display(self):
        print("name=",self.name)
        print("language=",self.lang)
        print("tool=",self.tool)
t=teamlead("akhil","python","tool needed")
t.display()