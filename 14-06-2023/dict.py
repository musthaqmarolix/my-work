# d=dict()
# d[10]="aman"
# d[20]="aman"
# d[30]="raju"
# d["ram"]=10
# print(d)


#to update the dict
# d={10:"aman",20:"ravi",30:"ram"}
# d.clear()
# print(d)
# d[100]="eehr"
# d[200]="abc"
# print(d)
# print(id(d))
# d[10]="raju"
# print(id(d))

# d={10:"aman",20:"ravi",30:"ram"}
# del d[10]
# print(d)

# d=dict(({200,"man"},{300,"am"},{400,"a"}))
# print(d)

# d=dict([(100,"rammu"),(300,"rajaram")])

# d={10:"aman",20:"ravi"}
# # print(len(d))
# print(d)
# d.pop(10)
# print(d)
# d.pop(20)
# print(d)
# d.pop(10)
# print(d)


# s=input("enter the string : ")
# i=0
# for x in s:
#     print("for each char present in ",i,"is",x)
#     i+=1

# x=0
# while x<=11:
#     print(x)
#     x+=1

#write a pro to find sum of frist n number  4 =>10

# n=int(input("enter some number to find sum : "))#4
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print("the sum of first ",n," number is :", sum)


# name=""
# while name!="aman":
#     name=input("enter your name to authenticate : ")
# print("Hello aman thank you for authentication")

#aman not is equal to "aman"
#aman equal to aman

#user name and password 

n=int(input("enter the number of student data : "))
d={}
for i in range(n):
    name=input("enter the name of student : ")
    marks=input("enter the marks of student : ")
    d[name]=marks
while True:
    name=input("enter stu name to get marks : ")
    marks=d.get(name,1)
    if marks==1:
        print("student {} name not found in data".format(name))
    else:print("the marks of {} are {}".format(name,marks))
    opt=input("do you want to find another student marks [yes/No]")
    if opt=="no":
        break
print("thank you")
