n = int(input())

arr = [0] * 200

for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100 #음수의 양수 처리
    #-100~100까지 가능
    x2 += 100 
    for j in range(x1, x2):
        #구간 - 끝점에서 닿는 경우 겹침 x 
        arr[j] += 1 

answer = 0 

for i in range(200):
    if answer < arr[i]: 
        answer = arr[i] 
    
print(answer)



