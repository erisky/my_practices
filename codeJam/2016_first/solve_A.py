import math
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for i in xrange(1, total + 1):
    N = int(raw_input())
    if N == 0:
        print "Case #{0}: {1} ".format(i,'INSOMNIA')
        continue

    rst1 = [0 for x in range(10)]
    time = 1
    while True:
        temp = N*time
        while (temp > 0):
            rst1[temp%10] = 1
            temp /= 10
        if all(item == 1 for item in rst1):
            print "Case #{0}: {1} ".format(i, N*time)
            break
        time += 1


    # print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
