n = input()
str = raw_input()

found = False
for i in range(n-1):
    if str[i] > str[i+1]:
        found = True
        break

if (found):
    print(str[:i] + str[i+1:])
else:
    print(str[:-1])
