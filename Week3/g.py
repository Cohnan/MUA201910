############################## I claim this works, but it is too slow\
# DO NOT MODIFY
from sys import stdin as inp

s = list(inp.readline()[:-1])
s.reverse()

ns = len(s)
currentns = ns
si = [(s[i], i) for i in range(ns)]
t = ['']
nt = 0
u = []
nu = 0

ordered = sorted(si, key = lambda x: (x[0], -x[1]))
j = 0


while(True):
    initj = j
    while((ordered[j][1] >= currentns) and (ordered[j][0] != t[-1])):
        j += 1
        if (j == ns): # s has to be empty now
            #print("Entro 1")
            while(nt > 0):
                u.append(t.pop())
                nt -= 1
                nu += 1
            print("".join(u))
            exit()
    if (ordered[j][0] == t[-1]):
        #print("Entro 2")
        u.append(t.pop())
        nt -= 1
        nu += 1
        j = initj
    else:
        #print("Entro 3")
        while(s[-1] != ordered[j][0]):
            t.append(s.pop())
            currentns -= 1
            nt += 1
        u.append(s.pop())
        currentns -= 1
        nu += 1
    if (nu == ns):
        print("".join(u))
        break