n, m = map(int,(input().split())) #세로 가로

#3 x 5 

arr = [[0 for i in range(m)] for i in range(n)]
k = 1
for i in range(n): #세로
    
    for j in range(m): #가로 
        arr[i][j] = k
        print(arr[i][j], end=" ")
        k += 1
    print()