import math








def flip_cake(cake):
    newcake = []
    for i in xrange(len(cake), 0, -1):
        if (cake[i-1] == '+'):
            newcake.append('-')
        else:
            newcake.append('+')
    return newcake

def count_step(cake, target):
    count = len(cake)
    print("Input:")
    print(cake)
    print(target)
    if count == 1:
        if cake[0] == target:
            return 0
        else:
            print(cake)
            print(1)
            return 1
    else:
        while count > 1 and cake[count-1] == target:
            count -= 1
        if count == 1:
            return count_step(cake[0:1], target)

        newcake = flip_cake(cake[0:count])
        # print(newcake)
        # step += 1
        if newcake[count-1] == target:
            print(11)
            return count_step(newcake[0:count-1], '+') + 1
        else:
            print(22)
            return count_step(newcake[0:count], '-') + 1


# test

c1 = ['-', '-', '+', '-']
print(count_step(c1, '+'))

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
