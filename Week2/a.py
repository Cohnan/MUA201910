n = input()
arrS = input().split()
arr = [int(a) for a in arrS]
arr.sort()

l = len(arr)
minDif = arr[1] - arr[0] # at least 2 numbers
ans = str(arr[0]) + " " + str(arr[1])

for i in range(1, l-1):
    dif = arr[i+1] - arr[i]
    if (dif < minDif):
        minDif = arr[i+1] - arr[i]
        ans = str(arr[i]) + " " + str(arr[i+1])
    elif (dif == minDif):
        ans += " " + str(arr[i]) + " " + str(arr[i+1])

print(ans)