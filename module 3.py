class Student:
    n=10
    p=100

    def sum__(self):
        a = int(input("Enter the value of a  :"))
        b = int(input("Enter the value of b  :"))
        c = a+b
        print("this is total" , c)
        self.z = self.n + self.p
        self.x = c + self.n+ self.p
        print("this is n+p", self.z)
        print("this is a+b",c)
        print( "this is total" , self.x)
    def multi(self):
        print()
        a = int(input("Enter the value of a  :"))
        b = int(input("Enter the value of b  :"))
        c = a*b
        print("this is total" , c)
        self.z = self.n * self.p
        self.x = c * self.n * self.p
        print("this is n+p", self.z)
        print("this is a+b",c)
        print("this is total" , self.x)
        print("N*P    ",self.n * self.p)


obj=Student()  # that is called making object


obj.sum__()
obj.multi()


print(obj.n)   # that is called the variable
print(obj.p)







################   contructor


class demo :
    def __init__(self):
        x = "Pramod Karpenter"
        print(x.upper())

obj = demo()


################   inheritence



####            single

print("           SINGLE INHERITENCE   ")
class A:
    def showA(self):
        print("class A")

class B(A):
    def showB(self):
        print("class B")


obj = B()
obj.showA()
obj.showB()

########     multi laval
print ("           MULTI LAVEL INHERITENCE")
class A:
    def showA(self):
        print("class A")
class B(A):
    def showB(self):
        print("class B")
class C(B):
    def showC(self):
        print("class C")
class D(C):
    def showD(self):
        print("class D")


obj =D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()

########        MULTIPLE

print("           MULTIPLE INHERITENCE")
class A:
    def showA(self):
        print("class A")
class B:
    def showB(self):
        print("class B")
class C:
    def showC(self):
        print("class C")
class D(A,B,C):
    def showD(self):
        print("class D")


obj =D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()



###############       geter  seter
class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name


obj = Student()
obj.setname("Pramod karpenter")
name = obj.getname()
print(name)




##########  ENCAPSULTION


class A:
    __name = 100
    def __init__(self):      # making constructor
        print(self.__name)
        self.__fun()         # call the __fun function in constuctor
    def __fun(self):         # private function using '__' then function name
        print("rendom")



obj = A()
#obj.__fun()


































