# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for Ti in xrange(1, T + 1):
    N = int(raw_input())
    tmp = raw_input().split()
    # print tmp
    a=[]
    b=[] 
    p={}
    for i in range (0,5000+1):
        p[i]=0
    for ni in range(N):
        # print ni
        a.append(int(tmp[ni*2]))
        b.append(int(tmp[ni*2+1]))
        # print a,b
        # now sum for each P
        for x in range(a[ni], b[ni]+1):
            p[x] = p[x]+1
    
    P = int(raw_input()) 

    print "Case #{}:".format(Ti),
    for pi in range(P):
        ci = int(raw_input())
        print str(p[ci])+ ' ',

    print ""
    # read empty line ,sucks
    if Ti < T:
        eline = raw_input()


