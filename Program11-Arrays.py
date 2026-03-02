# Program Name: Program11-Arrays.py

# Numpy Introduction
# pip install numpy


import numpy as np

a = np.array ([[1, 2, 3],
               [4, 5, 6] ] )
print(a.shape)  #o/p:(2, 3)



# Array fundamentals
# One way to initialize an array is using a Python sequence, such as a list. 
# For example:
b = np.array ( [1, 2, 3, 4, 5, 6] )
print (b)   #o/p: [1 2 3 4 5 6]
print(b[0]) #o/p: 1


# Like the original list, the array is mutable.
b[0] = 10
print (b)   # o/p: [10  2  3  4  5  6]


# Also like the original list, Python slice notation can be used for indexing.
print (b[:3])   # o/p: [10  2  3]


# One major difference is that slice indexing of a list copies the elements into a new list, but slicing an array returns a view: an object that refers to the data in the original array. The original array can be mutated using the view.
c = b[3:]   
print(c)    # o/p: [4 5 6]
c[0] = 40
print(b)    #o/p: [10  2  3 40  5  6]


# Two- and higher-dimensional arrays can be initialized from nested Python sequences:
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
'''
o/p: 
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

'''

print(a[1, 3])  #o/p: 8


# Array attributes:
# This section covers the ndim, shape, size, and dtype attributes of an array.

# The number of dimensions of an array is contained in the ndim attribute.
print(a.ndim)   #o/p: 2

ar1= np.array ( [1,2,3,4])
print(ar1.ndim) #o/p: 1

ar2= np.array ( [  [1,2],[3,4]  ])
print(ar2.ndim) #o/p: 2

ar3= np.array ( [[[1,2],[3,4]],
                 [[5,6],[7,8]],
                 [[9,10],[11,12]]])
print(ar3.ndim) #o/p: 3


# The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension.
print(a.shape)  #o/p:(3, 4)
print(len(a.shape) == a.ndim)   # o/p: True


# The fixed, total number of elements in array is contained in the size attribute.
print(a.size)   # o/p: 12


import math 
print(a.size == math.prod(a.shape))     #o/p: True

# Arrays are typically “homogeneous”, meaning that they contain elements of only one “data type”. The data type is recorded in the dtype attribute.
print(a.dtype)  #o/p: int64 # # "int" for integer, "64" for 64-bit




# How to create a basic array
# This section covers np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()

# Besides creating an array from a sequence of elements, you can easily create an array filled with 0’s:
print(np.zeros(2))  #o/p: [0. 0.]


# Or an array filled with 1’s:
print(np.ones(2))   #o/p: [1. 1.]


# Or even an empty array! The function empty creates an array whose initial content is random and depends on the state of the memory. The reason to use empty over zeros (or something similar) is speed - just make sure to fill every element afterwards!
# Create an empty array with 2 elements
print(np.empty(2))  #o/p: [1. 1.]  # may vary



# You can create an array with a range of elements:
print(np.arange(4)) #o/p: [0 1 2 3]

# And even an array that contains a range of evenly spaced intervals. To do this, you will specify the first number, last number, and the step size.
print(np.arange(2, 9, 2))   #[2 4 6 8]


# You can also use np.linspace() to create an array with values that are spaced linearly in a specified interval:
print(np.linspace(0, 10, num=5))        #o/p: [ 0.   2.5  5.   7.5 10. ]




# Can you reshape an array? Yes
# This section covers arr.reshape()

# Using arr.reshape() will give a new shape to an array without changing the data. Just remember that when you use the reshape method, the array you want to produce needs to have the same number of elements as the original array. If you start with an array with 12 elements, you’ll need to make sure that your new array also has a total of 12 elements.
# If you start with this array:
a = np.arange(6)
print(a)    # o/p: [0 1 2 3 4 5]

# You can use reshape() to reshape your array. For example, you can reshape this array to an array with three rows and two columns:
b = a.reshape(3, 2)
print(b)    
# o/p: 
'''
[[0 1]
 [2 3]
 [4 5]]
'''

# With np.reshape, you can specify a few optional parameters:
print(np.reshape(a, shape=(1, 6), order='C'))   # o/p: [[0 1 2 3 4 5]]
