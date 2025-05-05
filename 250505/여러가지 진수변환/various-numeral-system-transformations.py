#4, 8진수 
n, b = map(int, input().split())
arr = []
while True:
    if n == 0:
        break 
    res = n % b
    n = n // b
    arr.append(res)

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = "")
