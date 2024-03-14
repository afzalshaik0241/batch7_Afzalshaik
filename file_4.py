# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorial of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
'''
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"
# Example usage
print(catAndMouse(1, 2, 3))  # Output: Cat B

#  2nd answer
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

# 3rd answer
sum_even = 0
sum_odd = 0
for num in range(12, 38):
15:51
for num
'''

# ---> Day-4:-

# ---> While loop
# ----> break using while loop

#eg:-
# 1.)iterate from 20 t 30 and break the loop in 27

#i = 20
#while i<31:
#    if i == 27:
#        break
#    print(i)
#    i+=1

#i = 20
#while i<31:
#   print(i)
#    i+=1
#    if i == 27:
#        break

#i = 20
#while i<31:
#    print(i)
#    if i == 27:
#        break
#    i+=1

#i = 20
#while i<31:
#    if i == 27:
#        print(i)
#        break
#    i+=1

#---> Continue
# 1.)

#i = 20
#while i<31:
#    if i == 27:
#        continue
#    print(i)
#    i+=1

#i = 20
#while i<31:
#    print(i)
#    if i == 27:
#        continue
#    i+=1

#i = 20
#while i<31:
#   print(i)
#   i+=1
#   if i == 27:
#       continue

#i = 20
#while i<31:
#    i+=1
#    if i == 27:
#        continue
#    print(i)
    
#Eg-5:-
#While  to iterate from 12 to 22
# find the sum of all numbers

#i = 12
#sum=0
#while i<23:
#    sum+=i
#    i+=1
#    if i == 23:
#        print(sum)

# ! Eg:6
# Find the average of value from 20 to 25

#i = 20
#sum=0
#avg=0
#count=0
#while i<26:
#    sum+=i
#    count+=1
#    i+=1
#avg=(sum/count)
#print(avg)

# ! -------> Nested for loop

#for i in range(1, 3+1):
#    for j in range(1, 4+1):
#        print(i, j)

#eg-2:-
# * * * *
# * * * *
# * * * *
# * * * *
'''
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of cols: "))

for i in range (rows):
    for j in range (cols):
        print("*", end=" ")
    print()
'''

#for i in range (5):
#    for j in range (5):
#        print(i, end=" ")
#    print()

#! to print stars in right angled triangle
'''
for row in range (0, 6):
    for col in range (0, row):
        print("*", end=" ")
    print()

'''

#rows=int(input("Enter the number of rows: "))
#cols=int(input("Enter the number of cols: "))

#for rows in range (rows):
#    for cols in range (cols):
#        print("*", end=" ")
#    print()

# Eg:-
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#      *
#    * * *
#   * * * *
#  * * * * *

'''
for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *



'''
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
'''

# ----> List
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

#To access the elements in the list
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
# print(lst1)

# --> Indexing
#In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefines unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side

# ---> Positive indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[0])
#print(lst1[4])
#print(lst1[20]) ---> error

# ---->Negative indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])

# ? ----> Slicing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
# lst1[start_indexing:end_indexing}]
# print(lst1[0:4]
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:5])
# print(lst1[3:])
# print(lst1[:])

#print(lst[0:7:1]) # lst1[0:7] ----> both are same
#print(lst[0:7:2])

# trail = int(input())

lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst[-4:-1])
#print(lst1[-1:-4]) ---> []
#print(lst1[-7:-1])
#print(1st1[-7:-1:2])


#! To insert ot add element inside list

# append()-> used to add element at last position of list
# l1 = [9, 8, 0, 6]
# l1.append("car")
#print(l1)




























































