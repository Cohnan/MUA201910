from sys import stdin as inp

s = list(inp.readline()[:-1])
s.reverse()
ns = len(s)
t = ['']
nt = 0
u = []

ordered = sorted(s)
j = 0

while(True):
    while((ordered[j] not in s) and (ordered[j] < t[-1])):
        j += 1
        if (j == ns): # s has to be empty now
            while(nt > 0):
                u.append(t.pop())
                nt -= 1
            print("".join(u))
            exit()
    if (ordered[j] >= t[-1]):
        u.append(t.pop())
        nt -= 1
        j -= 1
    else:
        while(s[-1] != ordered[j]):
            t.append(s.pop())
            nt += 1
        u.append(s.pop())
    if (nu == ns):
        print("".join(u))
        break
