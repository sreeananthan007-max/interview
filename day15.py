#27.write a python program to the largest of 3 no
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if a>b and a<c:
#     print("A is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")

#29.python program to dispaly multiplication table

# n=int(input("enter a number"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


#34.

# a=int(input("enter  mark:"))
# b=int(input("enter  mark:"))
# c=int(input("enter  mark:"))
# d=int(input("enter  mark:"))
# e=int(input("enter  mark:"))
# total=a+b+c+d+e
# print("total=",total)
# avg=total/5
# print("avg=",avg)
# if avg>90:
#     print("grade=a")
# elif avg>80:
#      print("grade=b")
# elif avg>70:
#      print("grade=c")
# elif avg>60:
#     print("grade=d")
# else:
#      print("fail")

#35
# a=int(input("enter a number"))
# if a<=1:
#     print("not prime")
# else:
#     for i in range(2,a):
#         if a%i==0:
#          print("not prime")
#          break
#     else:
#          print("prime")


#36

# n=int(input("enter a number"))
# a=0
# b=1
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(a,end="")


#38
l=int(input("enter l:"))
b=int(input("enter b:"))
r=int(input("enter r:"))
def circ(r):
    return 3.14*r*r
print("area of circle=",circ(r))
def rec(l,b):
    return l*b
print("area of rectangle=",rec(l,b))
