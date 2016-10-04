Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # numpy.where function is the vectorized version of the expression x if condition else y.
>>> 
>>> import numpy as np
>>> xarr=np.arange(1.1, 1.5, 0.1)
>>> xarr
array([ 1.1,  1.2,  1.3,  1.4])
>>> xarr= np.arange(1.1, 1.6, 0.1)
>>> xarr
array([ 1.1,  1.2,  1.3,  1.4,  1.5])
>>> yarr = np.arange(2.1, 2.6)
>>> yarr
array([ 2.1])
>>> yarr = np.arange(2.1, 2.6, 0.1)
>>> yarr
array([ 2.1,  2.2,  2.3,  2.4,  2.5])
>>> cond = np.array([True, False, True, True, False])
>>> # take a value from xarr whenever the corresp. value in cond is True otherwise take the value from yarr.
>>> # with a loop:
>>> result = [(x if c else y)
	  for x,y,c, in zip(xarr, yarr, cond)}
SyntaxError: invalid syntax
>>> result = [(x if c else y)
	  for x,y,c, in zip(xarr, yarr, cond)]
>>> result
[1.1000000000000001, 2.2000000000000002, 1.3000000000000003, 1.4000000000000004, 2.5000000000000004]
>>> # PROBLEM: the loop will not work with multidimensional arrays.
>>> 
>>> # with np.where():
>>> result = np.where(cond, xarr, yarr)
>>> result
array([ 1.1,  2.2,  1.3,  1.4,  2.5])
>>> # use it on matrices:
>>> arr= np.random.randn(4,4)
>>> arr
array([[ 1.10789117, -0.92626898,  1.18339276, -0.12078597],
       [ 0.56104043,  1.83370465,  0.59022002,  0.70175873],
       [ 0.4176934 , -1.28865029,  1.26792695,  0.47135416],
       [ 0.10298086,  1.5377928 , -0.13277433, -0.25627138]])
>>> np.where(arr>0, 2, -2)
array([[ 2, -2,  2, -2],
       [ 2,  2,  2,  2],
       [ 2, -2,  2,  2],
       [ 2,  2, -2, -2]])
>>> np.where(arr>0, 2, arr) # set only positive values to 2
array([[ 2.        , -0.92626898,  2.        , -0.12078597],
       [ 2.        ,  2.        ,  2.        ,  2.        ],
       [ 2.        , -1.28865029,  2.        ,  2.        ],
       [ 2.        ,  2.        , -0.13277433, -0.25627138]])
>>> 
>>> # you can use np.where to express more complicated logic:
>>> cond1=np.array([True, True, False, False])
>>> cond2=np.array([True, False, True, False])
>>> 
>>> # 1st way:
>>> result[]
SyntaxError: invalid syntax
>>> result =[] # create empty list
>>> for i in range (len(cond1)) :
	if cond1[i] and cond2[i] :
		result.append(0) # you put a 0 in the empty list at the index where the condition holds
	elif cond1[i] :
		result.append(1)
	elif cond2[i] :
		result.append(2)
	else :
		result.append(3)

		
>>> result
[0, 1, 2, 3]
>>> # once again this pattern: you first create an empty list, then you fill it in with append according to your conditions!!
>>> 
>>> 
>>> # 2nd way: use a nested np.where expression:
>>> 
>>> np.where(cond1 & cond2, 0,
	 np.where(cond1,1,
		  np.where(cond2, 2, 3)))
array([0, 1, 2, 3])
>>> 
>>> # 3rd way: uses the fact that boolean values are treated as 0 or 1
>>> result= 1*cond1 + 2*cond2 + 3*-(cond1|cond2)
>>> result
array([3, 1, 2, 3])
>>> result= 1*cond1 + 2*cond2 + 0*-(cond1|cond2)
>>> result
array([3, 1, 2, 0])
>>> result= 1*cond1 + 2*cond2 + 3*(cond1|cond2)
>>> result
array([6, 4, 5, 0])
>>> result= 1*cond1 + 2*cond2 + 0*(cond1 & cond2)
>>> result
array([3, 1, 2, 0])
>>> result= 1*cond1 + 2*cond2 + 0*(cond1 & cond2) + 3*(-cond1 & -cond2)
>>> result
array([3, 1, 2, 3])
>>> 
>>> result= 1*cond1 + 2*cond2 + 0*(cond1 | cond2) + 3*(-cond1 & -cond2)
>>> 
>>> result
array([3, 1, 2, 3])
>>> result= 1*cond1 + 2*cond2 + 0*(cond1 & cond2) + 3*(-cond1 & -cond2)
>>> result
array([3, 1, 2, 3])
>>> # ok, I can't see why it doesn't hold...
>>> result= 1*cond1 + 2*cond2 +  3*(-cond1 & -cond2) + 0*(cond1 & cond2)
>>> result
array([3, 1, 2, 3])
>>> result= 1*cond1 + 2*cond2 +  3*(-cond1 & -cond2) + 0*(cond1 | cond2)
>>> 
>>> result
array([3, 1, 2, 3])
>>> result= 1*cond1 + 2*cond2 +  3*(-cond1 & -cond2) + 0*(cond1 == cond2)
>>> result
array([3, 1, 2, 3])
>>> result= 1*cond1 + 2*cond2  + 0*(cond1 == cond2)
>>> result
array([3, 1, 2, 0])
>>> result
array([3, 1, 2, 0])
>>> result= 1*cond1 + 2*cond2  + 0*(cond1 == cond2) + 3*(-cond1=cond2)
SyntaxError: invalid syntax
>>> result= 1*cond1 + 2*cond2  + 0*(cond1 == cond2) + 3*(-cond1==cond2)
>>> result
array([3, 4, 5, 0])
>>> 
>>> # ok, I don't know exactly..
