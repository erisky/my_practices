import math


gt = {7:[1],8:[2],6:[8],3:[9,10],9:[5,7], 10:[3,4]}
N = 10
def maxcircle(root, exclusion):
    # print len(exclusion)
    print root
    print exclusion
    if root in gt:
        ret = [1]
        for n in gt[root]:
            if n in exclusion:
                continue
            else:
                exclusion.append(root)
                v = 1 + maxcircle(n,exclusion)
                exclusion.remove(root)
                ret.append(v)
        if 1 == max(ret):
            for any in range(N+1):
                if any in exclusion:
                    continue
            else:
                if any in gt and root in gt[any]:
                    return 2
            return 1
        else:
            return max(ret)
    else:
        for any in range(N+1):
            if any in exclusion:
                continue
            else:
                if any in gt and root in gt[any]:
                    return 2
        return 1

for i in range(10):
    print "{}=?> {}".format(i+1, maxcircle(i+1,[]))

'''
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

'''