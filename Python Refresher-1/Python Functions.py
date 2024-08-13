#user defined functions (UDF)
#declaration
def greeting():
    return "Hello welcome"
#Calling
print(greeting())

#lambda function : Annonymous function
x = lambda a:a*2
print(x(2))

#In-built functions
list1 = [1,2,3,4,5]

#map : multiply each number by 2 in a list

print(list(map(lambda x: x*2,list1)))

#filter: print the even

print(list(filter(lambda x:x%2 ==0, list1)))

#reduce find the product of values in the list
from functools import reduce

x = reduce(lambda x, y: x*y, list1)
print(x)


'''
Create a function and apply it on reduce 
method to return aggragete sales

defaultdict is a kind of subset of dictionary- 
to avoid key error
'''

sales = [{'product':'Laptop', 'amount':50000,},
         {'product':'Iphone', 'amount':150000,},
         {'product':'Smart Tv', 'amount':75000,},
         {'product':'Gaming console', 'amount':35000,},
         {'product':'Laptop', 'amount':90000,},
         {'product':'Iphone', 'amount':75000,},]


#Accumulate total sales revenue for each product
from collections import defaultdict

def accumulate(accumulator, transaction):
    product = transaction['product']
    amount = transaction['amount']
    accumulator[product] += amount
    return accumulator

data = dict(reduce(accumulate, sales, defaultdict(int)))

for key, val in data.items():
    print(f"{key} : {val}")



#Reduce
#reduce(fucntion, iterable, initializer)
#initializer: used to initialize 


#find top selling product and top-selling revenue
# print([(key,val) for key,val in data.items() if val >= max(data.values())])

item = max(data, key = data.get)
print(f"Top selling product is {item} of total revenue {data[item]}")

# *args & **kwargs


def display(*args): 
   return(i for i in args if i%2==0)

print(list(display(*[1,2,3,4,8])))


def kw_display(**kwargs):
    for key,val in kwargs.items():
        print(key,val)
    

# kw_display(**{"username":"admin", "password":"root"})
kw_display(username = "admin", password = "root")
