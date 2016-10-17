Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # NumPy is able to save and load data to and from disk either in text or in binary format.
>>> 
>>> # 1) Storing arrays on disk in binary format
>>> import numpy as np
>>> arr= np.arange(10)
>>> arr
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.save('some_array', arr)
>>> 
>>> # arrays are saved in an uncompressed raw binary format with file extension .npy
>>> # arrays can be loaded using np.load
>>> 
>>> np.load('some_array.npy')
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> 
KeyboardInterrupt
>>> # you can save multiple arrays in a zip archive using np.savez and passing the arrays as arguments
>>> np.savez('array_archive.npz', a=arr, b=arr)
>>> arch= np.load('array_archive.npz')
>>> arch
<numpy.lib.npyio.NpzFile object at 0x7f7035a6ac10>
>>> np.load('array_archive.npz')
<numpy.lib.npyio.NpzFile object at 0x7f7035a6ae90>
>>> arch['b']
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> arch['a']
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> # you access the arrays within the archives using indexing
>>> 
