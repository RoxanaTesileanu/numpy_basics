Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import Gnuplot
>>> plot besj0(x)
SyntaxError: invalid syntax
>>> plot besj 0 (x)
SyntaxError: invalid syntax
>>> plot sin(x)
SyntaxError: invalid syntax
>>> plot sin(x)
SyntaxError: invalid syntax
>>> import numpy as np
>>> g = Gnuplot.Gnuplot()
>>> g.title('my first gnuplot')
>>> g.xlabel('x')
>>> g.ylabel('sin(1/x)')
>>> g('set term pngcairo')
>>> g('set out "GnuplotFromPython.png"')
>>> g('plot sin(1/x)')
>>> g('set term wx0')
>>> g('set term png')
>>> g('set out "GnuplotFromPython.png"')
>>> 
========================================= RESTART: Shell =========================================
>>> import numpy as np
>>> import Gnuplot
>>> g.title('my first gnuplot')

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    g.title('my first gnuplot')
NameError: name 'g' is not defined
>>> g = Gnuplot.Gnuplot()
>>> g.title('my first gnuplot')
>>> g('set term pngcairo')
>>> g('set out "GnuplotFromPython.png"')
>>> g('plot sin(1/x)')
>>> g('set out "GnuplotFromPython.png"')
>>> g.title('my first gnuplot')
>>> g.xlabel('x')
>>> g.ylabel('sin(1/x)')
>>> g('set term pngcairo')
>>> g('set out "GnuplotFromPython.png"')
>>> g('plot sin(1/x)')
>>> 
