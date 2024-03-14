# ! Eg_3:-
# Take valve of length and breadth
# from user and check it is square or not
'''
length=int(input("enter length"))
breadth=int(input("enter breadth"))
if(length == breadth):
    print("It is square")
else:
    print("It is not a square")
'''
# ! Eg_4:-
# Accept the age of 4 people and display the oldest one
'''
a=int(input("enter first person age"))
b=int(input("enter second person age"))
c=int(input("enter third person age"))
d=int(input("enter fourth person age"))
if(a>b and a>c and a>d):
    print("a is oldest")
elif(b>a and b>c and b>d):
    print("b is oldest")
elif(c>a and c>b and c>d):
    print("c is oldest")
elif(d>a and d>b and d>c):
    print("d is oldest ")
'''



#Eg_4:-
# Python program to check wheather the
#given integer is a multiple of both 5 and 7
'''
n = int(input("enter a number:  "))
if n%5==0 and n%7==0:
        print("yes")
else:
    print("No")
'''
#Eg_5:-
#Write a program to accept the cost the cost price of a bike
#and display the road tax to be paid
# according to the following criteria:

'''
price=int(input("enter the cost price"))
total = 0
if price >= 100000:
    discount = 100000*(6/100)
    value = price-discount
    amount= value*(15/100)
    total=(value+amount)
else:
    tax = price*(5/100)
    total = price+tax
print("the Onroad cost of bike is ",total)
'''
# A school ha sfollowing rules for grading system:
# a.Below 25- F
# b.25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. above 80 - A
# Ask user to enter marks and print the corresponding grade
'''
marks=int(input("enter the Marks:  "))
if (marks>=80):
    print("A")
elif(marks>=60 and marks<80):
    print("B")
elif(marks>=50 and marks<60):
    print("C")
elif(marks>=45 and marks<50):
    print("D")
elif(marks>=25 and marks<45):
    print("E")
elif(marks<=25):
    print("F")
'''

# !--> short hand if else
# Eg:1
a=9
b=6
#if a>b:
#    print("A")
#else:
#    print("B")
# --> using short hand if else
#rules
#1.) statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else

#print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent

#char = input("Enter the char:  ")
'''
if char=="a" or char =="e" or char =="i" or char =="o" or char=="u":
    print("is a vowel")
else:
    print("is a consonent")
'''
# ? or
'''
str1="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")

# shorthand if else
char = input("enter the char; ")
str1 ="aeiouAEIOU"
print("vowels") if char in str1 else print("consonent:")
        
# Find greatest among 3 variables using short hand if else
a = 8
b = 5
c = 9

print("A is greater") if a>b and a>c else print("B is greater")
if b>a and b>c else print("C is greater") 
'''

# ! ------> looping

#looping can be implemented using
#for loop
#while loop

#---> for loop
#for loop is used for iteration, if we know the number of times the loop have to run
# ? for loop is used to iterate the iterables eg(string, list, tuple, etc...)

#todo ---> Syntax for loop

# for syntax in c
# for(i=0,i<10:1++){
#        printf("hello");
# }

# ! for syntax in python
#for userdefined_variable in range(start, end, stop): default step value is 1
#   statement
#   statement
#   statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

#for i in range(0, 10):
    #print(i)
#    print("Hello")

# ? Eg:2
#for val in range(23, 50, 1):
#    print(val)

#for val in range(1, 15, 3):
#    print(val)

# ? Eg:3
# to decrement the value

#for val in range(10, 0, -1):
#    print(val)
    
#for val in range(10, 0, -2):
#    print(val)

#for val in range(10, 0, 1):
#    print(val)     # no output

#Eg:4
#printing the output of 7th multiplication table from 21 to 43

#for i in range (21, 43+1, 7):
#    print(i)

#for i in range (1, 10+1,):
    #print('7','x', i, '=',i*7) --> method 1

    # --> Method:2
    #ans="7x{}={}"
    #print(ans.format(i, i*7))

    #--> Method 3
    #print(f"7 x {i} = {i*7}")

# ? Eg:5
#------> break

#for val in range(1, 10):
#    if val == 6:
#        break
#    print(val)
    
# Eg:6
#for val in range(1, 10):
#   print(val)
#  if val == 6:
#       break
#Eg:7
#for val in range(1, 10):
#   if val == 6:
#       print(val)
#       break
    
# ! continue
# Eg:1
#for val in range(1, 10):
#    if val ==6:
#        continue
#    print(val)

#for val in range(1, 30):
#    if val == 6 or val == 8 or val ==21:
#        continue
#    print(val)


# ! Practise problems
# ? print the even number between 20 t0 40

#for i in range(20, 40+1):
#    if(i%2==0):
#        print(i)

# ? print the odd number between 20 t0 40

#for i in range(20, 40+1):
#    if(i%2!=0):
#        print(i)

#!--------> While loop
# ? while is used when we do not know the number the times the loop have to run
# ? t iterate the non iterable elements while loop is used

# todo syntax

#initialisation
#while condition:
#    statement
#    incre or decre

#! Eg:1
#to iterate number from 1 to 10

#i = 0
#while i<11:
#    print(i)

# For loop practise
# Write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37(including both numbers)
#for i in range






# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432

#print("Hello{0[0]} and {0[1]}".format(('foo', 'bin')))

true = false
while true:
    print(true)
    break
























