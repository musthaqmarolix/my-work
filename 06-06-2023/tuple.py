#Tuple packing
#packing==> grouping into single entity
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)

#tuple unpacking
# t={10,20,30,40}
# a,b,c=t
# print("a",a,"b",b,"c",c)

#tuple comprehensive
# l=(x*x for x in range(1,11))
# print(l)


#set datatype structures
# s=set()
# print(type(s))

# s={30,40,50}
# print(type(s))

# #set is mutable
# #set cannot have indexing and also we cannot use slicing

# s={10,20,30}#stored in the bases of address 

# s={10,20,20,10,50,30,40}
# s={10,20,50,30,40,}
# print(s)

# for x in s:
#     print(s)


# l=['abcabc','abcabc']
# s=set(l)
# print(s)


# s=set('aabbbbcccc')
# print(s)
#set

#list []
#tuple ()
#set {}

# l=[]

# s=set()
# print(type(s))

#indexing is not possiable, slicing is not possiable
#duplicate values are not allowed
#inseration order is not preserved

# s[start_index:end_index:step]

# s={10,10,20,30,40,40,20,30,40}
# print(s[0])
# print(s[0:3])

# s=[10,20,30]
# s.remove(20)
# print(s)
# l=[10,20,30]
# l.append(50)
# print(l)

# s={10,20,30,40}
# fs=frozenset(s)
# print(fs)


#dict
# d{key:value}
# d={100:'aman',200:"raju",300:"raviteja"}
# print(d[300])

# d={}
# d["aman"]="sunny"
# d[20]="sunny"
# d[10]="sunny"
# print(d)


# s=set()
# print(type(s))

# l=[10,20,30,40,50]
# print(l[-2:-5:-1])

# for x in range(0,11,2):
#     print(x)

# l="python is very hard language"
# print(l[0:6])#end -1 6-1

# s={100:"aman"}
# print(type(s))

# s=set()
# s.add(10)
# s.add(20)
# s.add(30)
# s.add(30)
# s.add(50)
# print(s)

s={10,20,30,40}
l=[50,60,70,70]
s.update(10,20,3060,80)

print(s)
