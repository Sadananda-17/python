#tuples are immutable cannot be change
#methods in tuples
#count and index
t=(10,20,30,40,50)
print(t.count(10))
print(t.count(20))
print(t.count(30))
print(t.count(40))
print(t.count(50))

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

print(t[1:])
print(t[:])
print(t[1:4])
print(t[::-1])


#nested tuples
nested=(1,(2,3),(4,5))
print(nested[1][1])

#tuples operation
#1)concatination
#2)Repitition
#3)membership
#iteration
#length
a=(1,2)
b=(3,4)
print(a+b)

print((1,2)*1000)

print(1 in a)
print(1 not in a)

for i in b:
    print(i)
print(len(a))

#sets in python
#set methods
#add
#update
#remove
#discard
#pop
#clear
#copy

s={1,2}
s.add(3)
s.update([4,5])
print(s)

s.remove(5)
s.discard(10)
print(s)

print(s.pop())
s.clear()
print(s)

#set operation
#union
#intersection
#differnce
#Symmetric difference
#subset/superset/disjoint
a={1,2,3}
b={3,4,5}
print(a|b)
print(a&b)
print(a-b)
print(a^b)#symmetric difference
print({1,2}.issubset(a))
print(a.issuperset({1}))
print(a.isdisjoint({6,7}))