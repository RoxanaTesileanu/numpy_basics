Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # some statistical estimates can be computed for the sample of norm. distrib. data:
>>> 
>>> import numpy as np
>>> arr= np.random.randn(5,4)
>>> arr
array([[-1.86272178, -1.2259515 , -0.80604716, -1.32662273],
       [ 0.39516912,  0.66947401, -2.53345164, -1.37575197],
       [ 0.11944553, -0.77548441,  0.10943983,  1.69801207],
       [ 0.78724673, -0.7401261 , -1.30092856,  0.90901747],
       [-1.64462203, -1.29974795, -0.44879758,  0.61764661]])
>>> arr.mean
<built-in method mean of numpy.ndarray object at 0x7fd308393b20>
>>> mean = arr.mean
>>> mean
<built-in method mean of numpy.ndarray object at 0x7fd308393b20>
>>> print mean
<built-in method mean of numpy.ndarray object at 0x7fd308393b20>
>>> arr.mean()
-0.50174010267803315
>>> print mean
<built-in method mean of numpy.ndarray object at 0x7fd308393b20>
>>> mean = arr.mean()
>>> print mean
-0.501740102678
>>> np.mean(arr)
-0.50174010267803315
>>> arr.sum()
-10.034802053560663
>>> # you can compute the statistic only along an axis:
>>> arr.mean(axis=1)
array([-1.30533579, -0.71114012,  0.28785325, -0.08619761, -0.69388024])
>>> # axis 0 along the rows, axis 1 along the columns
>>> arr.sum(0)
array([-2.20548243, -3.37183594, -4.97978512,  0.52230144])
>>> arr.sum(axis=0)
array([-2.20548243, -3.37183594, -4.97978512,  0.52230144])
>>> np.sum(arr[0])
-5.2213431669737584
>>> arr[0]
array([-1.86272178, -1.2259515 , -0.80604716, -1.32662273])
>>> arr.sum(axis=1)
array([-5.22134317, -2.84456048,  1.15141302, -0.34479046, -2.77552096])

>>> # you can also compute the cumsum and cumprod:
>>> arr.cumsum(0)
array([[-1.86272178, -1.2259515 , -0.80604716, -1.32662273],
       [-1.46755266, -0.55647749, -3.3394988 , -2.7023747 ],
       [-1.34810713, -1.33196189, -3.23005898, -1.00436263],
       [-0.5608604 , -2.07208799, -4.53098754, -0.09534517],
       [-2.20548243, -3.37183594, -4.97978512,  0.52230144]])
>>> arr.cumprod(1)
array([[-1.86272178,  2.28360656, -1.84069459,  2.44190727],
       [ 0.39516912,  0.26455545, -0.67023845,  0.92208187],
       [ 0.11944553, -0.09262814, -0.01013721, -0.0172131 ],
       [ 0.78724673, -0.58266185,  0.75800145,  0.68903655],
       [-1.64462203,  2.13759412, -0.95934708, -0.59253747]])
>>> # ok, so I've mixed up the axes: axis zero along columns and axis 1 along rows!!
>>> np.std(arr)
1.0825216357108278
>>> np.var(arr)
1.171853091782046
>>> np.min(arr)
-2.5334516403498211
>>> np.max(arr)
1.6980120660676756
>>> np.argmin(arr)
6
>>> arr
array([[-1.86272178, -1.2259515 , -0.80604716, -1.32662273],
       [ 0.39516912,  0.66947401, -2.53345164, -1.37575197],
       [ 0.11944553, -0.77548441,  0.10943983,  1.69801207],
       [ 0.78724673, -0.7401261 , -1.30092856,  0.90901747],
       [-1.64462203, -1.29974795, -0.44879758,  0.61764661]])
>>> np.argmax(arr)
11
>>> arr[6]

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    arr[6]
IndexError: index 6 is out of bounds for axis 0 with size 5
>>> # I've thought it returns a tuple of x,y values....
>>> arr(:6)
SyntaxError: invalid syntax
>>> arr(:, :6)
SyntaxError: invalid syntax
>>> arr([:], [:6])
SyntaxError: invalid syntax
>>> arr([], [:6])
SyntaxError: invalid syntax
>>> arr([], [6])

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    arr([], [6])
TypeError: 'numpy.ndarray' object is not callable
>>> for i in range(len(arr)) :
	return i=6
SyntaxError: invalid syntax
>>> 
>>> len(arr)
5
>>> arr.reshape(1)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    arr.reshape(1)
ValueError: total size of new array must be unchanged
>>> arr.reshape(1,1)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    arr.reshape(1,1)
ValueError: total size of new array must be unchanged
>>> arr.reshape((1,1))

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    arr.reshape((1,1))
ValueError: total size of new array must be unchanged
>>> arr
array([[-1.86272178, -1.2259515 , -0.80604716, -1.32662273],
       [ 0.39516912,  0.66947401, -2.53345164, -1.37575197],
       [ 0.11944553, -0.77548441,  0.10943983,  1.69801207],
       [ 0.78724673, -0.7401261 , -1.30092856,  0.90901747],
       [-1.64462203, -1.29974795, -0.44879758,  0.61764661]])
>>> arr.reshape((1,1))

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    arr.reshape((1,1))
ValueError: total size of new array must be unchanged
>>> newarr=[]
>>> for i in range(arr[i]+1) :
	newarr.append(i)

	

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for i in range(arr[i]+1) :
NameError: name 'i' is not defined
>>> for i in range(arr[i]+1) :
	newarr.append(arr[i])

	

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    for i in range(arr[i]+1) :
NameError: name 'i' is not defined
>>> for i in range(arr[i]+1) :
	newarr.append([i])

	

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    for i in range(arr[i]+1) :
NameError: name 'i' is not defined
>>> for i in range(len(arr)) :
	newarr.append(i)

	
>>> newarr
[0, 1, 2, 3, 4]
>>> for i in range(len(arr)) :
	newarr.append(arr[i])

	
>>> newarr
[0, 1, 2, 3, 4, array([-1.86272178, -1.2259515 , -0.80604716, -1.32662273]), array([ 0.39516912,  0.66947401, -2.53345164, -1.37575197]), array([ 0.11944553, -0.77548441,  0.10943983,  1.69801207]), array([ 0.78724673, -0.7401261 , -1.30092856,  0.90901747]), array([-1.64462203, -1.29974795, -0.44879758,  0.61764661])]
>>> newarr.remove(0:4)
SyntaxError: invalid syntax
>>> newarr.remove[0:4]

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    newarr.remove[0:4]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> newarr.remove[0]

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    newarr.remove[0]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> newarr.remove[0]

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    newarr.remove[0]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> newarr.remove(0)
>>> newarr
[1, 2, 3, 4, array([-1.86272178, -1.2259515 , -0.80604716, -1.32662273]), array([ 0.39516912,  0.66947401, -2.53345164, -1.37575197]), array([ 0.11944553, -0.77548441,  0.10943983,  1.69801207]), array([ 0.78724673, -0.7401261 , -1.30092856,  0.90901747]), array([-1.64462203, -1.29974795, -0.44879758,  0.61764661])]
>>> newarr.remove(1,2,3,4)

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    newarr.remove(1,2,3,4)
TypeError: remove() takes exactly one argument (4 given)
>>> newarr.remove(1)
>>> newarr
[2, 3, 4, array([-1.86272178, -1.2259515 , -0.80604716, -1.32662273]), array([ 0.39516912,  0.66947401, -2.53345164, -1.37575197]), array([ 0.11944553, -0.77548441,  0.10943983,  1.69801207]), array([ 0.78724673, -0.7401261 , -1.30092856,  0.90901747]), array([-1.64462203, -1.29974795, -0.44879758,  0.61764661])]
>>> .remove(2)
SyntaxError: invalid syntax
>>> newarr.remove(3)
>>> newarr.remove(4)
>>> newarr
[2, array([-1.86272178, -1.2259515 , -0.80604716, -1.32662273]), array([ 0.39516912,  0.66947401, -2.53345164, -1.37575197]), array([ 0.11944553, -0.77548441,  0.10943983,  1.69801207]), array([ 0.78724673, -0.7401261 , -1.30092856,  0.90901747]), array([-1.64462203, -1.29974795, -0.44879758,  0.61764661])]
>>> newarr.remove(0)

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    newarr.remove(0)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> newarr.remove(2)
>>> newarr = newarr
>>> newarr
[array([-1.86272178, -1.2259515 , -0.80604716, -1.32662273]), array([ 0.39516912,  0.66947401, -2.53345164, -1.37575197]), array([ 0.11944553, -0.77548441,  0.10943983,  1.69801207]), array([ 0.78724673, -0.7401261 , -1.30092856,  0.90901747]), array([-1.64462203, -1.29974795, -0.44879758,  0.61764661])]
>>> newarr[6]

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    newarr[6]
IndexError: list index out of range
>>> newarr(6)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    newarr(6)
TypeError: 'list' object is not callable
>>> 
>>> # if I can't turn a 2D array into a 1D array then  I can't use the index 6 to find out which value it contains
>>> 
>>> 
>>> ################################################################################################
>>> # Methods for Boolean Arrays #
>>> 
========================================= RESTART: Shell =========================================
>>> 
