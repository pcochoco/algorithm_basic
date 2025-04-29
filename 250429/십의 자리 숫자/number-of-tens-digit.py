

arr = [] 

for i in map(int, input().split()):
    if i == 0:
        break
    arr.append(i) #append하므로 배열 길이 == len(arr)
cnt = [0] * 10 #0 제외 `1 ~ 9 인덱스에 대해 
#arr의 len과 상관없음 

#각 10의 자리 수가 몇개인지 
#작은 수부터 

for i in range(len(arr)):
    cnt[arr[i] // 10] += 1
    #arr[0]부터 시작
    #cnt[1] 부터 시작 

for i in range(1, len(cnt)):
    print("%d - %d" %(i, cnt[i]))