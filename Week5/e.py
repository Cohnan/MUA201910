from sys import stdin as inp

def binPositions(p, n): #Camino para llegar a la posicion de x
    #p = array.index(x)
    res = []

    l = 0
    h = n - 1
    while (l <= h):
        m = (l + h)//2
        res.append(m)
        if m == p:
            break
        elif m < p:
            l = m + 1
        else:
            h = m - 1
    return res

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def rel(x, y):
    if x < y:
        return -1
    if x > y:
        return 1
    return 0

t = int(inp.readline())
for I in range(t):
    n, q = map(int, inp.readline().split())
    Array = list(map(int, inp.readline().split()))
    #ArrayT = [(Array[i], i) for i in range(len(Array))]


    for i in range(q): # For each student
        x = int(inp.readline())
        p = Array.index(x)

        array = Array[:] # final array for this query
        #arrayT = ArrayT

        evPos = binPositions(p, n) # Sec de posi por las que debo pasar: evaluation element

        arrayP = [i for i in range(n)] # positions available to be swapped outside the best ones (evaluation elements) (p can be inlcluded because it each element is unique)
        for pos in evPos:
            arrayP[pos] = None

        # Make the necessary swaps: those positions that will be evaluated during binary search
        counter = 0
        canBeDone = True
        for j in range(len(evPos)-1):
            if evPos[j] == None: # If this position has already been swapped with a previous one, ignore it
                continue

            pos = evPos[j]

            # If the array element doesn't satisfy the relation it should for the binary search, then swap it IF POSSIBLE
            if rel(pos, p) == rel(array[pos], x):
                continue
            ## Find pos2 that has its roles interchanged with pos
            # First, try to kill two birds with one stone: within evaluation elements, one that has its role interchanged with the curret array element
            foundGood = False
            for k in range(j+1, len(evPos)):
                if evPos[k] == None:
                    continue
                pos2 = evPos[k]
                if ( (rel(pos, p) == rel(array[pos2], x) ) and (rel(pos2, p) == rel(array[pos], x)) ):
                    foundGood = True
                    swap(array, pos, pos2)
                    evPos[j] = None
                    evPos[k] = None
                    counter += 1
                    break
            if foundGood:
                continue
            # Now try with the leftover positions, those which haven't been swapped with some previous evaluation element
            foundOK = False
            for k in range(len(arrayP)):
                if arrayP[k] == None:
                    continue
                pos2 = arrayP[k]
                if ( (rel(pos, p) == rel(array[pos2], x) )):
                    foundOK = True
                    swap(array, pos, pos2)
                    evPos[j] = None
                    arrayP[k] = None
                    counter += 1
                    break
            if foundOK:
                continue
            # If we get here, it means that it is not possible to swap an element which should be swapped
            canBeDone = False
            break
        
        if canBeDone:
            print(counter)
        else:
            print(-1)
