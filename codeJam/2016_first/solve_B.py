
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for i in xrange(1, total + 1):
    N = raw_input()
    # print "Case #{0}: {1}".format(i, count_step(list(N), '+'))
    result = 0
    for index in range(len(list(N))-1):
        if N[index] != N[index+1]:
            result += 1

    if N[len(N)-1] == '-':
        result += 1

    print "Case #{0}: {1}".format(i, result)
