"""dob=input("enter your dob: ")
age=2020 - int(dob)
print(" age= ",age)
print(type (dob))


wip=int (input("enter weight in pounds: "))
wik=wip*0.45
print("weight in kg is :",wik,"kg")
my_str='''Hello Ram 
happy new year
This is cts.
Swaagat nahi karoge hamara'''
print(my_str)

fname=input("Enter first name:")
lname=input("Enter last name:")
#msg1=(fname + '[' + lname + '] is a system admin')
msg2=f' {lname} [{lname}] is a system admin'
print(msg2)



is_rainy=True
if is_rainy:
    print ("It is a rainy day")
print("Enjoy your day")

num=int(input("enter a no."))
if num<0:
    print("Negative Integer")
elif num==0:
    print("zero")
else:
    print("Positive value")


a,b,c=input("Enter num1, num2, num3: ").split()
if a>b and a>c:
    print("Num 1 is greater")
elif b>c and b>a:
    print("Num 2 is greater")
else:
    print("Num 3 is greater")



a = [int(a) for a in input("Enter multiple value: ").split()]
if a[0]>a[1] and a[1]>a[2]:
    print("First is greatest")



num1, num2, num3 =input("Enter 3 values:").split()
a, b, c =[int(x) for x in input("Enter 3 values: ").split()]
print(a,b,c)


for i in range(100,10,-10):
    print(i,end='  ')


a,b=0,1
while b<1000:
    print(b, end=' ')
    a,b=b,b+a


for i in range (2,10):
    c= 0
    for j in range(2, (i-1)):
        if i%j==0:
            c= c+1
    if c== 0:
        print(i,end=",")"""



for i in range (2,10):
    for j in range(2,(i-1)):
        if i%j==0:
            break
    else:
        print(i,end=",")




