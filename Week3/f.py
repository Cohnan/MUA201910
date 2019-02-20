import sys
 
t = int(sys.stdin.readline())

for i in range(t):
    n, c = map(int, sys.stdin.readline().split())
    sumAs = sum(map(int, sys.stdin.readline().split()))
    if (sumAs <= c):
         print("Yes")
    else:
        print("No")
    