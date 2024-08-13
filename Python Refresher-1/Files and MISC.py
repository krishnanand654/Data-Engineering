'''
Usage of datetime package
'''
# import datetime

# # print(datetime.date.today())
# # print( datetime.datetime.now())

# # today = datetime.date.today()
# # print(f"Day: {today.day}, Month: {today.month}, Year: {today.year}")

# #usage of datetime in example
# class person:
#     def __init__(self, name, surname, birth_date, address, contact, email ) -> None:
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         self.address = address
#         self.contact = contact
#         self.email = email
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birth_date.year
#         if today < datetime.date(today.year, self.birth_date.month, self.birth_date.day):
#             age -= 1
#         elif age < 0:
#             print("Person is not born.")

#         return age

#     def __str__(self):
#         return(f'''
#                 {"-"*5}Person Details{"-"*5}
#                 Name: {self.name}
#                 Surname: {self.surname}
#                 Dob: {self.birth_date}
#                ''')
# obj = person("Kris", "xyz", datetime.date(2001, 10, 20), "something",9495434706, "something@example.com")
# print(obj.age())

'''
File handling

default - read mode
r+ : first read then write
w+ : first write then read
'''

# fileobj = open('new_file.txt','r')
# print(fileobj.read())

#Create file and open in write mode
fileobj = open("another_file.txt",'w')

fileobj.write("This is a new file ")
fileobj.close()

fileobj1 = open('another_file.txt','r+')
print(fileobj1.read())

fileobj1.write("Appending new data")

#Read again
#seek(0) position the cursor at first position
fileobj1.seek(0)
print(fileobj1.read())

fileobj1.close()



fileobj3 = open("filename.txt", 'w+')
#won't read first write only
print(fileobj3.read())
fileobj3.write("something")
fileobj3.seek(0)
print(fileobj3.read())
fileobj3.close()

with open('filename.txt','r+') as file:
    print(file.readlines())


'''
list comprehension
input marks oputput grade
'''
marks=[65,100,80,90]
list1 = lambda x: "A" if x > 90 else "B" if x > 80 else "C" if x >70 else "D" if x >60 else "F"
print([list1(x) for x in marks])