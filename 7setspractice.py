#1
tuple=(1,2,3,4,5)
#tuple[1]=1
#print(tuple)
print(tuple[1:3])
tuple1=(1,3,4,7,8,9)
tuple_concat=tuple+tuple1
print(tuple_concat)

#2
my_fav_fruits={"apple","banana","grapes","pomo"}
my_friend_fruits={"mango","watermelon","tomato","apple","pomo"}
print(my_fav_fruits | my_friend_fruits)
print(my_fav_fruits & my_friend_fruits)
print(my_fav_fruits - my_friend_fruits)

k={1,2,3,4,5}
print(k)
k2=(5,6,7)
k3=set((k2) ) 
print(k3) 
#print(k2.add(1,88))
k3.add(12)
print(k3)




