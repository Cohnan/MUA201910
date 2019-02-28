from sys import stdin as inp

t = int(inp.readline())

for i in range(t):
    n, th = map(int, inp.readline().split())
    A = list(map(int, inp.readline().split()))
    A.sort()
    M = -1
    mainsum = 0
    for i in range(n-1, 0, -1):
        mainsum += A[i]
        psum = mainsum - A[i-1]*(n-i)
        if (psum >= th):
            M = A[i-1]
            break

    if M == -1: # Si agregara 0 al inicio, me ahorraria esto
        mainsum += A[0]
        psum = mainsum
        M = 0
        i = 0

    while (psum >= th):
        M += 1
        psum = mainsum - (n-i)*M
    
    M -= 1
    S = mainsum - M*(n-i)
    print(str(M) + " " + str(S))
