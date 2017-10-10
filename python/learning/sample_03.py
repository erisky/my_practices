#!/usr/bin/env python

import sys
#tmp = sys.stdout
#sys.stdout = open('output.txt', 'a')


# variable number of arguments 

def min1(*args):
    res = args[0]
    for val in args[1:]:
        if (res > val):
            res = val
    return res


print min1(1,2,3,4,5)
print min1('a', 'b')
print min1('12321', '1efwef')



#lambda -- easier format of function
#ex
f = (lambda x=1,y=2,z=3: (x+y) *z)

print f(3,4)
print f(1,3,3)


mydict =  {'a':1, 'b':2}

print mydict['a']

mydict2 =  {'a':(lambda x,y: x+y), 'b':(lambda x,y: x *y)}

print mydict['a']
print mydict2['a'](12,23)
print mydict2['b'](12,23)


# apply function, something useful when make use of function pointer of C

def funct1(x,y,z):
    return x+y+z

f = funct1

print "apply:%d" % apply(f, (3,5,6))


# map function 

mylist1 = [1,2,3,4]

def sqrx(x):
    return x*x

print "list before map",
print mylist1
mylist1 = map(sqrx, mylist1)
print " after map:",
print mylist1

print " !!!!!!!!!!!!!!!!! "
print " MUST re-read bottom half of chapter 17" 
print "Done" 
