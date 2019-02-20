from sys import stdin as inp

table = list(inp.readline()[:-1])
hand = list(inp.readline()[:-1])
hand = [hand[i] for i in range(len(hand)) if (i+1)%3 != 0]

if (table[0] in hand or table[1] in hand): #The 2 sets are disjoint, so it is okay to do this rough test
     print('YES')
else:
     print('NO')