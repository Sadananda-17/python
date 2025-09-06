
x=int(input("enter the value for x"))
y=int(input("enter the value for y"))
if x>=10 and y>=10:
    print("true")
else:
    print("false")
    

    #2

x=2
y=7
if x<5 or y>5:
    print("true")
else:
    print("false")

#3
age =int(input("enter your age"))
if age>=18:
    print("you are adult")
elif age<18:
    print("your are not adult u are a minor")

#4
stringname=input("enter any fav state")
if"a"  in stringname:
    print("i love" +stringname)
elif "python" not in stringname:
    print("true")

a=2 #in binary 10
b=4 #in binary 100
print(a & b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)#8
print(a>>1)#1