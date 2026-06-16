# for i in range(1,11):
#     if i==5:
#         break
#     print(i)    

# for i in range(1,11):
#      if i==5 or i==8:
#          continue
#      print(i)    


# for i in range(6):
#     print("*"*i)


# attempt=3
# while attempt>0:
#     u=input("enter your uid")
#     p=int(input("enter your password"))
#     if u=="admin" and p==12345:
#         print("login")
#         break
#     else:
#         attempt-=1
#         print("invalid password or user name")
#     if attempt==0:
#         print("all attempt failed")
#         break
        
# for i in range(1,21):
#     if i%3==0:
#        continue
#     print(i)


# attempt=3
# while attempt>0: 
#      p=int(input("enter pin"))
#      if p==12345:
#         print("1.check balance")
#         print("2.deposit")
#         print("3.withdraw")
#         print("4.exit")
#         bal=10000
#         c=(int(input("enter your choise")))
#         if c==1:
#            print(bal)
#         elif c==2:
#             i=int(input("enter the amount"))
#             bal+=i
#             print(bal)     
#         elif c==3:
#             i=int(input("enter the amount"))
#             if i>bal:
#               print("insufficient balance") 
#             else:
#                 bal-=i
#                 print(bal)
#         elif c==4:
#             print("exit")
#             break
#         else:
#             print("invaild choise")    
#      else:
#          attempt-=1
#          print("invalid pin")
#      if attempt==0:
#          print("all attempts failed")
#          break


# a=int(input("enter your age"))
# ticket=100
# if a>=60:
#     ticket-=30
#     print("senior citizen",ticket,"rs")
# elif a<=12:
#     ticket-=50
#     print("child",ticket,":rs")
# else:
#     print("adult",ticket,"rs")




while True:
    a=int(input("enter mark of maths"))
    b=int(input("enter mark of english"))
    c=int(input("enter mark of cs"))
    if a and b and c<=100:
        print("choice1.caculate total")
        print("choice2.caculate average")
        print("choice3.check pass/fail")
        print("choice4.show grade")
        print("choice5.exit")
        while True:
            ch=int(input("enter your choice"))
            if ch==1:
               print("total=",a+b+c)
            elif ch==2:
                avg=(a+b+c)/3
                print("average=",avg)
            elif ch==3:
               if a<40 or b<40 or c<40:
                  print("failed")
               else:
                   print("passed")
            elif ch==4:
               avg=(a+b+c)/3
               if avg>=90:
                  print("a grade")
               elif avg>=75:
                  print("b grade")
               elif avg>=50:
                  print("c grade")
               else:
                   print("f")
            elif ch==5:
               print("exiting")
               break
    else:
        print("invalid mark")