# x=[]
# s=int(input("enter the no.of students"))
# for i in range(s):
#     n=input("enter student name")
#     x.append(n)
# print("list=",x)
# y=input("enter student name to count occurrence")
# c=0
# for i in x:
#     if i==y:
#         c+=1
# print("occurrence=",c)


# a=[]
# for i in range(1,21):
#     a.append(i)
# print(a)

# s=[i**2 for i in range(1,11)]
# print(s)

# l1=[1,2,3,4,5]
# l2=[2,4,5]
# d=[]
# for i in l1:
#     if i not in l2:
#         d.append(i)
# print(d)

# n=int(input("enter no:"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print("revesed is",rev)


# n=int(input("enter a number"))
# temp=n
# num=len(str(n))
# sum=0
# while temp>0:
#     digit=temp%10
#     sum +=digit**num
#     temp=temp//10
# if sum==n:
#     print("is amstrong")
# else:
#     print("not amstrong")

# n=int(input("enter a number"))
# a=0
# b=1
# for i in range(n):
#    print(a,end="")
#    c=a+b
#    a=b
#    b=c

# n=int(input("enetr a number"))
# for i in range(2,n+1):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#         print(i,end="")




# l=[1,2,3,4]
# total=0
# for i in l:
#     total+=i
# print(total)

l=input("enter a no")
n=list(l)
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print("largest element is:",largest)




