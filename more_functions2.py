Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> ##### Methods for Boolean Arrays #####
>>> 
>>> arr= np.array((np.random.randn(100)), dtype=bool)
>>> arr
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,  True], dtype=bool)
>>> data= np.random.binomial(100)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data= np.random.binomial(100)
  File "mtrand.pyx", line 3909, in mtrand.RandomState.binomial (numpy/random/mtrand/mtrand.c:27883)
TypeError: binomial() takes at least 2 positional arguments (1 given)
>>> data= np.random.binomial(100)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data= np.random.binomial(100)
  File "mtrand.pyx", line 3909, in mtrand.RandomState.binomial (numpy/random/mtrand/mtrand.c:27883)
TypeError: binomial() takes at least 2 positional arguments (1 given)
>>> trials=5
>>> prob= .5
>>> data=data= np.random.binomial(trials, prob, 100)
>>> data
array([3, 2, 2, 1, 4, 3, 3, 2, 0, 4, 3, 3, 0, 4, 5, 2, 1, 2, 3, 2, 2, 4, 1,
       2, 2, 1, 1, 5, 3, 2, 2, 3, 2, 4, 1, 3, 1, 1, 3, 2, 1, 2, 4, 1, 1, 3,
       1, 3, 2, 3, 2, 3, 4, 2, 1, 2, 1, 3, 4, 1, 2, 2, 1, 3, 3, 1, 1, 1, 2,
       4, 2, 2, 2, 2, 2, 4, 3, 1, 1, 3, 2, 4, 4, 2, 2, 4, 2, 2, 1, 2, 2, 4,
       3, 4, 1, 4, 2, 1, 3, 2])
>>> trials=1
>>> prob= .5
>>> data=data= np.random.binomial(trials, prob, 100)
>>> data
array([0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1,
       0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
       0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0,
       0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1,
       0, 1, 0, 1, 0, 1, 1, 1])
>>> # boolean values can be also expressed as a binomial result, when True and False are coerced to 1 and 0.
>>> (arr>0).sum()
100
>>> (arr<1).sum()
0
>>> (arr==0).sum()
0
>>> (data<1).sum()
54
>>> (data>0).sum()
46
>>> # see the randomness in this expreriment: chances are .5 but we've got 54 0s and 46 1s.
>>> 
>>> ##### Sorting #####
>>> 
>>> arr = np.random.randn(8)
>>> arr
array([ 0.22333642,  0.31627779, -0.77968517,  0.26682638,  1.03296566,
        1.48188523,  0.92474839,  0.24198216])
>>> arr.sort
<built-in method sort of numpy.ndarray object at 0x7fa5e8c2dd50>
>>> arr.sort()
>>> arr
array([-0.77968517,  0.22333642,  0.24198216,  0.26682638,  0.31627779,
        0.92474839,  1.03296566,  1.48188523])
>>> # you can sort along an axis
>>> 
>>> arr=np.random.randn(5,3)
>>> arr
array([[ 0.01709549,  0.93088898, -0.87006592],
       [-0.48973368,  2.82458951,  0.74143283],
       [ 1.11524929,  0.97327728, -0.6175459 ],
       [ 0.02859875,  0.59443227,  1.30018985],
       [-0.53318894,  1.36858409,  0.90523897]])
>>> arr.sort(1)
>>> arr
array([[-0.87006592,  0.01709549,  0.93088898],
       [-0.48973368,  0.74143283,  2.82458951],
       [-0.6175459 ,  0.97327728,  1.11524929],
       [ 0.02859875,  0.59443227,  1.30018985],
       [-0.53318894,  0.90523897,  1.36858409]])
>>> # axis 1 are the rows
>>> arr.sort(2)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    arr.sort(2)
ValueError: axis(=2) out of bounds
>>> arr.sort(0)
>>> arr
array([[-0.87006592,  0.01709549,  0.93088898],
       [-0.6175459 ,  0.59443227,  1.11524929],
       [-0.53318894,  0.74143283,  1.30018985],
       [-0.48973368,  0.90523897,  1.36858409],
       [ 0.02859875,  0.97327728,  2.82458951]])
>>> # axis 0 are the columns
>>> # np.sort returns a sorted copy of an array.
>>> 
>>> # try to compute quantiles of an array using np.sort
>>> large_arr = np.random.randn(1000)
>>> large_arr.sort
<built-in method sort of numpy.ndarray object at 0x7fa5e8c2dd50>
>>> large_arr.sort()
>>> large_arr[int(0.05*len(large_arr))]
-1.5740961606411874
>>> # this is the 5% quantile!
>>> len(large_arr)
1000
>>> 0.05*1000
50.0
>>> large_arr[50]
-1.5740961606411874
>>> 
>>> ##### Set Logic #####
>>> 
>>> names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
>>> np.unique(names)
array(['Bob', 'Joe', 'Will'], 
      dtype='|S4')
>>> ints = np.array([3,3,3,2,2,1,1,4,4])
>>> np.unique(ints)
array([1, 2, 3, 4])
>>> 
>>> values = np.array([6,0,0,3,2,5,6])
>>> np.in1d(values, [2,3,6])
array([ True, False, False,  True,  True, False,  True], dtype=bool)
>>> # it showed where in the values array is one of the items in [2,3,6].
>>> ints2= np.array([2,5,6,7,1])
>>> ints
array([3, 3, 3, 2, 2, 1, 1, 4, 4])
>>> ints2
array([2, 5, 6, 7, 1])
>>> intersect1d(ints, ints2)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    intersect1d(ints, ints2)
NameError: name 'intersect1d' is not defined
>>> np.intersect1d(ints, ints2)
array([1, 2])
>>> # intersection between 2 1darrays
>>> np.union1d(ints, ints2)
array([1, 2, 3, 4, 5, 6, 7])
>>> # union between 2 1darrays
>>> np.setdiff1d(ints, ints2)
array([3, 4])
>>> # set difference, elements in ints that are not in ints2
>>> np.setxor1d(ints, ints2)
array([3, 4, 5, 6, 7])
>>> # set symmetric difference => elements that are in either of the arrays, but not both
>>> 
>>> # from Wes McKinney(2013)
>>> 
