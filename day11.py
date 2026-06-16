# def employee(name,salary=15000):
#     print(name,salary)
# employee("sree",25000)
# employee("akhil")



# def movie(name,rating=5):
#     print(name,rating)
# movie("dune",4)
# movie("fight club")


# def mul(a,b):
#     m=a*b
#     print(m)

# mul(4,5)

# def name(a,b):
#     x=a+b
#     print(x)
# name("sree","padmanabhan")



# def student(name,age):
#     print("name=",name)
#     print("age=",age)
# student(age=21,name="sree")

# def s(*n):
#     sum=0
#     for i in n:
#        sum=sum+i
#     print(sum)
# s(1,2,3,4,5)

# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# print("maximum=",max(10,20))
    

name=input("enter name:")
rollno=int(input("enter rollno:"))
m=[]
for i in range(1,6):
    x=int(input("enter mark:"))
    m.append(x)
att=float(input("enter attendence %:"))
def total_mark(*m):
    total=0
    for i in m:
        total=total+i
    return total
print("total mark=",total_mark(*m))
total=total_mark(*m)
def average_mark(total):
    avg=total/5
    return avg
print("average=",average_mark(total))
avg=average_mark(total)
def grade(avg):
    if avg>=90:
        return "a grade"
    elif avg>=80:
        return"b grade"
    elif avg>=70:
        return"c grade"
    elif avg>=55:
        return"d grade"
    else:
        return"fail"
print("grade=",grade(avg))
def attent(att):
    if att>=75:
        return "eligible for exam"
    else:
        return"not eligible"
print(attent(att))