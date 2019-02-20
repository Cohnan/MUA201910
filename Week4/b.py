from sys import stdin as inp

y, b, r = map(int, inp.readline().split())
b -= 1
r -= 2

print(min([y, b, r])*3 + 3)