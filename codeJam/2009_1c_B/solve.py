import fileinput
import os
import math

class firefly():
    def __init__(self, inputline):
        listeach = inputline.split(' ')
        self.x = float(listeach[0])
        self.y = float(listeach[1])
        self.z = float(listeach[2])
        self.xv = float(listeach[3])
        self.yv = float(listeach[4])
        self.zv = float(listeach[5])

    def display(self):
        #print("(%d, %d, %d) v(%d, %d, %d)" % self.x, self.y, self.z, self.xv, self.yv, self.zv)
        print 'pos:({0},{1},{2})'.format(str(self.x), str(self.y), str(self.z))
        print 'v:({0:.6f},{1},{2})'.format(self.x, str(self.y), str(self.z))


# g[2].display()


def caldst(ix,iy,iz,mx,my,mz,t):
    # print '{0}, {1}, {2}'.format(mx,my,mz)
    px = ix + (t*mx)
    py = iy + (t*my)
    pz = iz + (t*mz)
    # print '{0}, {1}, {2}'.format(px,py,pz)
    dst = math.sqrt((px*px) + (py*py) + (pz*pz))
    return dst

def solve(listflies):
    delta_x = 0
    delta_y = 0
    delta_z = 0
    init_x = 0
    init_y = 0
    init_z = 0

    for fly in listflies:
        init_x += fly.x
        init_y += fly.y
        init_z += fly.z
        delta_x += fly.xv
        delta_y += fly.yv
        delta_z += fly.zv
        # print '>> {xv} {yv} {zv}'.format(xv=fly.xv, yv=fly.yv, zv=fly.zv)
    move_x = float(delta_x)/len(listflies)
    move_y = float(delta_y)/len(listflies)
    move_z = float(delta_z)/len(listflies)
    init_x = float(init_x)/len(listflies)
    init_y = float(init_y)/len(listflies)
    init_z = float(init_z)/len(listflies)

    #print 'v:({0:.8f},{1:.8f},{2:.8f})'.format(move_x,move_y,move_z)
    #print 'pos:({0:.8f},{1:.8f},{2:.8f})'.format(init_x,init_y,init_z)

#    print 'v:({0:.6f},{1},{2})'.format(self.x, str(self.y), str(self.z))
    #dmin =
    # for i in range(1,3):
    #    print "d({ii}):{0:.8f}".format(caldst(init_x,init_y,init_z,move_x, move_y,move_z, i), ii=i)


    dmin = caldst(init_x,init_y,init_z,move_x, move_y,move_z, 0)
    tmin = 0

    t = 1
    while 1:
        dnew = caldst(init_x,init_y,init_z,move_x, move_y,move_z, t)
        if dnew < dmin:
            dmin = dnew
            tmin = t
        t += 1
        if t > (tmin +3):
            break
    print '{0:.8f} {1:.8f}'.format(dmin, tmin)



# B-small-practice.in
g = []
g.append(firefly('3 0 -4 0 0 3'))
g.append(firefly('-3 -2 -1 3 0 0'))
g.append(firefly('-3 -1 2 0 3 0'))

T = 0
N = 0
listsolve = []
casen = 0
for lines in fileinput.input('B-small-practice.in'):
    # print(lines)
    if T == 0:
        T = int(lines)
        print(T)
        continue
    elif N == 0:
        N = int(lines)
        casen += 1
        # print(N)
        listsolve = []
        continue
    elif N >= 1:
        a = firefly(lines)
        listsolve.append(a)
        N -= 1
        # print 'N={0}'.format(N)
        if N == 0:
            print "Case #{0}: ".format(casen),
            solve(listsolve)
# solve(g)

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


# inputDict = input_getter()

# index = 0
# for strtest in inputDict['large']:
#    index += 1
#    print("Case #%d: %d" % (index, my_solve(strtest)))