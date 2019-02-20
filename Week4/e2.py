from sys import stdin as inp

def res(a,b, i, j):
    return sum(a[i][k]*b[k][j] for k in range(n)) / (j-i+1.)

def matmult2(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

n = int(inp.readline())
lista = map(int, inp.readline().split())

R = [[lista[j]*(j >= i) for j in range(n)] for i in range(n)]
M = [[(j >= i) for j in range(n)] for i in range(n)]

#A = [[matmult(R, M, i, j) for j in range(n)] for i in range(n)]
#print(A)
#print(matmult2(R, M))

#for i in range(n):
#    for j in range(i, n):
#        A[i][j] = A[i][j]/(j-i+1.)

l = n
found = False
while(l >= 1 and not found):
    for i in range(n+1-l):
        j = l-1+i
        if res(R, M, i, j) > 100:
            found = True
            print(l)
            break   
    l -= 1
if (not found):
    print(0)