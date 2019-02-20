from sys import stdin as inp
from math import ceil

t = int(inp.readline())

while (t > 0):
    t -= 1
    n, x, y, d = map(int, inp.readline().split())

    if (x - y) % d == 0:
        print((abs(x-y) // d))
    else:
        yfromn = -1
        yfrom1 = -1
        if (n - y) % d == 0:
            yfromn = (n-y)//d
        if (y - 1) % d == 0:
            yfrom1 = (y-1)//d
        
        if (yfromn == -1 and yfrom1 == -1):
            print(-1)
        else:
            xfromn = int(ceil(1.*(n-x)/d))
            xfrom1 = int(ceil(1.*(x-1)/d))
            
            Tfromn = xfromn + yfromn
            Tfrom1 = xfrom1 + yfrom1

            if (yfromn >= 0 and yfrom1 >= 0):
                print(min(Tfromn, Tfrom1))
            elif (yfromn >= 0):
                print(Tfromn)
            else:
                print(Tfrom1)