Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import Gnuplot
>>> g.Gnuplot.Gnuplot()

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    g.Gnuplot.Gnuplot()
NameError: name 'g' is not defined
>>> g= Gnuplot.Gnuplot()
>>> # we now can issue commands directly to gnuplot just by passing strings to g.
>>> # also the package has abstracted gnuplot commands like g.title.
>>> g.title ('Normally Distributed Random Data')
>>> g.xlabel('x')
>>> g.ylabel('y')
>>> g('set term pngcairo')
>>> g('set out "Normal_Distrib.png"')
>>> # you can then use numpy to pass an array to x:
>>> x = arange(1,1000)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = arange(1,1000)
NameError: name 'arange' is not defined
>>> x = arange (1, 1000)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x = arange (1, 1000)
NameError: name 'arange' is not defined
>>> x = np.arange(1, 1000)
>>> # you can use numpy to compute the y values corr. to the x values:
>>> y = [np.random.normal() for i in x]
>>> g.plot(Gnuplot.Data(x,y)
       )
>>> 
