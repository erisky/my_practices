import math
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for i in xrange(1, total + 1):
    N = int(raw_input())

    output = {}
    for j in range(2*N-1):
        S = raw_input().split()
        for x in S:
            if x in output:
                output[x] = output[x] + 1
            else:
                output[x] = 1

    olist = []
    for any in output:
        if output[any] % 2 == 1:
            olist.append(int(any))

    olist.sort()
    # print olist
    os=""
    for gg in olist:
        os += str(gg)
        os += " "


    print "Case #{}: {}".format(i, "".join(os))
    # check out .format's specification for more formatting options
