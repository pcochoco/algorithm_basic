#arr = [[0] * 110] * 110 불가 
#안쪽 가능 바깥은 for i in range 필요

arr = [[0 for i in range(200)] for i in range(200)]

n = int(input())
sum = 0 
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] += 1
            #넓이 = 1의 개수를 더함 
            
            if(arr[j][k] != 1):
                continue 
            sum += 1 

print(sum)