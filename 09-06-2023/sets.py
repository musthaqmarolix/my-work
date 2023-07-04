#math operations
# s1={10,20,30,40}
# s2={30,40,50,60}
# print(s1.union(s2))
# print(s1|s2)

# print(s1.intersection(s2))
# print(s1&s2)

# print(s1.difference(s2))
# print(s1-s2)

# print(s1.symmetric_difference(s2))
# print(s1^s2)

# s1=set('aman')
# # print(s1)
# print('m' in s1)


#list comprehensive
# l={x for x in range(1,11)}
# # print(l)
# print(l[0])
# print(l[0:6])

#program to remove duplicates elements from the given list
# l=eval(input("enter input :"))
# # print(l)
# s=set(l)
# print(s)
# l=int(input("enter :"))
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)


#dictionay 

# d={10: 'aman', 20: 'man', 30: 'boy', 40: 'aman', 'bindu': 10}
# print(d[10])

# s={10:"aman",20:"47"}
# print(s[10])
# # print(s.get(10))
# # print(s[30])
# # print(d.has_key(10))


# a=int(input("enter the first number: ")) #string type "10"
# b=int(input("Enetr the second value: "))
# if a<b:
#     print("a is less than b")
# else:
#     print("a is greater than b")


#identity operator

# a=10
# b=10
# print(a is not b )
# # print(id(a))
# # print(id(b))


# membership operator

# l1=[10,20,30]
# print(20 not in l1)


# a=int(input("enter the something : "))
# b=int(input("enter the something : "))
# print("sum of ",a+b)
# print(type(a))


# a=input("enter the something : ")
# b=input("enter the something : ")
# c=eval(a+b)
# print(c)

# print(type(a))


# x=eval("10+20+30.90")
# print(x)
# output statements
# print("hello \n aman")
# print("hello \t aman")
# print("hello"+"aman")
# print("hello"*aman)
# print("hello","aman")


# a,b,c=10,20,30
# print(a,b,c,sep=":")

# 10,20,30

# print("hello",end="")
# print("aman")


# Flow control
#At run time in which order the statements are going to be executed is decied by flow control


#syntax 
# if x:
#     action-1
# else:
#     action2


# n=input("enter the name :") #raju
# if n=="aman":
#     print("hello aman")
# else:print(n," is wrong user")


# if elif else

# beers=input(" Enter your brand of beers :") #blackdog
# if beers=="kf":
#     print("KF is availabvle")
# elif beers=="boom":
#     print("boom is available")
# elif beers=="rs":
#     print("RS is available")
# elif beers=="rc":
#     print("RC is available")
# else:print(beers,"Stock is not available")

#write a program to find biggest of given two numbers
# n1=int(input(" enter the first number : ")) #100
# n2=int(input(" enter the second number : ")) #200
# if (n1>n2):
#     print("biggest number is: ",n1)
# else:print("biggest number is ",n2)

#iterative statements
#for loop

# s="sunny"
# count=0
# for x in s:
#     count+=1
#     print(x,end=" ")
# print("the number of characters ",count)

# s=input("enter the any string : ") #salman bhai
# i=0
# for x in s:
#     print("for each charecter present in ",i,"is",x)
#     i+=1


#print vara prasad 10 times using loop

# for x in range(10):
#     print("vara prasad")

# print 0 - 20 only even numbers
# for x in range(21):
#     if x%2==0:
#         print(x)

# infinate loop
# x=1
# while x<=10:
#     print(x)
#     x+=1

d=dict({(10,"aman"),(20,"shannu")})
del d
d[100]="raju"
print(d)
# print(d)
# d.clear()
# print(d)
# s=sum(d.keys())
# print(s)