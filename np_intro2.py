Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> list1 = np.arange(0,10)
>>> list1
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list2 = np.arange(10, 20)
>>> list2
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>> myarr2d= ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>> myarr2d.count
<built-in method count of tuple object at 0x7f200612d290>
>>> myarr2d.count()

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myarr2d.count()
TypeError: count() takes exactly one argument (0 given)
>>> myarr2d=np.array(myarr2d)
>>> myarr2d
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])
>>> myarr2d.shape
(2, 10)
>>> myarr2d.reshape(4, 5)
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
>>> myarr2d[1]
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>> myarr2d=myarr2d.reshape(4, 5)
>>> myarr2d[1]
array([5, 6, 7, 8, 9])
>>> myarr2d[0]
array([0, 1, 2, 3, 4])
>>> myarr2d[:, 0]
array([ 0,  5, 10, 15])
>>> # I've made it to select the first column!
>>> myarr2d[,0]
SyntaxError: invalid syntax
>>> myarr2d[:, 0]
array([ 0,  5, 10, 15])
>>> myarr2d[1:2, 2:3]
array([[7]])
>>> myarr2d[1:2, 2:2]
array([], shape=(1, 0), dtype=int64)
>>> myarr2d[1:2, 2:3]
array([[7]])
>>> myarr2d[1:1, 1:2]
array([], shape=(0, 1), dtype=int64)
>>> myarr2d[1:1, 1:1]
array([], shape=(0, 0), dtype=int64)
>>> myarr2d[1:1, 1:1]
array([], shape=(0, 0), dtype=int64)
>>> myarr2d[1:1]
array([], shape=(0, 5), dtype=int64)
>>> myarr2d[1:1]
array([], shape=(0, 5), dtype=int64)
>>> myarr2d[1]
array([5, 6, 7, 8, 9])
>>> myarr2d[0:1]
array([[0, 1, 2, 3, 4]])
>>> myarr2d[0]
array([0, 1, 2, 3, 4])
>>> myarr2d[0:2]
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> myarr2d[0:2, 1:3]
array([[1, 2],
       [6, 7]])
>>> # from row 0 to row 2 without it, from column 1 to column 3 without it
>>> # it works like this: arr2d[axis 0, axis 1]
>>> myarr2d[:, :1]
array([[ 0],
       [ 5],
       [10],
       [15]])
>>> myarr2d[:, 1]
array([ 1,  6, 11, 16])
>>> myarr2d[:, 2]
array([ 2,  7, 12, 17])
>>> myarr2d[:, :2]
array([[ 0,  1],
       [ 5,  6],
       [10, 11],
       [15, 16]])
>>> # with : you get into the structure of the axis and only with , you choose an individual element
>>> # you can assign to a whole slice a value:
>>> myarr2d[:,:2]=1
>>> myarr2d
array([[ 1,  1,  2,  3,  4],
       [ 1,  1,  7,  8,  9],
       [ 1,  1, 12, 13, 14],
       [ 1,  1, 17, 18, 19]])
>>> # from Wes McKinney (2013)
