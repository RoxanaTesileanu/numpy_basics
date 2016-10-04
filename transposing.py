Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> # transposing returns a view without copying anything.
>>> arr = np.arange(15).reshape((3,5))
>>> arr.T
array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])
>>> arr
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> # det A^T = det A
>>> # useful if you want to ever calculate the inner product of two vectors in matrix form: a*b=a^T*b
>>> arr2= np.random.randn(6,3)
>>> arr2
array([[ 0.89175203, -0.74783546,  0.91505109],
       [-0.41880405,  0.16994219,  0.01398439],
       [-0.74027214,  0.54429399, -0.02500947],
       [-1.53383509, -0.23560946, -1.32108333],
       [ 0.84407849, -0.57392079,  0.07200237],
       [-0.28388188,  0.10019145, -1.52070052]])
>>> np.dot(arr2.T, arr)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    np.dot(arr2.T, arr)
ValueError: shapes (3,6) and (3,5) not aligned: 6 (dim 1) != 3 (dim 0)
>>> np.dot(arr2.T, arr2)
array([[ 4.66432887, -1.29247262,  3.3474547 ],
       [-1.29247262,  1.27932939, -0.57796874],
       [ 3.3474547 , -0.57796874,  4.9011151 ]])
>>> # for higher dimensional arrays transpose method accepts a tuple of axis numbers to permute the axes:
>>> arr3=np.arange(16).reshape(2,2,4) # two items each with 2 rows and 4 columns
>>> arr3
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])
>>> arr.transpose((1,0,2))

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    arr.transpose((1,0,2))
ValueError: axes don't match array
>>> arr3.transpose((1,0,2))
array([[[ 0,  1,  2,  3],
        [ 8,  9, 10, 11]],

       [[ 4,  5,  6,  7],
        [12, 13, 14, 15]]])
>>> arr3
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])
>>> arr.swapaxes(1,2)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    arr.swapaxes(1,2)
ValueError: bad axis2 argument to swapaxes
>>> arr3.swapaxes(1,2)
array([[[ 0,  4],
        [ 1,  5],
        [ 2,  6],
        [ 3,  7]],

       [[ 8, 12],
        [ 9, 13],
        [10, 14],
        [11, 15]]])
>>> # from Wes McKinney (2013)
