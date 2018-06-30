def neg(v):
    if v == 1:
        return 0
    elif v == 0:
        return 1
    else:
        return "ERROR"


def recursive_solve(N):
    # print '->', N
    base = [0,0,0,1,0,0,1,1]
    if N <=7:
        return base[N]
    else:
        # find K so tha 2^K > N
        K2 = 8

        while K2 < N:
            K2=K2*2
            if N==K2:
                return 0
        if N == K2:
            return 0

        return neg(recursive_solve(K2-N))
        
#for x in range(1, 100):
#    print x,
#    print recursive_solve(x)

#print recursive_solve(2)
#print recursive_solve(3)
#print recursive_solve(10)
#print recursive_solve(11)
#print recursive_solve(15)
#print recursive_solve(17)
#print recursive_solve(16)
#print recursive_solve(31)
#print recursive_solve(100)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for Ti in xrange(1, T + 1):
    N = int(raw_input())
#    print "!!!" + str(N)
    print "Case #{}: {}".format(Ti,recursive_solve(N))

