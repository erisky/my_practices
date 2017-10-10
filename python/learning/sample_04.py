#!/usr/bin/env python

print "------ starting OOP -------" 

import sys

#from
#reload

import module1

module1.printer("test module")


from module1 import printer

printer("Using from", 123 )

