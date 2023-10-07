print("pk")
######         nested dictonary

course = {
'php   ' : { 'duration' : '1 months', 'fees' : 12000 },

'pyhton' : { 'duration' : '2 months', 'fees' : 11000 },

'cpp   ' : { 'duration' : '3 months', 'fees' : 14000 },

'java  ' : { 'duration' : '4 months', 'fees' : 15000 },

'html  ' : { 'duration' : '5 months', 'fees' : 16000 },

'css   ' : { 'duration' : '6 months', 'fees' : 17000 }

}

print(course)
print()

print(course['php   '])


print()
print(course['php   ']['fees'])
print()

for i,j in course.items():
    print(i,j)

for i,j in course.items():
    print(i,j['duration'],j['fees'])

################  tuple
# it is orderd data type & it is imnutable list ke compair me tuple fasr work krta hai


t = (10,10,20,30,40,50)
print(t)
print(t.index(40))
print(sum(t))

for a in range(len(t)):
    print(a)

for a in range(5):
    print(a)

for a in range(5):
    print(t[a])

for a in t:
    print(a)

print("sum function")
print(sum(t))
print()

print("min function")
print(min(t))
print()

print("max function")
print(max(t))
print()

print("count function")
print(t.count(10))
print()

print("index function")
print(t.index(40))
print()


############     SETS

s = {10,20,30,40,50,60,}
print(s)
print()

print("ADD FUN")
s.add(120)
print(s)


print(print("POP FUN"))
print(s.pop())
print()

print(print("REMOVE FUN"))
print(s.remove(30))
print(s)
print()

print(print("DISCARD FUN"))
print(s.discard(120))
print(s)
print()

print(print("CLEAR FUN"))
print(s.clear())
print(s)
print()


l = {90,80,70,60,20}
print(print("UPDATE FUN"))
print(s.update(l))
print(s)
print()

##############   USER DEFINE FUNCTION

def simple_fun():
    print("pramod karpenter")
    print("karpenter pramod")
simple_fun()



def sum(a,b=30):
    c=a+b
    print(c)

sum(10)
sum(20,20)

def sum_(a,b):
    c=a+b
    return c

op = sum_(110,30)
print(op)

##################   MODULE


def  sun(a,b):
    c=a+b
    return c

def  multi(a,b):
    c=a*b
    return c


whem call this one then name of module like....

    from module1 import sum
    print(sum(20,30))

    import module1 as m
    print(m.mul(10,20))

    from module1 import *             all function
    pri nt(sum(20,30))


            import math


print("FACTORIAL ")
print(math.ceil(11.2))
print()


print("MODD MEANS ALWAYS POSITIVE VALUE ")
print(math.fabs(-10))
print()


print("FACTORIAL ")
print(math.factorial(5))
print()

print("UPAR KI VALUE ")
print(math.floor(5.2))
print()

L = (12,13,14,14,24,39,67,46,3,7,34,78,357,3,23,6,33,67,34,33,2,35,24,32)
print("SUM OF LIST ")
print(math.fsum(L))
print()

print("UNDER ROOT ")
print(math.sqrt(22))
print()


import random

print("INKE BICH RENDOM NO. DENA")
print(random.randint(2,9))
print()

print("INME SE 9 INCLUDE NHI HOGA")
print(random.randrange(2,9))
print()


L = (12,13,14,14,24,39,67,46,3,7,34,78,357,3,23,6,33,67,34,33,2,35,24,32)
print("KOI V ELEMENT DEGA")
print(random.choice(L))
print()


print("0 to 9 rendom no.")
print(random.random())
print()

print("list ke koi v no. khi pe v ho jate hai ")
l = [10,20,30,40,50]
print(random.shuffle(l))
print()

print("INKE BICH RENDOM floating value DENA")
print(random.uniform(2,9))
print()