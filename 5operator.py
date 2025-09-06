#operators
#Assigment operator
x=10 # assignment operator
y=30
z=45
g=8

a=10
#a=a+100
print(a)
a+=100
print(a)
a-=100
print(a)
a*=100
print(a)
a/=100
print(a)
a//=100
print(a)
a**=100
print(a)

#Comparision operator
a=10
b=20
print(a<b)
print(a==b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)

x=100-10
y=100-10
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical operator vvv imp
print(True and True) #1  both should be true
print(True and False)#0
print(False and True)#0
print(False and False) #0  #and gate

print(True or True)#any one is true then true
print(True or False)
print(False or True)
print(False or False)

print(not(True))
print(not(False))

print(2==2 and 1==1)
print(2<=2 and 2<=1)
print(2>3 and 3>2)
print(2>10 and 3>10)


print(1 or 0)
print(1 or 1)
print(0 or 1)
print(0 or 0)

print(not(1))
print(not(0))
print(not(1<2))

#membership operator
x="chandan"
print("c" in x)

s="sadananda"
print("s" in s)
print("sdn" not in s)
print("k" not in s)
print("k" in s)

my_list=[1,2,3,4,5]
my_string="python"
print(3 in my_list)
print(6 not in my_list)
print("p" in my_string)
print("z" in my_string)

s="chandan"
s2="chandang"
print(("g" in s) or ("g" in s2))
print("h" in s)and (("h" in s2))
print("h" in s)or (("h" in s2))
print("a" in s)and (("a" in s2))
print("a" in s)or (("a" in s2))
print("n" in s)and (("n" in s2))
print("n" in s)or (("n" in s2))
print(not("g" in s2))

#bitwise operator 
a=5 #in binary:101
b=3 #n binary 011
print(a&b)
print(a|b)
print(~(a))
print(a^b)
print(a<<1)#10
print(a>>1)#2

x=4 #in binary100
y=2 #in binary 010
print(x&y) #bitwise and
print(x|y) #bitwise or
print(~x)#bitwise not
print(x^y)#bitwise xor
print(x<<1)#bitwise left shift #8
print(x>>1)#bitwise right shift #2

