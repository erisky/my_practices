#!/usr/bin/env python


#functions 


def maker(N):
    def action(X):
        return X**N
    return action


f = maker(2)
g = maker(3)

print f(4)
print g(4)




def remove_tail(x):
    if (len(x) > 1):
        x.pop(len(x)-1)
    return []


l1 = [1,2,3,4]

remove_tail(l1)
print l1
remove_tail(l1)
print l1

# pass an copy
remove_tail(l1[:])
print l1

