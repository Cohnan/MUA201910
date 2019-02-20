from sys import stdin as inp

def removeStables(linea):
    k = 0
    for i in range(len(linea)):
        if linea[i] != '{':
            if linea[i] =='}': k+=1
            continue
        for j in range(i+1, len(linea)):
            if linea[j] == '}':
                linea[i] = ''
                linea[j] = ''
                break
    #print([a for a in linea if a!=''])
    return (len([a for a in linea if a!='']), k)


line = list(inp.readline())
i = 1
while(line[0] != '-'):
    n, k = removeStables(line[:-1])
    #print(n, k)
    print(str(i) + '. ' + str(n/2 + k%2))

    i+=1
    line = list(inp.readline())