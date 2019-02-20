from sys import stdin as inp

n = int(inp.readline())

arr = list(map(int, inp.readline().split()))
arr.sort()

dn = arr[n-1] - arr[n-2]
d0 = arr[1] - arr[0]
if (dn > d0):
    print(arr[n-2]- arr[0])
else:
    print(arr[n-1] - arr[1])