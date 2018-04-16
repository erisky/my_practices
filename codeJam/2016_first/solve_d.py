
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for i in xrange(1, total + 1):
    strIn = raw_input()
    K = int(strIn.split()[0])
    C = int(strIn.split()[1])
    S = int(strIn.split()[2])

    # decide the position of LLLGLLL (single G
    steps = K
    pos = [p+1 for p in range(K)]

    iter = 1
    while iter < C:
        steps -= 1
        for pi in range(len(pos)):
            p = pos[pi]
            p = p +


    print "Case #{0}: {1} {2} {3} ".format(i, K,C,S)
