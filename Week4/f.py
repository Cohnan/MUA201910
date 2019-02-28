from sys import stdin as inp

primos5 = [2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41, 43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]

def primedec(n, currpd):
    res = []
    mult = 1
    #totaldiv = 1
    for p in primos5:
        if mult == n or p > n**0.5: break
        N = n
        ex = 0
        while (N % p == 0):
            ex += 1
            N /= p
            mult *= p
        if (ex != 0):
            res.append([p, ex])
        
        if n/p in primos5:
            N = n
            q = n/p
            ex = 0
            while (N % q == 0):
                ex += 1
                N /= q
                mult *= q
            if (ex != 0):
                res.append([q, ex])
            #totaldiv *= (ex + 1)
    return res

def divs(n, pdec):
    res = [1]
    for i in range(len(pdec)):
        p = pdec[i][0]
        ex = pdec[i][1]
        clen = len(res)
        for j in range(clen):
            for e in range(1, ex+1):
                res.append(res[j]*(p**e))
    return res

print(divs(28, primedec(28)))

t = int(inp.readline())

xs = [0]*t

for i in range(t):
    xs[i], yi = map(int, inp.readline().split())
    ares = divs(xs[i], primedec(xs[i]))

    for j in range(i - yi, i):
        indtorem = []
        for k in range(len(ares)):
            d = ares[k]
            if xs[j] % d== 0:
                indtorem.append(k)
        ares = [ares[k] for k in range(len(ares)) if k not in indtorem]
    print(len(ares))