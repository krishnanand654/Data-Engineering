import numpy as np

# arr_1 = np.array([10, 20, 30, 40, 50, 60])
# print(arr_1)

# #number of values present in this list
# print(arr_1.shape) #no of rows, no.of columns
# print(type(arr_1))
# print(arr_1.dtype) #returns the datatype
# # constumize dtype by passing it a named argument to np.array(list, dtype = 'int8')
# print(arr_1.itemsize) 
# print(arr_1.size)   #Returns the total size
# print(arr_1.ndim) #Dimentionality
# print(arr_1.nbytes) #total size of the numpy array

# #type of numpy array
# # create 1-D array
# arr_2 = np.array([10, 15, 17, 21, 23, 44, 65, 89])

# #create a 2-D matrix
# arr_3 = np.array([[10, 15, 17, 21],
#                  [23, 44, 65, 89],
#                  [11, 12, 13, 14]])
# print(arr_3)

# #shape returns (rows, columns)
# print(arr_3.shape)
# print(arr_3.ndim)

# #create a 3-D matrix
# arr_4 = np.array([[[10, 15, 17, 21],
#                  [23, 44, 65, 89],
#                  [11, 12, 13, 14]],

#                  [[20, 25, 27, 23],
#                  [13, 24, 59, 99],
#                  [9, 22, 43, 54]]
#                  ])
# print(arr_4)

# #shape returns (matrices, rows, columns)
# print(arr_4.shape)
# print(arr_4.ndim)
# print(arr_4.itemsize)

# #slicing & indexing in Numpy array
# print(arr_3[0]) #slicing for first row element
# print(arr_3[:,:]) #all rows and all columns
# print(arr_3[:,0]) #elements from all rows and first column
# print(arr_3[:,0:2]) #elements from all rows and first column index


# print(arr_3[1:-1, 1:-1]) #start index = 1 and stop index = last index poisition

# #slicing 3-D numpy array
# #getting 59 from the multidimentional matrix
# print(arr_4[1,1,2])

# #create numpy array using functions
# arr_5 = np.arange(1,51)
# #1-D array
# print(arr_5)

# #create multi-dimentional
# arr_6 = np.arange(1,51).reshape(2, 5, 5)
# print(arr_6)

# #zero matrix : np.zeros(shape)
# arr_7 = np.zeros((5,7), dtype='int16')
# print(arr_7)

# #convert to float type (type casting) from int to float
# # [[0. 0. 0. 0. 0. 0. 0.]
# #  [0. 0. 0. 0. 0. 0. 0.]
# #  [0. 0. 0. 0. 0. 0. 0.]
# #  [0. 0. 0. 0. 0. 0. 0.]
# #  [0. 0. 0. 0. 0. 0. 0.]]
# print(arr_7.astype('float16'))

# #ones matrix
# # [[1 1 1 1 1]
# #  [1 1 1 1 1]
# #  [1 1 1 1 1]
# #  [1 1 1 1 1]
# #  [1 1 1 1 1]]
# arr_8 = np.ones((5,5), dtype='int16')
# print(arr_8)

# #identity matrix : diagonal values one
# # [[1 0 0 0 0]
# #  [0 1 0 0 0]
# #  [0 0 1 0 0]
# #  [0 0 0 1 0]
# #  [0 0 0 0 1]]
# arr_9 = np.identity(5, dtype='int8')
# print(arr_9)

# #empty matrix filled with some value
# # [[4.94e-323]
# #  [7.41e-323]
# #  [1.14e-322]
# #  [2.17e-322]
# #  [5.43e-323]
# #  [5.93e-323]]
# arr_10 = np.empty((6,1))
# print(arr_10)

# #fill the empty matrix
# arr_10.fill(2)
# print(arr_10)

# #full create 1-row with len 10 fill every place with 6.1
# print(np.full(10, 6.1))

# #linspace: create equally spaced array (start, stop, no.of elements)
# print(np.linspace(10,100,10))

# # logspace - N evenly spaced array elements on a log scale between start and stop
# #log base = 10
# print(np.logspace(0, 1, 10, base=10))

# # Exercise 
# new_array = np.zeros((10,10), dtype='int16')
# new_array[0] = 1
# new_array[9] = 1
# new_array[:,0] = 1
# new_array[:,9] = 1
# print(new_array)

# #Exercise 2
# new_array = np.zeros((10,10), dtype='int16')
# new_array[::2,::2] = 1
# new_array[1::2,1::2] = 1
# print(new_array)

#Mathematical operations - on numpy array
arr_13 = np.array([[[1, 3, 5],
                    [4, 8, 7],
                    [9, 11, 13]],

                    [[2, 4, 7],
                    [3, 1, 5],
                    [5, 2, 8]],
                    ])

print(arr_13.sum())
#x = 0 row wise
# [[ 3  7 12]
#  [ 7  9 12]
#  [14 13 21]]
print(arr_13.sum(axis = 0))

#x = 1 column wise addition 1+4+9 = 14 
# [[14 22 25]
#  [10  7 20]]
print(arr_13.sum(axis = 1))

#min value
print(arr_13.min())

#max value
print(arr_13.max())

#where() - returns index position for condition = True
#return index positions where my values are greater than 8
arr_14 = np.arange(1,21).reshape(5,4)
print(np.where(arr_14 > 8))

arr_15 = np.arange(1,37).reshape(6,6)
arr_15.mean() #calculate mean
arr_15.mean(axis=0) #calculate mean row wise
arr_15.mean(axis=1) #calculate mean col wise

np.std(arr_15) #overall standard deviation
np.var(arr_15) #variance

#reverse and array
arr_16 = np.arange(50)
# 0-1 = -1, -1-1 = -2, -2-1 = -3 ......
print(arr_16[::-1])

#flip the array left to right and up to down
print(np.flip(np.arange(1,21).reshape(5,4)))

#flip the rows up to down
print(np.flipud(np.arange(1,21).reshape(5,4)))

#flip the columns left to right
print(np.fliplr(np.arange(1,21).reshape(5,4)))

#Create random array
arr_17 = np.random.randint(10, 50, size = (5,3))
print(arr_17)

#flattern - to convert N-D array into 1-D array
print(arr_17.flatten())

#ravel(): same as flattern: to convert N-D array into 1-D array
print(arr_17.ravel())


arr_18 = np.array([10, 15, 17, 21])

#argmax() returns index position of maximum value along the axis.
print(np.argmax(arr_18))




