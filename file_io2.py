Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ## Saving and loading text files ##
>>> 
>>> !cat </home/Desktop/mypoints_data.txt>
SyntaxError: invalid syntax
>>> import os
>>> import numpy as np
>>> !cat </home/Desktop/mypoints_data.txt>
SyntaxError: invalid syntax
>>> arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter=',')

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter=',')
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '//home/Desktop/mypoints_data.txt'
>>> import numpyio

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import numpyio
ImportError: No module named numpyio
>>> import npyio

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import npyio
ImportError: No module named npyio
>>> import sys
>>> arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter=',')

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter=',')
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '//home/Desktop/mypoints_data.txt'
>>> import csv
>>> arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter='')

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter='')
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '//home/Desktop/mypoints_data.txt'
>>> arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter='', skiprows=1)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter='', skiprows=1)
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '//home/Desktop/mypoints_data.txt'
>>> arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter='\t', skiprows=1)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    arr = np.loadtxt('//home/Desktop/mypoints_data.txt', delimiter='\t', skiprows=1)
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '//home/Desktop/mypoints_data.txt'
>>> arr = np.loadtxt('\\home\Desktop\mypoints_data.txt', delimiter='\t', skiprows=1)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    arr = np.loadtxt('\\home\Desktop\mypoints_data.txt', delimiter='\t', skiprows=1)
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '\\home\\Desktop\\mypoints_data.txt'
>>> arr = np.loadtxt('\\home\roxana\Desktop\mypoints_data.txt', delimiter='\t', skiprows=1)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    arr = np.loadtxt('\\home\roxana\Desktop\mypoints_data.txt', delimiter='\t', skiprows=1)
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '\\home\roxana\\Desktop\\mypoints_data.txt'
>>> arr = np.loadtxt('\\home\roxana\\Desktop\mypoints_data.txt', delimiter='\t', skiprows=1)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    arr = np.loadtxt('\\home\roxana\\Desktop\mypoints_data.txt', delimiter='\t', skiprows=1)
  File "/usr/lib/python2.7/dist-packages/numpy/lib/npyio.py", line 803, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: '\\home\roxana\\Desktop\\mypoints_data.txt'
>>> arr = np.loadtxt('//home//roxana//Desktop//mypoints_data.txt', delimiter='\t', skiprows=1)
>>> arr
array([[ 45.588181,  25.43351 ],
       [ 46.031064,  26.240716],
       [ 46.021454,  26.279365],
       [ 45.87556 ,  26.13671 ],
       [ 45.86835 ,  26.069261],
       [ 46.20929 ,  26.074031],
       [ 46.022898,  26.229338],
       [ 46.025487,  26.22793 ],
       [ 46.21483 ,  26.07377 ],
       [ 46.21078 ,  26.07313 ],
       [ 46.211998,  26.07306 ],
       [ 46.21288 ,  26.07258 ],
       [ 46.214327,  26.073897],
       [ 45.87266 ,  26.120281],
       [ 45.87338 ,  26.126311],
       [ 45.87361 ,  26.12865 ],
       [ 46.021459,  26.280567],
       [ 46.02149 ,  26.2818  ],
       [ 46.021671,  26.283095],
       [ 46.021466,  26.283914],
       [ 45.707574,  25.50954 ],
       [ 45.706623,  25.50954 ],
       [ 45.706482,  25.506279],
       [ 45.600059,  25.436954],
       [ 45.598904,  25.437478],
       [ 45.597952,  25.437466],
       [ 45.596645,  25.437536],
       [ 45.595186,  25.437522],
       [ 45.732201,  25.8097  ],
       [ 45.730301,  25.80866 ],
       [ 45.7303  ,  25.808661]])
>>> 
========================================= RESTART: Shell =========================================
>>> import numpy as np
>>> import os
>>> arr = np.loadtxt('//home//roxana//Desktop//mypoints_data.txt', delimiter='\t', skiprows=1)
>>> arr
array([[ 45.588181,  25.43351 ],
       [ 46.031064,  26.240716],
       [ 46.021454,  26.279365],
       [ 45.87556 ,  26.13671 ],
       [ 45.86835 ,  26.069261],
       [ 46.20929 ,  26.074031],
       [ 46.022898,  26.229338],
       [ 46.025487,  26.22793 ],
       [ 46.21483 ,  26.07377 ],
       [ 46.21078 ,  26.07313 ],
       [ 46.211998,  26.07306 ],
       [ 46.21288 ,  26.07258 ],
       [ 46.214327,  26.073897],
       [ 45.87266 ,  26.120281],
       [ 45.87338 ,  26.126311],
       [ 45.87361 ,  26.12865 ],
       [ 46.021459,  26.280567],
       [ 46.02149 ,  26.2818  ],
       [ 46.021671,  26.283095],
       [ 46.021466,  26.283914],
       [ 45.707574,  25.50954 ],
       [ 45.706623,  25.50954 ],
       [ 45.706482,  25.506279],
       [ 45.600059,  25.436954],
       [ 45.598904,  25.437478],
       [ 45.597952,  25.437466],
       [ 45.596645,  25.437536],
       [ 45.595186,  25.437522],
       [ 45.732201,  25.8097  ],
       [ 45.730301,  25.80866 ],
       [ 45.7303  ,  25.808661]])
>>> 
