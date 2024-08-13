'''
String methods
'''

str1 = 'This is Python'
#Reverse the string using index
print(str1[::-1]) # str1[0:len(str):-1]

#Find a word in a string
str1 = str.lower(str1)
print("The starting index of word 'python' is {}".format(str1.find('python')))

#join method
list1 = [' Hello', "world"]
result = ' '.join(list1)
print(result)

user_input = int(input("Enter a number "))
print(f"The number is {user_input}")

#Remove white spaces on the left eg: user inputs like white spaces
print(result.lstrip())

#partitions the inputs based on the delimiters eg: ;,""''
#Split the string at the last occurrence of delimiter
sentence = "this is an input"
print(sentence.rpartition(" "))


'''
list
'''

list_2 = ['hello','python','we','are','learning']

#append: adding element to the end of the list
list_2.append('list')
print(list_2)

#shallow copy: copy the contents only
list_3 = list_2.copy()

#deep copy: copies the reference if one changes the other also changes
list_4 = list_2

#Testing 
list_2.append("and datastructures")
print(list_3)
print(list_4)


list_2.extend(list1)
print(list_2)

#Remove the last element
list_2.pop
print(list_2)

#Remove element from he list using index
list_2.pop(1)
print(list_2)

'''
Tuple

Tuples iterate faster compared to list
list manages 2 memory where tuple manages only one.
'''

'''
Sets : Unordered colleciton of hetrogenous data with no indexes
    As it is unordered hence no indexes are there
'''
sets_1 = set()

sets_1 = {1,2,3,5,5,5,3,7,8}
sets_2 = {9,10,11,12,13,14,15}
sets_3 = {14,15,16,17,18,19,20}


print(sets_1.difference(sets_2))

#remove one random value
print(sets_1)
sets_1.pop()
print(sets_1)
sets_1.pop()
print(sets_1)

#Concatination of 2 sets without including duplicate values
sets_1.union(sets_2)

#updates the sets_1 with dummy input set
sets_1.update({100,200,300})
print(sets_1)

#union of two sets contianing elements present in either in two sets but not in both
print(sets_1.symmetric_difference(sets_2))

# common elements in both sets
sets_1.intersection(sets_2)

'''
Dictionary
'''

#method 1
dict_1 = {} 
dict_1 = {'A':'Apple', 'B':"Banana", 'C':'Cat'}

keys = ['EKM', 'TVM', 'KTM','CGY']
default  = 0
values = [10,20,30,4]

#method 2
dict_2=zip(keys,values)
print(dict(dict_2))

#method 3
dict_3 = dict([('EKM',10), ('TVM',20), ('KTM',30)])
print(dict_3)

for key, value in dict_3.items():
    print(key,value)

#enumerate example getting the index of each item in a list
for idx,values in enumerate(keys):
    print(idx, values)






