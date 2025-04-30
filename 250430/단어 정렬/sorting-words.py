
n = int(input())
arr = [input() for i in range(n)]

arr.sort()
#sorted(arr)
for i in range(n):
    print(arr[i])
