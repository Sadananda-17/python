#1
"""
list_of_Strings=["rolex","benz","dream house","iphone","making parents proud"]
list_of_Strings.append("being a goodperson")
print(list_of_Strings)
list_of_Strings.insert(2,"be in the list of 1per people")
print(list_of_Strings)
list_of_Strings.remove("dream house")
print(list_of_Strings)

list_no=[1,3,2,5,4,7,6,9,8,10]
list_no.sort(reverse=True)
list_no.reverse()
print(list_no)
#or


#slicing practice
#basic                  #-ve index -6  -5  -4 -3 -2   -1
text="python"           # index     0   1   2   3   4   5   6
print(text[0:4])         #char      P   Y   T   H   0   N
                        #slice      p   y   t   h

print(text[:4])#stop to 3 but start from 0 index itself(omiting stop)

print(text[2:])#start from 2nd index but end not mention so it go till the end

print(text[:]) #there is no mention of the start and stop so it go and print the whole string

#NEGITIVE SLICING
print(text[-4:]) # start only -4 that is in +ve indexing is  2 but end not mention go till end
print(text[-6:-2])#start point is -6 and end to -3 exclude -2


#using step
print(text[2::2]) #whole strings is divided by one after one
print(text[1::2])

#NEGITIVE STEP REVERSE
print(text[::-1])
print(text[::-2])
print(text[::-3])


#partial reverse with negitive step
print(text[5:2:-1])
print(text[4:0:-2])

#out of range index
print(text[0:100])
print(text[-100:3])

print(text[::10])

#slice objects
s=slice(1,5,2)
print(text[s])


#list set of problems
list_int=[10,20,30,40,50]
print(list_int)
list_int[2]=35
print(list_int)

list_fruits=['apples','banana','cherry']
list_fruits.append('oranges')
print(list_fruits)
list_fruits.insert(1,"kiwi")
print(list_fruits)
list_fruits.remove('banana')
print(list_fruits)
list_fruits.clear()
print(list_fruits)


numbers=[1,2,3,4,5]
numbers.append(6)
numbers.pop(2)
numbers.remove(1)
print(numbers)

data=[10,20,30,40,50]
data[0]=0
data[1]=0
data[3]=0
print(data)

nums=[10,20,30,40,50,60,70,80]
print(nums[0:4])
print(nums[5:])
print(nums[::2])
print(nums[::-1])
print(nums[::-2])
print(nums[2:6:2])


nums=[4,1,7,3,4,2,4]
print(len(nums))
print(sorted(nums))
nums.sort()
print(nums)
print(sorted(nums,reverse=True))
nums.sort(reverse=True)
print(nums)

total=sum(nums)

print(total)
"""
nums=[4,1,7,3,4,2,4]
print(nums.index(4))
print(nums.index(1))
print(nums.index(7))
print(nums.index(3))

print(nums.count(4))
nums.reverse()
print(nums)

matrix=[
    [1,2,3],        #0   1  2
    [4,5,6],        #1
    [7,8,9]         #2
]
ele=matrix[1][2]
ele1=matrix[1][1]=10
print(ele1)
print(ele)
print(matrix[1])
last_col=[row[2] for row in matrix]
print(last_col)

rev_row=matrix[::-1]
print(rev_row)

nums=[1,2,3,4,5]
nums[1:4]=nums[1:4][::-1]
print(nums)
