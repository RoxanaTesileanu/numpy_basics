Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # a universal function is a function that performs elementwise operations on data in ndarrays.
>>> # many ufuncs are simple elementwise transformations, like sqrt or exp.
>>> 
>>> import numpy as np
>>> arr= np.arange(10)
>>> np.sqrt(arr)
array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ,
        2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ])
>>> np.exp(arr)
array([  1.00000000e+00,   2.71828183e+00,   7.38905610e+00,
         2.00855369e+01,   5.45981500e+01,   1.48413159e+02,
         4.03428793e+02,   1.09663316e+03,   2.98095799e+03,
         8.10308393e+03])
>>> # ufuncs taht take one array are called UNUARY ufuncs
>>> # ufuncs that take 2 arrays and return a single array are called BINARY ufuncs
>>> 
>>> x=np.randn(8)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x=np.randn(8)
AttributeError: 'module' object has no attribute 'randn'
>>> x=np.random.randn(8)
>>> x
array([ 1.0812581 , -0.70572238,  0.74311548,  0.81678334, -1.6225645 ,
       -0.36390965, -0.52153012, -1.60637377])
>>> y= np.random.randn(8)
>>> y
array([-0.82363435,  0.74062992,  2.20531089, -0.62077794, -0.94520856,
       -0.72337818, -0.6452626 ,  1.60378576])
>>> np.maximum(x,y) # element-wise maximum
array([ 1.0812581 ,  0.74062992,  2.20531089,  0.81678334, -0.94520856,
       -0.36390965, -0.52153012,  1.60378576])
>>> arr=np.random.randn(7)*5
>>> arr
array([ -2.3966598 ,  10.30676797,  -2.64795659,   2.17147173,
         1.61174657,   2.00824242,   3.80721699])
>>> np.modf(arr)
(array([-0.3966598 ,  0.30676797, -0.64795659,  0.17147173,  0.61174657,
        0.00824242,  0.80721699]), array([ -2.,  10.,  -2.,   2.,   1.,   2.,   3.]))
>>> # while not common a ufunc can return multiple arrays, like e.g. modf function which returns the fractional and integral parts of a floating point array.
>>> 
>>> ceil(arr)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ceil(arr)
NameError: name 'ceil' is not defined
>>> np.ceil(arr)
array([ -2.,  11.,  -2.,   3.,   2.,   3.,   4.])
>>> np.floor(arr)
array([ -3.,  10.,  -3.,   2.,   1.,   2.,   3.])
>>> np.rint(arr)
array([ -2.,  10.,  -3.,   2.,   2.,   2.,   4.])
>>> np.logical_not(arr)
array([False, False, False, False, False, False, False], dtype=bool)
>>> -arr
array([  2.3966598 , -10.30676797,   2.64795659,  -2.17147173,
        -1.61174657,  -2.00824242,  -3.80721699])
>>> 
