from sys import stdin as inp

t = int(inp.readline())

for i in range(t):
    n = int(inp.readline())
    s = [a for a in inp.readline() if (a == '1')]
    l = len(s)
    print(l*(l+1)//2)