a=12
b=20
c=30
d,f,g=1,2,3
h=j=k=100
print(a,b,c,d,f,g,h,j,k)
print(type(a),type(b),type(c),type(d),type(f),type(g),type(h),type(j),type(k))
print(a+b+c)
print(h+j+k)
#variable:variable is a container which holds the value which can be changed during the execution of the program
#we can declare vaiable in many ways like a=10 b=20
#we can declare multiple variables in a single line like a,b,c=10,20,30
#we can declare multiple variables with the same value like a=b=c=100
#we can print the value of the vaiables using the print() function

#there should be some rules to be declare a variables in python 
#1)should not start with a numbers or any special characters except _(underscore)
#2)it should be start with a letters or _ 
#3) python is a case sensitive language that means  a and A both are different variables
#4)can contain (a-A),(0-9)and underscore(_)

_name_1_="chandan and darshan"
name="sadananda"
Name="sanjeev"
print(name)
print(Name)
print(_name_1_)
print(name+" and "+Name)


#datatypes
#datatypes:datatype is the type of value that a variables holds in simple words datatypes is a  water inside the bottle
#there are 4 basic datatypes in python 1)integer 2)float 3)string 4)boolean


name="sadanada" #string
age=2
is_student=True #boolean
height=5.4 #float
print(age)
print(name)
print(type(name))
print(type(age))
print(is_student)
print(type(is_student))
is_student="yes" #string
print(type(is_student))
print(height)
print(type(height))

age=23
print(age)



#type conversion
#its a process of converting one data type to another data type

marks=100
per=100.0
name2="chandan anna"
print(float(marks))
print(int(per))
print(bool(name2))
print(str(marks))



#operators
#operators:this are special symbols that perform specific operations on one or more operands
#1)arithmetic operators:these operators are used to perform mathematical operation like addn,sub,mul,div etc
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a*b-a+a//b)
print(a+b-a+b*2**3)


#perform arithmetic opertions on two variables such as addn,sub,muldiv etc
x=15
y=10
print("addition of two variables:",x+y)
print("sub two variables:",x-y)
print("mul two variables:",x*y)
print("div two variables:",x/y)
print("floor div of two var:",x//y)
print("reminder of two var:",x%y)

#swap two numbers
a=10
b=20
print("a",a)
print("b",b)
a=a+b #30
b=a-b #10
a=a-b #20
print("a",a)
print("b",b)