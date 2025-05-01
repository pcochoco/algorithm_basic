n = int(input())

arr = list(map(int, input().split()))

min = 1000000
for i in range(n - 1): 
    for j in range(i + 1, n):
   
        if arr[i] > arr[j]:
            dif = arr[i] - arr[j] 
        else:
            dif = arr[j] - arr[i]
        if min > dif:
            min = dif 



print(min)