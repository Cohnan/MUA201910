from sys import stdin as inp

n = int(inp.readline())
w = int(inp.readline())
toffs = map(lambda x: 1-1/float(x), inp.readline().split())
lands = map(lambda x: 1-1/float(x), inp.readline().split())

c1 = reduce(lambda x, y: x*y, toffs)
c2 = reduce(lambda x, y: x*y, lands)

C = c1*c2

if C > 1 or C <= 0:
    print(-1)
else:
    print(format(w*(1-C)/C, '.10f'))