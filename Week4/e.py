from sys import stdin as inp

def checkDDOS(sec, l):
    pm = max(0, sec-(l-1) - 1)
    pM = min(n, sec+l-1) - (l-1)
    for i in range(pm, pM):
        if (sp[i+l] - sp[i]) > 100*l: #good
            return True
    return False

n = int(inp.readline())
lista = map(int, inp.readline().split())
sp = [0]*(n+1)
DDOS = []
for i in range(len(lista)):
    if (lista[i] > 100):
        DDOS.append(i+1)
    sp[i+1] = sum(lista[0:i+1])

ds = len(DDOS)
if ds > 0:
    found = False
    check = [False]*ds
    l = n
    while(not found and (1 <= l and l <= n)):
        for dt in DDOS:
            if checkDDOS(dt, l):
                found = True
                print(l)
                break
        l -= 1

else:
    print(0)



# en 1 seg i                        sp[i] - sp[i-1]
# en 2 seg i, i+1:                  sp[i+1] - sp[i-1]
# en l seg i, ..., i+l-1:           sp[i+l-1] - sp[i-1]
# en l seg i-(l-1), ..., i:         sp[i] - sp[i-(l-1) - 1]