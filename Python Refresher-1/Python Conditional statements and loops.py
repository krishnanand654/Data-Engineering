'''
Loops
'''
#condition controlled loop
i=0
while i<10:
    print(i, end=" ")
    i += 1

#Count controlled loop
for i in range(0,10):
    print(i, end=" ")

#collection controlled loop:
lst=['a','b','c']
for i in lst:
    print(i,end=" ")

import keyword
print(keyword.kwlist)

list_val=[]
statement = "how are you"
for character in statement:
    list_val.append(character)
print(list_val)


'''
Conditional statements
'''
bro_age = int(input("Enter the brother's age: "))
sis_age = int(input("Enter sister's age: "))

if bro_age > sis_age:
    print("Brother is elder")
elif bro_age < sis_age:
    print("Sister is elder")
else:
    print("Both are twins")


'''
create a login access using loop and condition
'''
while True:
    print(f"{'-'*5}Menu{'-'*5}\n1.Login\n2.Exit")
    ch = input("Choose an option: ")
    if ch == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username=="admin" and password == "root":
            print("Login successfull")
            break
        else:
            print("Incorrect Username or Password, Please try again")
    
    elif ch == '2':
        print("Exiting from the program")
        break
    
    else:
        print("Invalid choice, Please choose option login or exit")

#break and continue
list1 = ['EKM', 'TVM',None, 'KTM',None,'CGY',None]

for city in list1:
    if city == None:
        continue
    print(city)
    
