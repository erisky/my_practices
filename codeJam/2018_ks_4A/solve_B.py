# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for Ti in xrange(1, T + 1):
    tmp = raw_input().split()
    N = int(tmp[0])
    K = int(tmp[1])
    P = int(tmp[2])
    reslist = {}
#    print N,K,P
    for i in xrange(1, K+1):
        tmp = raw_input().split()
        Ai = int(tmp[0])
        Bi = int(tmp[1])
        Ci = int(tmp[2])
#        print Ai,Bi,Ci
        if Ai != Bi:
            print "Error"
        reslist[Ai] = str(Ci)        
    p_in_bin = bin(P-1)[:1:-1]
#3    print P
#3    print "ppp", p_in_bin
    pi = 0
    for j in xrange(N, 0, -1):
        if j in reslist.keys():
            continue
        else:
            if len (p_in_bin) > pi:
                if p_in_bin[pi] == '1':
                    reslist[j] = '1'
                else:
                    reslist[j] = '0'
                pi += 1
            else :
                reslist[j] = '0'

    res =""
    for j in xrange(1,N+1):
        res=res+reslist[j]
#    print  "result;", reslist, res
    print "Case #{}:".format(Ti), res


