#tuples:its a similar to list and also ordered but the only one thing is its not changeble (immutable)
gender=("male","female","others")
print(gender)
print(type(gender))
print(len(gender))
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[:])

cars=("benz","fortuner","audi","rangerover")
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print(cars[0:2:1])
print(cars[::-1])
print(cars[::-2])

#tuple_concatenation
tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)
tuple=tuple1+tuple2
print(tuple)

alpa=('a','b','c','d','e')
ALPA=('A','B','C','D','E')
add=alpa+ALPA
print(add)

#repeated Tuple
repated_tuple=("hello","hi")
repeat_tuples_mul=repated_tuple*100
print(repeat_tuples_mul)

names=("rohith sharma","virat kohli")
names_repeat=names*12
print(names_repeat)


#checking membership
tuples_fruits=("banana","apple","oranges")
tuples_check="banana" in tuples_fruits or "oranges" not in tuples_fruits
check=print("grapes" not in tuples_fruits)
print("apples" in tuples_fruits)
print(tuples_check)


tuples=("male","male",'female',"other")
print(tuples.count("male"))
tuples_count=tuples.count("other")
print(tuples_count)
print(tuples.index("male"))
print(tuples.index("female"))
print(tuples.index("male"))
print(tuples.index("other"))


tuples=(1,2,3,4,(1,2,3,4,5))
print(tuples[4][0:])
print(tuples)
#advantages of tuples
#immutable 
#faster the lists
#it can be used as keys in dictnoiry



#sets:sets is a collection of unique items
#set is adenoted by{}
#and its a unoredered and unindexed
#for list we use []
#for tuples we use ()
#for sets we use {}
sets={12,3,4,4,5,6,7,8}
print(sets)
#s=set(1,2,3,4) #we can declare set using set()functions
s=set((1,2,3,4,5,6)) # so we have to put in tuples
print(s)
print(type(s))
s=()
print(type(s))
l={}
print(type(l))
k=set()
print(type(k))

#sets operation
s={1,2,3,4}
s1={2,3,4,4,5,6}
print(s|s1)#union it joins both the sets but duplicate wont allow
print(s&s1)#intersection it shows only the same ele in both sets
print(s-s1)# difference it 
print(s1-s) #minuses the sets from the given set


#set methods
s={1,2,3,2}
s.add(4)
#s.remove(10) it  give the error because that 10 is not there in that set
#so use
s.discard(1) #so use discard method
print(s)

s={"f","g","h"}
s.pop()
s.pop() #pop()
s.pop()
print(s)

#clear
s={1,2,3,4,5,6}
s.clear()
print(s)
