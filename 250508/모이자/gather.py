n = int(input())
arr = list(map(int, input().split()))
sum = 0
min = 100000
for i in range(n):
    sum = 0
    for j in range(n):
        
        sum += abs(j - i) * arr[j]

    if min > sum:
        min = sum 

print(min)