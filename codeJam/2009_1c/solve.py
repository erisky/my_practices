import fileinput
import os


def input_getter():
    filelist = os.listdir(".")

    inputDict = {}
    inputDict['small'] = []
    inputDict['large'] = []

    for filename in filelist:
        if filename.rfind(".in") == -1:
            continue
        first = 0
        for lines in fileinput.input(filename):
            if first == 0:
                first = int(lines)
                continue
            if filename.rfind("small") != -1:
                inputDict['small'].append(lines.strip('\n'))
            else:
                inputDict['large'].append(lines.strip('\n'))
            # print("{0}".format(lines))
            # print ("%s" % lines)
    # print(len(inputDict['small']))
    # print(inputDict['small'])
    # print(len(inputDict['large']))
    # print(inputDict['large'])

    return inputDict




def my_solve(inputstr):
    # 1st should be the index 1
    # 2nd appear is 0
    numdict = {}
    index = 2
    for c in inputstr:
        if len(numdict) == 0:
            numdict[c] = 1
        elif numdict.has_key(c):
            pass
        elif len(numdict) == 1:
            numdict[c] = 0
        else :
            numdict[c] = index
            index+=1

    # print(numdict)
    base = len(numdict)
    strlen = len(inputstr)
    result = 0
#    if base == 1 and strlen == 1:
#        numdict[inputstr[0]] = 0
    if base == 1:
        numdict['any'] = 0
        base += 1

    for c in inputstr:
        result += numdict[c] * (base ** (strlen-1))
        strlen -= 1
        # print(result)
    return result


#my_solve('11001001')
#my_solve('cats')
#my_solve('zig')


inputDict = input_getter()

index = 0
for strtest in inputDict['large']:
    index += 1
    print("Case #%d: %d" % (index, my_solve(strtest)))