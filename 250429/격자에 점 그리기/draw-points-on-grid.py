#격자 크기 N, 점의 개수 M 
n, m = map(int, input().split())

#m개의 점 
marr = [list(map(int, input().split())) for i in range(m)]
arr = [[0 for i in range(n)] for i in range(n)]


for i in range(m): #3 
    
    arr[marr[i][0] - 1][marr[i][1] - 1] = i + 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()