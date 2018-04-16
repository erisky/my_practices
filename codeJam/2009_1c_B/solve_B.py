import math
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for i in xrange(1, total + 1):
    n = int(raw_input())
    # print "#?{}".format(n)
    x = 0
    y = 0
    z = 0
    vx = 0
    vy = 0
    vz = 0
    for j in xrange(1, n+1):
        listitems = [float(s) for s in raw_input().split(" ")]
        x += listitems[0]/n
        y += listitems[1]/n
        z += listitems[2]/n
        vx += listitems[3]/n
        vy += listitems[4]/n
        vz += listitems[5]/n
    # print "{},{},{},{},{},{}".format(x,y,z,vx,vy,vz)
    # f(t) = At^2 + Bt + C
    # A = vx^2+ vy^2 + vz^2
    # B = 2(x*xv + y*vy + z*vz)
    # C = x^2+y^2+z^2
    # for f(t) min, --> t = -b/2a
    A = vx * vx + vy*vy + vz*vz
    B = 2*(x*vx + y*vy + z*vz)
    C = x*x + y*y + z*z
    # print("A {} B {}").format(A,B)
    if A < 0.0000001 or (vx*vx+vy*vy+vz*vz) < 0.000001:
        tt = 0
        dt = math.sqrt(x*x + y*y + z*z)
    else:
        tt = - ((B)/ (2*A))
        if tt < 0:
            tt = 0
        temp = A*tt*tt+ B*tt+ C
        if temp > 0:
          dt = math.sqrt(temp)
        else:
          dt = 0

    print "Case #{0}: {1:.8f} {2:.8f} ".format(i, dt, tt)
    # print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
