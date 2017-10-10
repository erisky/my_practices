#!/usr/bin/env python



class c1:
    def __init__(self, name='noset'):
        self.name = name
    def setname(self, who):
        self.name = who


I1 = c1('eric')
I2 = c1('joe')
I3 = c1()
print I1.name 
print I2.name

I1.setname("newbane")
print I1.name
print I3.name


class c2(c1):
    def setold(self, old):
        self.yearsold = old

    def test(self,gg):
        self.testatt = gg
    ggy = 'shit'
    data = 1
#   operator overload !?
    def __add__(self, value):
        return self.data + value

I4 = c2()
I4.setold(23)
print "name:%s old:%d" % (I4.name, I4.yearsold)
I4.test(123)
print I4.testatt
print I4.ggy


b = I4 + 4
print b
