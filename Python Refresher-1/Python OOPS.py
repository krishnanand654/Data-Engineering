# class Person:
#     def __init__(self, *args):
#         if len(args) >= 4:
#             self.name = args[0]
#             self.age = args[1]
#             self.dob = args[2]
#             self.email = args[3]
#         else:
#             raise ValueError("Not enough arguments passed! Expected 4")
   
#     def __str__(self):
#         return(f'''Name: {self.name}\nAge: {self.age}\nDob: {self.dob}\nEmail: {self.email}''')

# try:
#     obj = Person("krishnanand",22, "20/10/2001","krishnanand654@gmail.com")
#     print(obj)
# except ValueError as e:
#     print(e)


#Inheritance
#single level
# class Vehicle:
#     def __init__(self,brand, model, mileage):
#         self.brand = brand
#         self.model = model
#         self.mileage = mileage
# class Car(Vehicle):
#     def __init__(self,brand, model, mileage, wheels):
#         self.wheels = wheels
#         super().__init__(brand, model, mileage)
#     def __str__(self):
#         return(f"Brand: {self.brand}\nModel: {self.model}\nMileage:{self.mileage}\nWheels:{self.wheels}")
       
# car = Car("BMW", "M Series", 15, 4)
# print(car)

#Multi level inheritance
# class Country:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
# class State(Country):
#     def __init__(self,name, population,region):
#         self.region = region
#         super().__init__(name, population)
# class City(State):
#     def __init__(self,name, population,region,food):
#         self.food = food
#         super().__init__(name, population, region)
    
#     def __str__(self):
#         return(self.name)

# city1 = City("Kottayam", 1000000, "South", "Kappa")
# print(city1)

# #Multi level inheritance
# class Entity:
#     def __init__(self, name):
#         self.name = name
# class User(Entity):
#     def __init__(self,name,email):
#         self.email = email
#         super().__init__(name)

# class Admin(User):
#     def __init__(self, name, email, permission):
#         super().__init__(name, email)
#         self.permission = permission
#     def __str__(self):
#         return(f"{self.name} has following permission {', '.join(self.permission)}")

# obj = Admin("admin","admin@example.com",['read','write','execute'])
# print(obj)

# #Hierarchical inheritance
# class Phone:
#     def __init__(self, brand, model, color):
#         self.brand =brand
#         self.model = model
#         self.color = color
# class Android(Phone):
#     def __init__(self,brand, model, color, os, osversion, processing):
#         super().__init__(brand, model, color)
#         self.os = os
#         self.osversion = osversion
#         self.processing = processing
#     def __str__(self):
#         return(f'''
#                 {'-'*4}Android Description{'-'*4}
#                 Brand: {self.brand}
#                 Model: {self.model}
#                 Color: {self.color}
#                 Os: {self.os}
#                 OSversion: {self.osversion}
#                 processing: {self.processing}
#                ''')
# class Iphone(Phone):
#     def __init__(self,brand, model, color, os, osversion, processing):
#         super().__init__(brand, model, color)
#         self.os = os
#         self.osversion = osversion
#         self.processing = processing
#     def __str__(self):
#         return(f'''
#                 {'-'*4}Iphone Description{'-'*4}
#                 Brand: {self.brand}
#                 Model: {self.model}
#                 Color: {self.color}
#                 Os: {self.os}
#                 OSversion: {self.osversion}
#                 processing: {self.processing}
#                ''')
# android = Android("Samsung", "S24", "black", "Android 14", 14, "Snapdragon")
# iphone = Iphone("iphone", "15", "black", "17.6.1", 14, "A16 Bionic")

# print(android)
# print(iphone)

# #Mutliple Inheritance
# class vehicle:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model

# class electric:
#     def __init__(self, battery_type, battery_level):
#         self.battery_type = battery_type
#         self.battery_level = battery_level

# class electric_vehicle(vehicle, electric):
#     def __init__(self, name, model, battery_type, battery_level,range):
#         vehicle.__init__(self,name, model)
#         electric.__init__(self,battery_type, battery_level)
#         self.range = range
#     def __str__(self):
#         return(f'''
#                 Vehicle name: {self.name}
#                 Model: {self.model}
#                 Battery Type: {self.battery_type}
#                 Battery percentage: {self.battery_level}
#                 Range in km: {self.range} km
#                 ''')

# ev = electric_vehicle("Tesla","X3", "Li-Ion",100, 300)
# print(ev)

#Abstraction
#import abstract class package
from abc import ABC, abstractmethod

class Bill(ABC):
    def print_slip(self, amount):
        print("Purchase amount: ", amount)
    
    @abstractmethod
    def bill(self, amount):
        pass

class DebitCardPayment(Bill):
    #method overriding
    def bill(self, amount):
        print("Debit card payment of - ", amount)

obj = DebitCardPayment()
obj.print_slip(200)
obj.bill(200)



    
