#1.) Write a Python script to generate and print a dictionary that 
#contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary (n=5): 
# Expected Output (1:1, 2:4, 3:9, 4: 16, 5:25)
# def generate_squared_dict(n):
#     squared_dict = {}
#     for i in range(1, n + 1):
#         squared_dict[i] = i * i
#     return squared_dict

# def print_squared_dict(squared_dict):
#     print("Generated Dictionary:")
#     for key, value in squared_dict.items():
#         print(f"{key}:{value}", end=", ")

# n = int(input("Enter the value of n: "))
# squared_dict = generate_squared_dict(n)
# print_squared_dict(squared_dict)



# def raj(n):
#     d1={}
#     for i in range(1, n+1):
#         d1[i]=i*i
#     return d1
# def raj(d1):
#     print("generated d1:")
#     for mon, value in d1.marks():
#         print(f"{mon}:{value}", end=", ")
        
# n = int(input("enter the value of n: "))
# n = generated raj(n)
# print d1(raj)
        
        
        
        
### 222      
# s1 = "hello how are you"
# s2 = "hello how is"

# s1=s1.split(" ")
# s2=s2.split(" ")

# for val in s1:
#     if val not in s2:
#       print(val)
# for val in s2:
#     if val not in s1:
#         print(val)  


# 333333  find the 8th fibanochi number
# num=8
# n1=0
# n2=1

# for val in range(num):
#     ans=n1+n2
#     n1=n2
#     n2=ans
#     print(ans)
# ! constructors


# ? eg 2
# unparamised constructor 
# class profile:
#     def __init__ (self):
#         print("hello world")
# obj =profile()
# obj.__init__()

# ? eg 3:
# parameteraised constructor
# class profile:
#     def __init__(self, id, name, age):
#         print(id, name, age)
        
# obj=profile(1, "sid", 29)

# ? eg 4
# class c1:
#     email = "sid@gmail.com"
  
    
#     def m1(self):
#         name = "sid"
#         place= "cbe"
#         print(name,place)
#         print(self.email)
        
# pbject = c1()
# object.m1()

# ? eg:5
# class c1:
#     def m1(self):
#         name = "sid"
#         age = 28
#         return name,age
#     def display(self):
#         # print(name, age) except
#         # print(self.name, self.age) except
#         print(self.m1())
        
# object = c1()
# object.display()

# eg : 6
# to use the variable inside the constructor in another methods
# class class1:
#     def __init__ (self):
#         self.name = "sid"
#         self.email = "sid@gmail.com"
    
    
#     def display(self):
#         print(self.name, self.email)
        
# c1 =  class1()
# c1.display()

# ! ------> inheritance
# * sinlge Inheritance
# ? it has only one parent class and only one child class
# | Eg:1
# class parent:
#     def m1(self):
#         print("I am parent class")


# class child(parent):
#     def m2(self):
#         print("I am child class")

# obj = child()
# obj.m1()

# ! eg:2
# class c1:
#     def __init__(self):
#         print("i am constructor from parent class")
        
# class child1(c1):
#     pass

# obj = child1()

# eg :3
# class parent:
#     name = "sidhu"
    
# class child(parent):
#     name = "rajesh"
    
#     def display(self):
#         print(self.name)
        
# d = child()
# d.display()

# ! multilevel inheritance
# eg : 1
# class voice:
#     def sound(self):
#         print("all the animals have their own voices")
        
# class dog(voice):
#     def dog_voice(self):
#         print("bark")
        
# class cat(dog):
#     def cat_voice(self):
#         print("meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")
        
# all=parrot()
# all.dog_voice()
# all.cat_voice()
# all.sound()
# all.parrot_voice()

# ? Eg:2
# class honda_city:
#     def honda_city_engine_specs(self, cc, hp, torque, fuel_type, num_of_positions):
#         print(self, cc, hp, torque, fuel_type, num_of_positions)
        
#     def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#         print(self, color, weight, height, length, vehicle_type)
# class amaze(honda_city):
#     def civic_engine_specs(self, cc, hp, torque, fuel_type, num_of_positions):
#         print(self, cc, hp, torque, fuel_type, num_of_positions)
        
#     def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#         print(self, color, weight, height, length, vehicle_type)

# class honda_city:
#     def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
#         print(cc, Hp, torque, fuel_type, num_of_piston)

#     def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#         print(color, weight, height, length, vehicle_type)
# class amaze(honda_city):
#     def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
#         print(cc, Hp, torque, fuel_type, num_of_piston)

#     def amaze_body_specs(self, color, weight, height, length

# class while_pertol:
#        def function_w(self): print("used to Airplans")
# class Organic_petrol:
# def function_o(self):
# print("used for Bike, cars")
# class premium_petrol:
# def function_p(self): print("spots cars, bikes")
# class petrol (while_pertol, Organic_petrol, premium_petrol):
# def defanition(self): print("Petrols types")
# # Multiple Inheritance
#  #? It has multiple parent and 1 child
# class while_pertol:
#     def function_w(self):
#         print("used to Airplans")

# class Organic_petrol:
#     def function_o(self):
#         print("used for Bike, cars")
# class premium_petrol:
#     def function_p(self):
#         print("spots cars, bikes")
# class petrol(while_pertol, Organic_petrol, premium_petrol):
#     def defanition(self):
#         print("Petrols types")
# # p=petrol()
# p.defanition()
# p.function_o()

# ! multiple inhertance
# ? it has multiple parent and 1 child
# class while_petrol:
#     def function_w(self)


# # ! Eg:2
# class addition:
#     def add(self, a,b):
#         print(a+b)

# class substract:
#     def sub(self, a,b):
#         print(a-b)

# class multiply:
#     def mul (self, a,b):
#         print(a*b)

# class division(addition, substraction, multiply):
#     def div(self, a, b):
#         print(a/b)

# calc = division()
# calc.add(3, 4)
# calc.mul(5, 2)

# Eg:2
# MRO---> Method resolution Order
# class addition:
#     def add(self, a, b):
#         print(a+b)
#     def mul(self,a,b):
#         print(a%b)
# class subract:
#     def sub(self, a, b):
#         print(a-b)
# class multiply:
#     def mul(self, a, b):
#         print(a*b)
# class division(addition, subract, multiply):
#     def div(self, a, b):
#         print(a/b)
# calc=division()
# calc.add(3,4)
# calc.mul(5,2)


# # ! herirarical inheritance
# The one parent class will acts ac parent for all the child classes
'''
class category:
    def weight(self, weight):
        print(weight
    def display(self, color, taste):
        print(color, taste)
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste "neutral taste"
        self.display(color, taste)
class carrot(catagory):
    def carrot_specs(self):
color="green"
taste "sweet"

self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
color="green
c=carrot()
c.carrot_specs()
c.weight("30gms")
'''

# ! Hybrid Inheritance
# ? The combination of above 4 inheritance is called Hybrid Inheritance
class c1:
    def m1(self):
        print("Class 1")

class c2(c1):
    def m2(self):
        print("Class 2")

class c3(c2):
    def m3(self):
        print("Class 3")

class c4(c2):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("i am m3 from c4")

class c5(c3):
    def m5(self):
        print("Class 4")  

class c6(c5, c4, c2, c1):
    def m6(self):
        print("Class 4")
        
obj = c6()
obj.m3()

# ! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# * Ploymorphism in operators
#-----> +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[4,5,6])

# *
# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)

# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding




























     


