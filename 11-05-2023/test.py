# s="mohan is good boy"
# print(s[1:5:2])
# print(len())
#list
# l=[10,20,30,40,'aman']
# print(l.append(None))

#tuple

# t=(10,20,[5
# 0,30],30)
# print(t[2])

#range

# range(10,20) 

# s={10,20,30}
# print(s.remove(20))
# print(s)

#dict

# d={1:"abc",2:"ced"}
# print(d[1])

# if x:
#     action-1
# elif:
#     action-2
# elif:
# action-3
# else:
# action-4

# n1=int(input('enter the number'))
# n2=int(input('enter the number'))
# if n1>n2:
#     print("the bigger number is ", n1)
# else:
#     print("the bigger number is ",n2)

# #selection statements
# name=input("enter your name")

#s=input("enter the string ")
# if n>=1 and n<=100:
#     print("the number",n, " is in between 1 and 100")
# else:
#     print("the number" , n , "is not in b/w 1 and 100")
     

# if n==0:
#     print("zero")
# elif n==1:
#     print("one")
# elif n==2:
#     print("two")
# else:print("enter number from 0 to 1 only")

# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# output=''.join(l)
# print(output)


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#     *
#    ***
# \ *****


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,end=" ")
#     print()

#       *
#      **
#     ***
#    ****
#   *****
#  ******

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
# A A A A A A A A A A A A A A A A A A A A A A A A A A A
# B B B B B B B B B B B B B B B B B B B B B B B B B B B
# C C C C C C C C C C C C C C C C C C C C C C C C C C C
# D D D D D D D D D D D D D D D D D D D D D D D D D D D
# E E E E E E E E E E E E E E E E E E E E E E E E E E E
# F F F F F F F F F F F F F F F F F F F F F F F F F F F
# G G G G G G G G G G G G G G G G G G G G G G G G G G G
# H H H H H H H H H H H H H H H H H H H H H H H H H H H



# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#      * 
#    * * 
#   * * * 
#  * * * *
# * * * * *



# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),(str(i)+" ")*i)
# print()
#      1
#     2 2
#    3 3 3
#   4 4 4 4
#  5 5 5 5 5



# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,end=" ")
#     print()
#      *
#     **
#    ***
#   ****
#  *****


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for x in range(1,n+1):
    print(" "*(n-x),end=" ")
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5