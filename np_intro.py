Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # from McKinney (2013)
>>> # NumPy is mainly used for: (i) array operations for data munging, subsetting, filtering, transformation, (ii) array algorithms like sorting, set operations, (iii) descriptive statistics and aggregating data, (iv) data alignment for merging heterogeneous data, (v) expresssing conditional logic as array expressions, (vi) group-wise data manupulations like aggregation, transf., function application).
>>> import numpy as np
>>> data = np.empty((2, 3), float32)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data = np.empty((2, 3), float32)
NameError: name 'float32' is not defined
>>> data = np.empty((2, 3), np.float32)
>>> data
array([[  2.85829910e-38,   0.00000000e+00,  -2.37549495e-23],
       [  4.57019481e-41,   4.48415509e-44,   0.00000000e+00]], dtype=float32)
>>> data[0,0]
2.8582991e-38
>>> data[0,0] = 0.9526
>>> data[0,1]=-0.246
>>> data[0,2] = -0.8856
>>> data[1,0]=0.5639
>>> data[1,1]=0.2379
>>> data[1,2]=0.9104
>>> data
array([[ 0.9526    , -0.24600001, -0.88559997],
       [ 0.56389999,  0.2379    ,  0.91039997]], dtype=float32)
>>> data*10
array([[ 9.52600002, -2.46000004, -8.85599995],
       [ 5.63899994,  2.37899995,  9.10400009]], dtype=float32)
>>> # so, you can multiply an array with a number like a matrix
>>> data+data
array([[ 1.9052    , -0.49200001, -1.77119994],
       [ 1.12779999,  0.47580001,  1.82079995]], dtype=float32)
>>> # you can add an array to anather array when it has the same shape
>>> data.shape
(2, 3)
>>> # you can find out the shape of the array with .shape
>>> # => ARRAYS ENABLE YOU TO PERFORM MATHEMATICAL OPERATIONS ON WHOLE BLOCKS OF DATA
>>> 
>>> #ndarrays are one category of array objects. An ndarray is a multidimensional container of items of the same type and size.
>>> 
>>> # Every array has a shape ( a tuple indicating the size of each dimension) and a dtype (an object indicating the data type of the array).
>>> data.dtype
dtype('float32')
>>> 
>>> # creating ndarrays
>>> data1= [6, 7.5, 8, 0, 1]
>>> arr1 = np.array(data1)
>>> arr1
array([ 6. ,  7.5,  8. ,  0. ,  1. ])
>>> arr1.dtype
dtype('float64')
>>> # so, you can have as an input for an array: a simple list, or a nested sequence like a list of equal-lenght lists!
>>> data2 = [[1,2,3,4], [5,6,7,8]]
>>> # this is a list containing two lists
>>> arr2 = np.array(data2)
>>> arr2
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
>>> arr2.ndim
2
>>> arr2.shape
(2, 4)
>>> # => A NESTED SEQUENCE WILL BE CONVERTED INTO A MULTIDIMENSIONAL ARRAY!
>>> 
>>> # In addition to np.array, you can use np.zeros or np.ones to create arrays of 0s and 1s and np.empty to create an array without initializing its values.
>>> 
