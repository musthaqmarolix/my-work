#imp methods of sets
#s.add()

# s=set()
# 
# s.add(20)
# s.add(30)
# s.add()
# print(s)

#update
# s={10,20,30,40}
# l=[10,60,70]
# t=(90,100)
# s.update(l,range(1,5),"aman","musthaq",t)
# print(s)

# s={10,20}
#s.add(89) #valid
#s.add(10,20,30) #invalid # type error
#s.add('phone') #valid #"phone" 
#s.update(10) #invalid
#s.update(range(1,5),range(10,20,2)) #valid
#s.update([10,20,30,50]) #vaild
#s.update(10,20,30) #invalid
#s.update((10,20,30,40)) #valid
#s.update('python','aman') #vaild
#s.update("am"+"an") #


#copy() #to create a duplicate or cloning the object 
# s={10,20,30}
# s1=s.copy()
# print(s1)
# print(id(s))
# print(id(s1))

#pop()
# s={10,20,30}
# print(s.pop())
# print(s.pop())
# print(s.pop())


# s={10,20,30}
# s.remove(100)
# print(s)

#discard()

# s={10,20,30}
# s.discard(10)
# print(s)

# s={10,20,30}
# s.clear()
# print(s)



#python is dynamically programming language

# print("helloword")
# "aman" or 'aman'

# a=10
# b=20
# print(id(a))
# print(id(b))


# a=10
# b=
# print(id(a))
# print(id(b))
# print(id(c))

# # operators:
# a=10
# b=2
# print("a+b",a+b) #30
# print("a-b",a-b) #10
# print("a*b",a*b) #
# print("a/b",a/b)
# print("a moduls b",a%b)
# print("a**b",a**b)

#relational operators
# > < <= >=

# a=10
# b=2
# print("a>b", a>b) #true
# print("a<b", a<b)#fals
# print("a==b", a==b)#false
# print("a<=b", a<=b)#false
# print(a!=10)

# a="Aman"
# b="Aoy"
# print("a>b", a>b)

# unicode A 65 and a 97


# a='Rurga'
# b='Ravi'
# print(a>b)

# Equality operator
# a=10
# b="aman"
# print(a==b) #False
# # 10!=20 #True


# a=eval(input("enter the frist value"))
# b=eval(input("enter the second value"))
# if (a>b):
#     print(a," is greater than ", b)
# else:
#     print(a," is not greater than ",b)

s1={10,20,30}
s2={30,40,50}
print(s1|s2)

