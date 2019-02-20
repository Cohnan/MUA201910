#import sys
#encr = list(sys.argv[1])
encr = list(raw_input())
if len(encr) %2 != 0:
    encr.append("")
n = len(encr)
ans = [None]*n

for i in range(0, n//2):
    ans[n-2 - 2*i] = encr[i]

for i in range(n//2, n):
    ans[2*i + 1 - n] = encr[i]

print(''.join(ans))