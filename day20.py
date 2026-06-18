# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class manager(employee):
#     def display(self):
#         print("employee name=",self.name)
#         print("employee salary=",self.salary)
# m=manager("akhil",10000)
# m.display()
#---------------------------------------------------------------------------------------------------------------------------

# class school:
#     def __init__(self,sname):
#         self.sname=sname
# class teacher(school):
#     def __init__(self,sname,sub):
#         school.__init__(self,sname)
#         self.sub=sub
# class headteacher(teacher):
#     def __init__(self,sname,sub,exp):
#        teacher.__init__(self,sname,sub)
#        self.exp=exp
#     def display(self):
#         print("school name=",self.sname)
#         print("subject=",self.sub)
#         print("experince=",self.exp)
# h=headteacher("lbs","maths",10)
# h.display()
#------------------------------------------------------------------------------------------------------------------------------
class music_palyer:
    def music(self):
        print("music is palying")
class camera:
    def cam(self):
        print("photo taken")
class smartphone(music_palyer,camera):
    def phone(self):
        print("phone")
s=smartphone()
s.phone()
s.music()
s.cam