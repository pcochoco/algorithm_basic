#격자 크기 동전 개수
n, m = map(int, input().split()) # 2 3 

arr = [[0 for i in range(n)] for i in range(n)]

for i in range(m): #입력값 받음 
    x, y = map(int, input().split())

    arr[x-1][y-1] = 1 

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()

