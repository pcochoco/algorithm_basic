
arr = [list(map(int, input().split())) for i in range(4)]

for i in range(4):
    sum = 0
    for j in range(4):
        sum += arr[i][j]
    print(sum)  