# n=int(input("enter a number:"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")    


# n=int(input("enter a number:"))
# if n % 2==1:
#     print("odd")
# else:
#     print("even")


# n=int(input("enter age:"))
# c=input("enter contry:")
# if n>=18 and c=="india":
#     print("eligible for voting")
# else:
#     print("not eligible") 


# n=int(input("enter a mark:"))
# if n>=90:
#     print("a grade")
# elif n>=75:
#     print("b grade")
# elif n>=50:
#     print("c grade")
# else:
#     print("fail")


# n=int(input("enter age:"))
# c=input("enter contry:")
# if n>=18 and c=="india":
#     print("eligible for driving in india")
# elif n>=16 and c=="usa":
#     print("eligible for driving in usa")
# else:
#     print("not eligible to drive") 


# for i in range(1,11):
#     print(i)

# for i in range(50,81):
#     print(i)

# for i in range(50,81,5):
#      print(i)


# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(n,"*",i,"=",i*n)


# n=int(input("enter a number:"))
# sum=0
# i=1
# while i<=n:
#      sum=sum+i
#      i=i+1
# print(sum)

print("1.balance")
print("2.deposit")
print("3.withdraw")
print("4.exit")
bal=2000
c=int(input("enteryour choise"))
if c==1:
    print(bal)
elif c==2:
    i=int(input("enter the amount"))
    bal+=i
    print(bal)     
elif c==3:
     i=int(input("enter the amount"))
     if i>bal:
          print("insufficient balance") 
     else:
          bal-=i
          print(bal)
elif c==4:
     print("exit")
else:
     print("invaild choise")     
