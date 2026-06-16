# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# numbers=[1,2,3,4,5]
# even_no=list(filter(even,numbers))
# print("orginal no=",numbers)
# print("even no=",even_no)    



# def odd(n):
#     if n%2!=0:
#         return True
#     else:
#         return False
# numbers=[1,2,3,4,5]
# odd_no=list(filter(odd,numbers))
# print("orginal no=",numbers)
# print("even no=",odd_no)    


# def sq(n):
#     return n*n
# num=[1,2,3,4,6]
# squre=list(map(sq,num))
# print("orginal no:",num)
# print("squre of no:",squre)


# def upp(words):
#     return words.upper()
# word=["apple","orange","banana"]
# uppercase=list(map(upp,word))
# print("orginal word",word)
# print("words in uppercase",uppercase)


# sq=lambda x: x*x
# num=5
# print("squre=",sq(num))

# add=lambda a,b,c:a+b+c
# print("sum=",add(10,10,30))


# n=[1,2,3,4,5]
# sq=list(map(lambda x:x*x,n))
# print("squre",sq)



# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n - 1)

# print("Factorial:", fact(5))



def prime(n, i=2):
    
    if n<=1:
        return False
    
    if i==n:
        return True
    
    if n%i== 0:
        return False
    
    return prime(n, i + 1)
n=5

if prime(n):
    print(n,"is Prime number")
else:
    print(n,"is Not Prime number")


