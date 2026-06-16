# def s1(a,b,c):
#     m=a+b+c
#     return m
# def s2(d,e,f):
#     m=d+e+f
#     return m
# s1a=int(input("enter s1 mark:"))
# s1b=int(input("enter s1 mark:"))
# s1c=int(input("enter s1 mark:"))
# s2a=int(input("enter s2 mark:"))
# s2b=int(input("enter s2 mark:"))
# s2c=int(input("enter s2 mark:"))

# sem_1=s1(s1a,s1b,s1c)
# sem_2=s2(s2a,s2b,s2c)
# print("s1 mark=",sem_1)
# print("s2 mark=",sem_2)
# total=sem_1+sem_2
# print("total=",total)


# def palindrome(n):
#     rev=0
#     while n>0:
#          digit=n%10
#          rev=rev*10+digit
#          n=n//10
#     return rev
# n=int(input("enter the no"))
# pal=palindrome(n)
# if n==pal:
#      print("palindrome")
# else:
#      print("not palindrome")

# def mul(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",i*n)
# n=int(input("enter a no"))
# mul_table=mul(n)
# print(mul_table)
    
# def rev(n):
#     rev=0
#     while n>0:
#          digit=n%10
#          rev=rev*10+digit
#          n=n//10
#     return rev
# n=int(input("enter the no"))
# reverse=rev(n)
# print("reversed no=",reverse)


# def prime(n):
#      count=0
#      for i in range(1,n+1):
#         if n%i==0:
#            count+=1
#      if count==2:
#          print(n,"is prime")
#      else:
#          print(not prime)
# prime(2)
# prime(8)
    

# def fib(n):
#      a=0
#      b=1
#      for i in range(n):
#          print(a,end="")
#          c=a+b
#          a=b
#          b=c
# n=int(input("enter a no:"))
# fibi=fib(n)
# print(fibi)

# def is_armstrong(num):
#     temp = num
#     total = 0
#     digits = len(str(num))

#     while temp > 0:
#         digit = temp % 10
#         total = total + digit ** digits
#         temp = temp // 10

#     return total == num

# print(is_armstrong(153))


# def factorial(n):
#     fact = 1

#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
# print(factorial(5))


# def large(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input("enter first no"))
# b=int(input("enter second no"))
# lar=large(a,b)
# print("largest=",lar)

def cou(n):
    count=0
    while n>0:
        count += 1
        n=n//10
    return count
print(cou(12345))