# Day-6:-

# 1.) Python program to capitalize the first and last character of each
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


# s1 = input("enter a string: ")
# fst = s1[0].upper()
# lst = s1[-1].upper()
# print(fst+s1[1:len(s1)-1]+lst)

#n = 128
#for i in n:
#    print(i)


#n = 128
#while n!=0:
#    rem = n%10
#    print(rem)
#    n = n/10

#n = 128
#for i in str(n):
#    print(i)

'''
n = 128678
temp = n
str1 = ""
while n!= 0:
    rem = n%10
    check = temp % n
    if check == 0:
        print("yes")
    else:
        print("no")
    n = n//10
'''

'''
n = 128
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp % n
    if check != 0:
       f1 = 1
    n = n//10

if f1 == 0:
    print("yes")
else:
    print("no")
'''    

#l1 = [8, 9, 0, 7]
#l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
#l3 = []
#for val in range(len(l1)):
#    ans = l1[val]+l2[val]
#    l3.append(ans)
#print(l3)

'''
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

#print([l1[0]+l2[0], l1[1]+l2[1], l1[2]+l2[2], l1[3]+l2[3]])
# (or)
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)
'''

# ! ------> Set

# ? Characterstics  of set
# 1.) Set can be created using {}
# 2.) The elements inside set are not indexed
# 3.) Does not allow duplicate values
# 4.) It unordered
# 5.) Heterogenous
# 6.) Mutable or changable

# Eg:1
# s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
# print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 3
# min(), max(), len()

# * Eg: 4
# ? to add element inside set

#s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
#print(s1)

# update()
# s1.update([9,0])
# print(s1)

# ? To delete element inside set
#s1 = {8, 78, 67, 'u'}

#pop() # to delete one element randomly
# s1.pop()
# print(s1)

# remove()
# s1.remove(78)
# print(s1)

#discard()
# s1.discard(8967)
# print(s1)

# clear()
# l1 = {}
# print(type(l1)) --> datatype is dict

# s1 = set() # to create empty set
# print(type(s1))

# s1 = {8, 9, 0}
# s1.clear(s1)

# * Join the sets
#s1 = {9, 0, 8}
#s2 = {9.90, "card", 't', 56}
# union() ----> to combine 2 sets
#s3 = s1.union(s2)
#print(s3)


# * intersection() ---> to get common elments inside set
# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.intersection(s2))

#s1 = {4,5,6}
#s2 = {5,6,7,8}
# print(s1.difference(s2))
# print(s2.difference(s1))
#print(s1.symmetric_difference(s2))

# isdisjoit(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))
                      
#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}

#for val in s1:
#    if val in s2:
#        str1 = "Its joint set"
#print(str1)
    
# ! ---> Dictionary
# Eg:-1
#d1 = {1:100, 'a':200, 4.5:"hello"}
#print(d1)
#print(len(d1))

'''
mech_name = ["name1", "name2", "name3"]
mech_age = [23,22,24]
mech_mark = [89,78,60]
mech_email = ["name2@gmail.com", "name3@gmail.com"]

mech = {
    "student1":{
        "name":"name1",
        "age":24,
        "mark":89,
    },
    "student2":{
        "name":"name2",
        "age":22,
        "mark":76,
        "email":name@gmail.com,
    },
    "student3":{
        "name":"name3",
        "age":21,
        "mark":85,
        "email":name@gmail.com,
    },
}
print()
'''

# ? Char of dictionary

# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) Key does not allow mutable,datatypes, values allow mutable datatype

#d1 = {1:100, 2:200, 3:300, 4:400}
# * to access element in dictionary

# print(d1)
# or
# To access the values
#print(d1[1]) # o/p --> 100

# ? some common functions
#len(), min() , max()
#print(min(d1))
#print(max(d1))   

# ? To find min, max based on values
#print(min(d1.values()))
#print(max(d1.values()))

# ? dictionary based functions
# to add element (key and value pair) in dict
#d1 = {1:100, 2:200, 3:300, 4:400}
#d1[5] = 500
#print(d1)

# ? To replace a value in dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d1[2]="mango"
#print(d1)

# ? delete element from dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#popitem()#-->to delete last key value pair in dict
#d1.popitem()
#print(d1)

#pop()
#d1.pop(2) # 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
#update()
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()---> used to get the value from a key
#d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[90])
#print(d1.get[90])

# to print all the keys
#print(d1.keys())
#print(type(d1.keys()))

#To print all the values
# print(d1.values())

# * Iterating dictionary
#for val in d1:
#    print(val)

#for val in d1.value():
#    print(val)

# to get both keys and values
'''
for key, val in d1.items():
    print(key, val)
'''

#1.) swap elemwnts in string list
# The original list is :["Ggf", "best", "for", "geeks"]
# List after performing character swaps:]"efg", "is", "bBgst", "for", "eGGks"]
#problem
'''
n=int(input("Enter of times:"))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("Enter of times:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) ==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
'''
#problem2
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}



set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)

print(set3)
#problem3
# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']




















    
