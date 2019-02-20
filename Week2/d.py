import math

primos = [2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41, 43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
def firstD(k):
    for i in range(len(primos)):
        if (k % primos[i] == 0):
            return primos[i]

#t = int(input())
t = input()
results = ['' for i in range(t)]

for i in range (t):
    #n = int(input())
    n = input()
    ###3#rawlist = [13, 2, 8, 6, 3, 14, 9]#rawlist = [1, 5, 9, 2, 6, 8, 3]#rawlist = [13, 2, 8, 6, 3, 14, 9]#rawlist = raw_input().split()
    rawlist = raw_input().split()
    lista = [( int(rawlist[j]), firstD(int(rawlist[j])), j ) for j in range(len(rawlist))]
    #####print(lista)
    listalog = [( int(math.log(lista[j][0], 2)), lista[j][1], lista[j][2] ) for j in range(len(lista))]
    listalog.sort(key = lambda x: (x[0], x[1]), reverse = True) # parece que si conserva el orden de insercion de aquellos que tienen el mismo valon
    ######print(listalog)
    result = [rawlist[a[2]] for a in listalog]
    #results[i] = " ".join(x for x in result)
    print(result)
    for a in result:
        results[i]+= a + ' '

for s in results:
    print(s[:-1])