Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> arr = np.arange(32).reshape((8,4))
>>> arr
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])
>>> # passing multiple index arrays => selects a 1D array of elements corresponding to each tuple of indices:
>>> arr[[1,5,7,2], [0,3,1,2]]
array([ 4, 23, 29, 10])
>>> # => took out the elements (1,0), (5,3), (7,1), (2,2).
>>> # again, select a row:
>>> arr[1]
array([4, 5, 6, 7])
>>> # select column:
>>> arr[, 1]
SyntaxError: invalid syntax
>>> arr[, [1]]
SyntaxError: invalid syntax
>>> arr[:, [1]]
array([[ 1],
       [ 5],
       [ 9],
       [13],
       [17],
       [21],
       [25],
       [29]])
>>> # now select a subset of the matrix's rows and columns:
>>> arr[[1,5,7,2]][:,[0,3,1,2]]
array([[ 4,  7,  5,  6],
       [20, 23, 21, 22],
       [28, 31, 29, 30],
       [ 8, 11,  9, 10]])
>>> # another way to select a subset of rows and columns is to use the np.ix_ function:
>>> arr[np.ix_([1,5,7,2], [0,3,1,2])]
array([[ 4,  7,  5,  6],
       [20, 23, 21, 22],
       [28, 31, 29, 30],
       [ 8, 11,  9, 10]])
>>> 
>>> # KEEP IN MIND THAT FANCY INDEXING, UNLIKE SLICING, ALWAYS COPIES THE DATA INTO A NEW ARRAY!
>>> 
