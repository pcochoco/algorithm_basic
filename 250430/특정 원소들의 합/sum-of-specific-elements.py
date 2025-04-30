arr = [list(map(int, input().split())) for i in range(4)]

#i = 0 j = 0
#i = 1 j = 0 1 
sum = 0
for i in range(4):
    for j in range(i + 1):
        sum += arr[i][j]

print(sum)