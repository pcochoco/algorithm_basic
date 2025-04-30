n = int(input())

#n x n 
arr = [[0 for i in range(n)] for i in range(n)]

k = 1 
for i in range(n):
    for j in range(n):
        arr[j][i] = k 
        k += 1

for i  in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()