#!/usr/bin/env python


import dir1.dir2.mod1




print dir1.dir2.mod1.x


# dir1 already acts like an object
print " reloading dir1" 
reload(dir1)


#from dir1.dir2 import mod
from dir1.dir2 import *
#from *

print "using from"
print mod1.x
print mod1._test
