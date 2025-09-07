
item1="sugar"
item2="milk"
item3="salt"
print(item1,item2,item3,sep="")

#this method gonna very lengthy if we have more items to print
#so here comes the List concepts

#list is a collection of items in a particular order
#list is  a mutable etc
#list can defined by square brackets[]
#and also different data types can be stored in a list
items=["sugar",'milk','salt']
print(items)
print(items[0])
print(items[1])
print(items[2])
print(items[-1])#last item
print(items[-2])#second last item
print(items[-3])#third last item
print(items[0:2])#slicing


my_list=["benz","bmw","opera","safari","audi"]
print(my_list)

int_list=[1,2,3,9,-1,0,-10000000000000000000000]
print(int_list)

float_list=[1.5,2.9,55.0,100.0,200.0,78.0]
print(float_list)


l=[1,"bru",True,5.6,[1,2,3,4,5]]#list iside a list

print(l[4])
print(l)

items=["building a dream  house","buying a dream car","getting a dream job","making our parents proud"]
items.pop(0)
items.pop(1)
items.pop() #pops the last item it removes the list items

items.append("travel the world")#it adds the new items at the end of the list
items.append("becoming a coder")    
print(items)

list=["sugar","bru","Milk"]
list.remove("sugar")  #remove
list.remove("Milk")
#list.remove("salt") #it will give a error beacuse it not present in the list
print(list)

my_marks=[100,98,90,89,80]
my_marks.insert(1,99) #insert means it will add the elements based on index what index we specify
print(my_marks)

my_dream_cars=["benz","bmw","rangerover","thar rox","safari"]
my_dream_cars.insert(0,"roll sroys")
print(my_dream_cars)
print(my_dream_cars[0:6])
print(my_dream_cars[:6])
print(my_dream_cars[0:])
print(my_dream_cars[1:-1])

my_dream_cars.clear() #it will clear whole list
print(my_dream_cars)


#changing the specific element inthe list
my_list=["bru","sugar","salt","milk"]
my_list[0]="nescafe"
my_list[1]="brown sugar" #just by giving its index and then modify it by what u the alternative name
my_list[2]="tata salt"
my_list[3]="nandini milk"
print(my_list)


#slicing the list
l=["a","b","c","d"]
print(l[0:2])
print(l[1:3])
print(l[2:4])
print(l[0::2])#start:stop:step

n=[100,200,300,400,500]
print(n[0:])
print(n[0:2])
print(n[0:5])
print(n[0:6:3])
n2=n[1:]
print(n2)
n3=n[0:5]
print(n3)
n4=n2[1:3]
print(n4)

#list function
#1)len()
amma_grossury_list=["bru","sugar","milk"]
print(len(amma_grossury_list)) #len() start from 1

#2)sorted()
numbers=[1,3,2,4,6,5,9,7,8]
sorted_no=sorted(numbers)#here we assign the sorted() method to another var
print(sorted_no)# and here we printing that one
print(sorted(numbers)) # but here we directly printing by using sorted()function


#3)sum
number=[1,2,3,4]
print(sum(number))

"""
mix_data=[1,"chandan","hello",3.0]
print(sum(mix_data)) #it gonna give the type error beacuse of diff types of data types
"""
#4index
element=["apple","banana","grapes","pomo"]
print(element.index("apple"))
print(element.index("pomo"))
print(element.index("grapes"))
print(element.index("banana"))


#5count
ele=[1,2,3,4,1,2,2,1,1,2]
print(ele.count(1))
print(ele.count(0))
print(ele.count(2))
print(ele.count(3))
print(ele.count(4))#it wil give the count of each no


#6 reverse
n1=[1,3,2,4,7,5,6,6,9,8]
n1_sorted=sorted(n1)
print(n1_sorted)
n1_sorted.reverse()
print(n1_sorted)
n1_sorted.sort()
print(n1_sorted)


#matrix
m=[
    [1,2],
    [3,4]
]
print(m)
print(type(m))
print(m[0][0])
print(m[0][1])
print(m[1][0])
print(m[1][1])

m=[[1,2],   [2,3,[3,3,3]]]
   # 0(0,1)  1(0,1(0,1,2))
print(m)
print(m[1][1])
print(m[1][2])



