import math
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for numcases in xrange(1, total + 1):
    S = list(raw_input())
    alldict = {}
    for x in S:
        if x in alldict:
            alldict[x] = alldict[x]+1
        else:
            alldict[x] = 1

    #strnum = ["ZERO",  "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    strnum = ["TWO", "SIX", "SEVEN", "FIVE", "FOUR", "EIGHT", "ZERO", "ONE", "NINE","THREE"]
    outdig = [2,6,7,5,4,8,0,1,9,3]
    output = []
    for i in range(len(strnum)):
        tempc = list(strnum[i])
        tempdic = alldict.copy()
        gonext = 0
        thiscount = 0
        while gonext == 0:
            for ch in tempc:
                if ch in tempdic and tempdic[ch] > 0:
                    tempdic[ch] -= 1
                else:
                    gonext = 1
            if (gonext == 0):
                thiscount += 1
        # print "thscount {} for {}".format(thiscount, i)
        if thiscount > 0:
            for ch in tempc:
                alldict[ch] -= thiscount
            for j in range(thiscount):
                output.append(str(outdig[i]))
    #print(alldict)
    for anyy in alldict:
        if alldict[anyy] != 0:
            print(alldict)
    output.sort()
    print "Case #{}: {}".format(numcases, "".join(output))
    # check out .format's specification for more formatting options
