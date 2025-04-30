#n x m 
n, m = map(int, input().split())

arr = [[0 for i in range(m)] for i in range(n)]

k = 0
for j in range(m): 
    for i in range(n):

        if(j % 2 == 0):
            arr[i][j] = k
        else:
            arr[n - i - 1][j] = k 

        #arr[0][0] arr[1][0] arr[2][0] arr[3][0]
        #arr[3][1] arr[2][1] arr[1][1] arr[0][1]


        #arr[i][0] -> 0 
        #arr[n - i - 1][1] -> 1  
        #arr[i][2] -> 2 
        #arr[n - i - 1][3] ... -> 3 

        #arr[i][j]
        #arr[n - i][j] 

        k += 1 

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()