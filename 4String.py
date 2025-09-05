#string manipulations
first_name="sadananda "
last_name="s shellikeri"
full_name=first_name+last_name
print(full_name)

first_name="puneeth "
last_name="rajkumar"
full_name=first_name+last_name
print(full_name)

first_name="chandan"
last_name=" gowda"
third_name=" anna "
final_name=first_name+last_name+third_name
print(final_name)

#repitition
messege=" welcome "*100
print(messege)

message1=" i love kannada " 
print(message1)


#string operation
#1)upper
#2)lower
print(message1.upper())
print(message1.lower())
print(messege.lower())
print(messege.lower())

#strip
amazon="hello its my dream company"
print(amazon.strip())

#replace
message="error"
name4="i love manglore"
name5="i love kudla"
print(name4.replace(name4,name5))



#learn more String methods 

name=""" sadananda always says to me"hello" 
        sanjeev replied as how u doing bro """
print(name)
message="This is a Warining "

#length
print(len(message)) #length of the string

#indexing
name="sadananda"
print(name[2]) #indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])

#slicing
print(name[0:9])
print(name[4:9])
print(name[0:])
print(name[-8])
print(name[:9])
#step counting
print(name[::2])
print(name[::4])

#escape sequence
s="sadananda\nis a good boy"
n="sanjeev \tis a good boy" 
k="sanjeev \\ is a good boy" 

print(s)
print(n)
print(k)
