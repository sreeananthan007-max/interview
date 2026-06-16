# shiping_charge=100
# def total(n):
#     if n>=1000:
#         return n
#     else:
#         return n+shiping_charge
# i=input("enter name:")
# n=int(input("enter the price:"))
# print("name:",i)
# print("amount:",n)
# print("total:",total(n))

# consulting_fee=500
# def total(age):
#     if age>=60:
#         return consulting_fee-(consulting_fee*20)/100
#     else:
#         return consulting_fee
# n=input("enter name:")
# age=int(input("enter age:"))
# print("name:",n)
# print("age:",age)
# print("consulting fee:",consulting_fee)
# print("total amount=",total(age))
    
# bonus=10
# def cal_bounus(s):
#     bon=s*bonus/100
#     return bon
# def total_salary(s):
#     total=s+cal_bounus(s)
#     return total
# n=input("enter name:")
# s=int(input("enter salary:"))
# print("name:",n)
# print("salary",s)
# print("bonus:",cal_bounus(s))
# print("total salary:",total_salary(s))


# gst=0.05
# def bill(*n):
#     total=sum(n)
#     gstrate=total*gst
#     final_bill=total+gstrate
#     return total,gstrate,final_bill
# n1=int(input("enter price of item"))
# n2=int(input("enter price of item"))
# n3=int(input("enter price of item"))
# n4=int(input("enter price of item"))
# n5=int(input("enter price of item"))
# total,gstrate,final_bill=bill(n1,n2,n3,n4,n5)
# print("bill:",total)
# print("gst:",gstrate)
# print("finalbill:",final_bill)


t=200
def total_cost(age,t):
    if age<12:
        price=t*0.5
        return price
    elif age>=60:
        price=t*0.7
        return price
    else:
        price=t
        return price
name = input("Enter Customer Name:")
age = int(input("Enter Age: "))
print("Name:",name)
print("Age:",age)
print("ticket price",t)
print("Final Amount:",total_cost(age,t))

