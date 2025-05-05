n = int(input())
arr = [0] * 101
for i in range(n):
    x1, x2 = map(int, input().split())

    for k in range(x1, x2 + 1):
        arr[k] += 1 
    
max = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)