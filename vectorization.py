Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # VECTORIZATION - replacing explicit loops with array expressions.
>>> 
>>> import numpy as np
>>> points = np.arange(-5,5, 0.01)
>>> points[0:10]
array([-5.  , -4.99, -4.98, -4.97, -4.96, -4.95, -4.94, -4.93, -4.92, -4.91])
>>> xs, ys = np.meshgrid(points, points)
>>> xs[0:10]
array([[-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       ..., 
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99]])
>>> xs
array([[-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       ..., 
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99],
       [-5.  , -4.99, -4.98, ...,  4.97,  4.98,  4.99]])
>>> ys
array([[-5.  , -5.  , -5.  , ..., -5.  , -5.  , -5.  ],
       [-4.99, -4.99, -4.99, ..., -4.99, -4.99, -4.99],
       [-4.98, -4.98, -4.98, ..., -4.98, -4.98, -4.98],
       ..., 
       [ 4.97,  4.97,  4.97, ...,  4.97,  4.97,  4.97],
       [ 4.98,  4.98,  4.98, ...,  4.98,  4.98,  4.98],
       [ 4.99,  4.99,  4.99, ...,  4.99,  4.99,  4.99]])
>>> len(xs)
1000
>>> len(ys)
1000
>>> # the np.meshgrid function takes two 1D arrays and produces two 2D matrices corresponding to all pairs of (x,y) in the two arrays.
>>> 
>>> # now evaluate the function sqrt(x^2 + y^2) across this regular grid of values:
>>> import matplotlib.pyplot as plt
>>> z= np.sqrt(xs**2 + ys**2)
>>> z
array([[ 7.07106781,  7.06400028,  7.05693985, ...,  7.04988652,
         7.05693985,  7.06400028],
       [ 7.06400028,  7.05692568,  7.04985815, ...,  7.04279774,
         7.04985815,  7.05692568],
       [ 7.05693985,  7.04985815,  7.04278354, ...,  7.03571603,
         7.04278354,  7.04985815],
       ..., 
       [ 7.04988652,  7.04279774,  7.03571603, ...,  7.0286414 ,
         7.03571603,  7.04279774],
       [ 7.05693985,  7.04985815,  7.04278354, ...,  7.03571603,
         7.04278354,  7.04985815],
       [ 7.06400028,  7.05692568,  7.04985815, ...,  7.04279774,
         7.04985815,  7.05692568]])
>>> plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
<matplotlib.image.AxesImage object at 0x7f0d1149a9d0>
<matplotlib.colorbar.Colorbar object at 0x7f0d114262d0>
>>> plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
<matplotlib.text.Text object at 0x7f0d114ee310>
>>> # ok, the problem is I can't come to really see it yet.
>>> 
>>> # from Wes McKinney (2013)
>>> 
