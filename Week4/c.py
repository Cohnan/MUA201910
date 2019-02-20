from sys import stdin as inp
#aaaaaaaaaaa
n = int(inp.readline())
s = inp.readline()

found = False
if n > 1:
    for i in range(n-(2-1)):
        if s[i] != s[i+1]:
            found = True
            print("YES")
            print(s[i:i+2])
            break

if not found: print('NO')