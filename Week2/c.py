n = input()
arrS = input().split()
arr = [int(a) for a in arrS]
l = len(arr)
counter = 0

for i in range(1, l):
    copy = arr.copy()
    for j in range(i-1, -1, -1):
        if (arr[j] > arr[j+1]):
            counter += 1
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    
print(counter)
