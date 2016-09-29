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
>>> np.zeros(10)
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
>>> np.zeros((3,6))
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
>>> np.empty((2,3,2))
array([[[  6.92081461e-310,   8.84197271e-317],
        [  8.78421503e+247,   1.34453222e+161],
        [  5.83439495e+252,   4.95261616e+223]],

       [[  4.44034597e+252,   6.32275170e+233],
        [  6.01346953e-154,   5.28964691e+180],
        [  2.47379808e-091,   4.47593816e-091]]])
>>> # !! you can arrage the values of an array in incremental order with np.arrage(). (this is what I've been looking for).
>>> np.arrage(15)

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    np.arrage(15)
AttributeError: 'module' object has no attribute 'arrage'
>>> np.arange(15)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
>>> # so, you have for the creation of an array: np.array(), np.arange(), np.empty(), np.ones(), np.zeros().
>>> # ...you can create an indentity matrix with np.eye().
>>> np.eye(2,3)
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.]])
>>> # oh, it has to be a square matrix:
>>> np.eye(3,3)
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
>>> # you can covert the dtype of an array using arr.astype() function
>>> # (or is it a method?!)
>>> arr = np.array([1,2,3,4,5])
>>> arr.dtype
dtype('int64')
>>> float_arr = arr.astype(np.float64)
>>> float_arr
array([ 1.,  2.,  3.,  4.,  5.])
>>> float_arr.dtype
dtype('float64')
>>> 
>>> # Operations between arrays and scalars
>>> # batch operations on data without writing for loops!
>>> #(vectorization)
>>> # any arithmetic operations between equal-sized arrays are done elementwise
>>> arr
array([1, 2, 3, 4, 5])
>>> arr*arr
array([ 1,  4,  9, 16, 25])
>>> 1/arr
array([1, 0, 0, 0, 0])
>>> 1/float_arr
array([ 1.        ,  0.5       ,  0.33333333,  0.25      ,  0.2       ])
>>> 
>>> # OPERATIONS BETWEEN DIFFERENTLY SIZED ARRAYS IS CALLED BROADCASTING !
>>> 
>>> # Basic indexing and slicing:
>>> # one-dimensional arrays:
>>> arr= np.arange(10)
>>> arr
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> arr[5]
5
>>> # this is why it is a good idea to start a list at 0! You match the index with the value.
>>> arr[5:8]
array([5, 6, 7])
>>> arr[5:8]=12
>>> arr
array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
>>> # => if you assign a value to a slice, the value is propagated (broadcasted)
>>> # !! SLICES ARE NOT COPIES OF DATA CHUNKS, BUT ARE VIEWS ON THE ORIGINAL DATA! ANY MODIFICATIONS TO THE VIEW WILL BE REFLECTED IN THE SOURCE ARRAY!
>>> arr_slice = arr[5:8]
>>> arr_slice[1]=12345
>>> arr
array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,     9])
>>> arr_slice[:]=64
>>> arr
array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
>>> # [:] => from the start to the end of an one-dimensional array
>>> 
>>> # if you need to copy a slice to an ndarray instead of having a view, you need to explicitly copy the array.
>>> myslice= arr[5:8].copy()
>>> 
>>> myslice
array([64, 64, 64])
>>> 
>>> # indexing and slicing higher-dimensional arrays :
>>> 
>>> arr2d= np.array([1,2,3], [4,5,6], [7,8,9])

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    arr2d= np.array([1,2,3], [4,5,6], [7,8,9])
ValueError: only 2 non-keyword arguments accepted
>>> arr2d= np.array([[1,2,3], [4,5,6], [7,8,9]])
>>> arr2d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> # (the small lists inside the large list are the individual rows, all first elements of the small lists form the first column, all the second elements of the samll lists form the second column, all third elements of the small lists form the third column.
>>> # axis 0 is the row axis and axis 1 is the column axis.
>>> arr2d[2] # selects the third small list of the large list
array([7, 8, 9])
>>> # you select individual items with a(r,c):
>>> arr2d[0,1] # element of the first row and second column
2
>>> arr2d[:1]
array([[1, 2, 3]])
>>> arr2d[1:]
array([[4, 5, 6],
       [7, 8, 9]])
>>> arr2d[:2]
array([[1, 2, 3],
       [4, 5, 6]])
>>> arr2d[2:]
array([[7, 8, 9]])
>>> # so, if you leave out an index in multidimensional arrays, the returned object will be a lower dimensional ndarray consisting of all the data along the higher dimensions. In the above case it returns the complete rows!
>>> # [:1] the first complete row, [1:] without the first complete row, [:2] the first two rows, [2:] without the first two rows.
>>> # if you have axis 0 and axis 1, leaving out an index will return axis 0, i.e. the rows!
>>> 
>>> # 3darrays:
>>> arr3d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
>>> arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> arr3d[0]
array([[1, 2, 3],
       [4, 5, 6]])
>>> old_values = arr3d[0].copy()
>>> arr3d[0]=42
>>> arr3d
array([[[42, 42, 42],
        [42, 42, 42]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> arr3d[0]= old_values
>>> arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> arr3d[1,0]
array([7, 8, 9])
>>> # if takes out the second item of the array and from the second item the first item (so, the first list of the second list of lists)
>>> # SLICING HIGHER-DIMENSIONAL ARRAYS - you can slice one or more axes and also mix integers/
>>> # A slice selects a range of elements along an axis.
>>> 
