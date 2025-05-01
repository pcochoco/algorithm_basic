n = int(input())

arr = [[1 for i in range(n)] for i in range(n)]

for i in range(1, n): #[0][j] 제외 
    for j in range(1, n): #[i][0] 제외
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1] + arr[i - 1][j - 1]
        
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()