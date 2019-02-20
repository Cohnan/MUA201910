from sys import stdin as inp

t = int(inp.readline())

while (t > 0):
    t-=1
    n, k = map(int, inp.readline().split())
    ans = ''
    for i in range(k):
        ans += chr(97 + i)*(n/k)
    ans += 'a'*(n%k)
    print(ans)