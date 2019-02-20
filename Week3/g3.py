#
# 
from sys import stdin as inp

s = list(inp.readline()[:-1])
s.reverse()

ns = len(s)
currentns = ns
si = [(s[i], i) for i in range(ns)]
t = []
nt = 0
u = []
nu = 0

ordered = sorted(si, key = lambda x: (x[0], -x[1]))
j = 0

while(True):
    while (ordered[j][1] >= currentns):
        j += 1

    while (nt > 0 and ordered[j][0] >= t[-1]):
        u.append(t.pop())
        nu += 1
        nt -= 1
    
    nToT = (currentns-1) - ordered[j][1]
    for i in range(nToT):
        t.append(s.pop())
    u.append(s.pop())
    currentns = currentns - (nToT+1)
    nt += nToT
    nu += 1

    if(currentns == 0):
        while (nt > 0):
            u.append(t.pop()) 
            nt -= 1 # nu += 1
        print("".join(u))
        break
