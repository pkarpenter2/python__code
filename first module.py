first_name = "tony"
last_name  = "stark"
age = 51
is_genious = True
print(first_name)
print(last_name)
print(age)
print(is_genious)



name = input("what is your name ? ")
print("hello " + name)



old_age = input("Enter your old age : ")
new_age = int(old_age) + 5
print(new_age)



first = input("Enter first number")
scound = input("Enter scound number")
sum = int(first) + int(scound)
print(sum)
print("the total number is "+ str(sum))



name = "Pramod Carpenter"
print (name.upper())
print (name.lower())
print(name.find('C'))
print(name.find('Carpenter'))
print(name.replace('Carpenter' , 'Karpenter'))



name = "Pramod karpenter"
print('karpenter' in name)
print('m' in name)
print('Kanchan' in name)
print('Others' in name)
print(name.find('C'))



  #ADD
print(5+3)

   SUBRECTION
print(5-3)

   MULTIPLY
print(5*3)

   DIVIDE jab double // use krege to only int. part
print(5/3)

   RIMNEDER
print(25%3)

   POWER
print(5**3)


#  condisional statement


age = 12


if age >= 18:
    print("your are adult ")
    print("you can vote")
elif age < 18 and age >= 5 :
    print("your are in school")
else :
    print("your are 5 yrae old")




first = input("Enter first number : ")
operator = input("Enter operator (+,-,*,/,%,**) : ")
scound = input("Enter scound number : ")

if operator == "+" :
    print("This is addition operation : ")
    print(int(first) + int(scound))
elif operator == "-" :
    print("This is subtraction operation : ")
    print(int(first) - int(scound))
elif operator == "*" :
    print("This is Multiply operation : ")
    print(int(first) * int(scound))
elif operator == "/" :
    print("This is Divide operation : ")
    print(int(first) / int(scound))
elif operator == "%" :
    print("This is modaulo operation : ")
    print(int(first) % int(scound))
else :
    print("This is power operation : ")
    print(int(first) ** int(scound))



i = 1
while i<=5 :
    print(i * "*")
    i = i+1

print("revese ")
i = 5
while i>=1 :
    print(i * "*")
    i = i-1




for i  in range(6):
   print(i* '*')


marks = [54, 34, 28, 'pramod', 'raj', 'nitesh']


marks.append(55)
marks.insert(0,34)

for i in range(7):
    print(marks[i])




print("pramod")
per = input("Enter your marks : ")
if  (int(per) >= 75) :
    print("your are first devision A ")
elif  (int(per)>=60) :
    print("you are Secound devision : B ")
elif (int(per)>=45) :
    print("you are trird devision : C ")
elif (int(per)>=33) :
    print("you are forth devision : D ")
else :
    print("you are fail : F ")



#calculator

A = int(input("Enter the value one : "))
B = int(input("Enter the value two : "))
opr = input("Enter the operator: ")

if  (opr == '+') :
    print("Addition")
    print(A+B)
elif  (opr == '-') :
    print("Subatraction")
    print(A-B)
elif (opr == '*') :
    print("Multiple")
    print(A*B)
elif (opr == '/') :
    print("Devide")
    print(A/B)
elif (opr == '**') :
    print("Power")
    print(A**B)
else :
    print("Modulo")
    print(A%B)

per = input("Enter the marks : ")
print()

if (int(per) >= 75) :
   print("you are first devision : A ")
elif (per>=60 && per<=74) :
   print("you are Secound devision : B ")
elif (per>=45 && per<=69) :
   print("you are trird devision : C ")
elif (per>=33 && per<=44) :
   print("you are forth devision : D ")
else :
   print("you are fail : F ")



for i in range(100):
   print(i)

for i  in range(6):
    print(i* '*')

num = [6,5,4,3,2,1]
sort(num)

for i in range(0,11,2):
   print(i)



for i  in range(6):
    print(i* '*')


i=1
while(i<=10) :
   print(i)
   i=i+1

print(i)

#+ symbol use for concation######     STRING       ###############

























































