from sys import stdin as inp

t = int(inp.readline())

while (t > 0):
    t-=1
    n, k = map(int, inp.readline().split())
    ws = list(map(int, inp.readline().split()))
    ws.sort()
    minsize = min(k, n-k)
    
    lessW = 0
    for i in range(minsize):
        lessW += ws[i]

    biggerW = 0
    for i in range(minsize, n):
        biggerW += ws[i]

    print(biggerW - lessW)