#n x m 

n, m = map(int, input().split())

#m개의 원소를 2n번 
m_arr = [list(map(int, input().split())) for i in range(2*n)]

arr = [[0 for i in range(m)] for j in range(n)]

for i in range(n): 
    for j in range(m):

        if m_arr[i][j] != m_arr[i + n][j]:
            arr[i][j] = 1
        print(arr[i][j], end = " ")
    print()