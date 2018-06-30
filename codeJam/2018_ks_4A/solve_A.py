# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for Ti in xrange(1, T + 1):
    tmp = raw_input().split()
    F = int(tmp[0])
    L = int(tmp[1])

    print F, L
    r = 0
    for i in xrange (F, L+1):
        if (i % 9) == 0:
            continue
        if '9' in str(i):
            continue
        # print i
        r=r+1


    print "Case #{}:".format(Ti), r 


