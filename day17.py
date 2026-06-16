# def m(x):
#     res=[]
#     for i in range(1,11):
#         if i not in x:
#             res.append(i)
#     return res
# n=[1,2,3,4,5,8,9,10]
# print(m(n))

# def a(x):
#     res=[]
#     for i in x:
#         if type(i)==int:
#           res.append(i)
#     return res
# n=[67,"car",76,"bike"]
# print(a(n)) 

# def x(a):
#     res=[]
#     for i in a:
#         if a.count(i)==1:
#             res.append(i)
#     return res
# n=[3,4,5,5,6,7,3,4,3,4]
# print(x(n))

# def m(x):
#     i=list(n)
#     i.sort()
#     return i
# n=("hello")
# print(m(n))

def m(x):
    temp=list(x)
    j=list(x)
    j.sort()
    if temp==j:
     return True
    else:
        return False 
print(m("abc"))
print(m("cvfdf"))