from sys import stdin as inp

n = int(inp.readline())
lista = map(int, inp.readline().split())
sp = [0]*(n+1)
for i in range(len(lista)):
    sp[i+1] = sum(lista[0:i+1])
print(sp)

found = False
for l in range(n, 0, -1):
    if found: break
    for i in range(n-l+1):
        print(sp[i+l] - sp[i])
        if (sp[i+l-1] - sp[i])/100 > l:
            print("Yay", i)
            found = True

# en seg i sp[i] - sp[i-1]