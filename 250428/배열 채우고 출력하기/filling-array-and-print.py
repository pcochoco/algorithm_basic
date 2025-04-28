arr = input().split()

#for i in range(1, len(arr) + 1, 1):
    #print(arr[-i])
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = "")