n = int(input())
cur = 10 #구간의 크기 - 정확한 위치 필요 x 
arr = [0] * 21 #-10~0~10  
for i in range(n):
    step, dir = input().split()
    step = int(step)

    if dir == 'R':
        for k in range(cur, cur + step):
            arr[k] += 1

        cur = cur + step
    else: #dir == 'L' 
        for k in range(cur, cur - step, -1):   
            arr[k] += 1
            
        cur = cur - step 

sum = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        sum += 1 

print(sum)