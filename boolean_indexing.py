Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
>>> data = randn(7,4)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data = randn(7,4)
NameError: name 'randn' is not defined
>>> data = np.rndn(7,4)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data = np.rndn(7,4)
AttributeError: 'module' object has no attribute 'rndn'
>>> data= np.randn(7,4)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data= np.randn(7,4)
AttributeError: 'module' object has no attribute 'randn'
>>> data= np.random(7,4)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data= np.random(7,4)
TypeError: 'module' object is not callable
>>> from numpy import random
>>> data= np.randn(7,4)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data= np.randn(7,4)
AttributeError: 'module' object has no attribute 'randn'
>>> data= np.random
>>> data = np.randn(7,4_
		
SyntaxError: invalid syntax
>>> data = np.randn(7,4)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data = np.randn(7,4)
AttributeError: 'module' object has no attribute 'randn'
>>> 
========================================= RESTART: Shell =========================================
>>> import numpy as np
>>> import numpy.random
>>> data = np.random(7)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data = np.random(7)
TypeError: 'module' object is not callable
>>> numpy.random(7)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    numpy.random(7)
TypeError: 'module' object is not callable
>>> np.random.normal(7)
7.676448956141504
>>> 
========================================= RESTART: Shell =========================================
>>> import numpy as np
>>> # use the function np.random.normal()
>>> np.random.randn(7,4)
array([[ 1.39911566, -0.83703526, -1.28780229,  1.171044  ],
       [ 1.65853048,  0.21245124, -0.14060627,  0.84365293],
       [-0.4591814 , -0.48806503,  0.31264996, -0.06255551],
       [ 0.8491481 ,  0.20648235, -0.32742787, -0.75176428],
       [-0.89552067,  1.24223112,  0.56876088, -0.22553177],
       [ 0.55637173, -0.22585074,  0.02896416,  0.26998799],
       [ 0.80911703, -1.68311781, -1.34651131,  0.33045153]])
>>> # np.random.randn() returns a sample from the standard Normal distribution
>>> 
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
>>> data=np.random.randn(7,4)
>>> names
array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], 
      dtype='|S4')
>>> # let's look only at names now:
>>> names=='Bpb'
array([False, False, False, False, False, False, False], dtype=bool)
>>> names=='Bob'
array([ True, False, False,  True, False, False, False], dtype=bool)
>>> # I've obtained a Boolean array indicating where in the list of strings appears Bob.
>>> 
>>> # data[names=='Bob']
>>> # what this means is that you take the boolean array and at the indexes when it prints TRUE, you spit out the rows of random numbers.
>>> # you can probably use it to find correspondences between two arrays.
>>> data[names=='Bob']
array([[ 1.79150183, -0.56791619, -1.26428799, -0.33307961],
       [-0.06454025,  1.23850419,  0.498643  , -1.0054507 ]])
>>> data
array([[ 1.79150183, -0.56791619, -1.26428799, -0.33307961],
       [-0.28534853,  0.25384393,  0.08612657,  0.18678145],
       [-1.65862996, -1.13497903,  2.37042692, -0.32649542],
       [-0.06454025,  1.23850419,  0.498643  , -1.0054507 ],
       [ 0.69990009,  0.20123548, -0.41576065,  1.41743773],
       [-0.14384815,  1.04318141,  0.27037958,  0.41289764],
       [ 0.85966636,  0.89106192,  0.29237064,  1.94651405]])
>>> # the rows number is the data array must be the same as the length of the boolean array.
>>> data[names=='Bob', 2:]
array([[-1.26428799, -0.33307961],
       [ 0.498643  , -1.0054507 ]])
>>> data[names=='Bob', 3]
array([-0.33307961, -1.0054507 ])
>>> # to exclude Bob you can either use != or - :
>>> names!= 'Bob'
array([False,  True,  True, False,  True,  True,  True], dtype=bool)
>>> data[-(names=='Bob')] # select the indices that do not refer to Bob
array([[-0.28534853,  0.25384393,  0.08612657,  0.18678145],
       [-1.65862996, -1.13497903,  2.37042692, -0.32649542],
       [ 0.69990009,  0.20123548, -0.41576065,  1.41743773],
       [-0.14384815,  1.04318141,  0.27037958,  0.41289764],
       [ 0.85966636,  0.89106192,  0.29237064,  1.94651405]])
>>> # combine multiple boolean conditions with & (and) and | (or):
>>> mask = (names=='Bob')| (names=='Will')
>>> mask
array([ True, False,  True,  True,  True, False, False], dtype=bool)
>>> data[mask]
array([[ 1.79150183, -0.56791619, -1.26428799, -0.33307961],
       [-1.65862996, -1.13497903,  2.37042692, -0.32649542],
       [-0.06454025,  1.23850419,  0.498643  , -1.0054507 ],
       [ 0.69990009,  0.20123548, -0.41576065,  1.41743773]])
>>> data[data<0]=0
>>> data
array([[ 1.79150183,  0.        ,  0.        ,  0.        ],
       [ 0.        ,  0.25384393,  0.08612657,  0.18678145],
       [ 0.        ,  0.        ,  2.37042692,  0.        ],
       [ 0.        ,  1.23850419,  0.498643  ,  0.        ],
       [ 0.69990009,  0.20123548,  0.        ,  1.41743773],
       [ 0.        ,  1.04318141,  0.27037958,  0.41289764],
       [ 0.85966636,  0.89106192,  0.29237064,  1.94651405]])
>>> data[names != 'Joe']=7
>>> data
array([[ 7.        ,  7.        ,  7.        ,  7.        ],
       [ 0.        ,  0.25384393,  0.08612657,  0.18678145],
       [ 7.        ,  7.        ,  7.        ,  7.        ],
       [ 7.        ,  7.        ,  7.        ,  7.        ],
       [ 7.        ,  7.        ,  7.        ,  7.        ],
       [ 0.        ,  1.04318141,  0.27037958,  0.41289764],
       [ 0.85966636,  0.89106192,  0.29237064,  1.94651405]])
>>> 
>>> # from Wes McKinney (2013) - 'Python for Data Analysis'
>>> 
