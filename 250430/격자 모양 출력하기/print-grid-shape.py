#n x n 격자 
#m개의 점
#각 점 크기는 행 * 열

n, m = map(int, input().split())
arr = [[0 for i in range(n)] for i in range(n)]

#m개의 점들이 n번 존재 
m_arr = [list(map(int, input().split())) for i in range(n)]


for i in range(n):
    #점은 각 두 값으로 계속 존재(행, 열)
    arr[m_arr[i][0] - 1][m_arr[i][1] - 1] = m_arr[i][0] * m_arr[i][1]
    
for i in range(n):  
    for j in range(n):
        print(arr[i][j], end = " ")
    print()