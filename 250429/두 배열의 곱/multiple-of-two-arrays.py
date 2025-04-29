#3x3

arr = [list(map(int, input().split())) for i in range(3)]
#print(arr)
n = input().split() #중간의 \n으로 인해 arr2의 칸이 모자라게 되는 문제
arr2 = [list(map(int, input().split())) for i in range(3)]
#print(arr2)

arr3 = [[0 for i in range(3)] for i in range(3)]
#배열안의 배열(2차원)을 위해서는 arr3 = [0 for in range(3) for i in range(3)] x


#배열 2개의 같은 위치에 있는 수의 곱 
for i in range(3):
    for j in range(3):
        arr3[i][j] = arr[i][j] * arr2[i][j]
        print(arr3[i][j], end=" ")
    print()
