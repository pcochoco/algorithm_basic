n = int(input())
arr = []
while n != 0:
    res = n % 2 
    arr.append(res)
    n = n // 2
    
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = "")