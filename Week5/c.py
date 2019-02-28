from sys import stdin as inp

n = int(inp.readline())
m = int(inp.readline())
a = [0]*n

for i in range(n):
    a[i] = int(inp.readline())

a.sort()
A = a[-1]
kmax = A + m

for i in range(n-2, -1, -1):
    while (a[i] < A and m > 0):
        a[i] += 1
        m -= 1
    if (m <= 0):
        kmin = A

if m > 0:
    kmin = A + m//n + (m%n > 0)

print(str(kmin) + " " + str(kmax))