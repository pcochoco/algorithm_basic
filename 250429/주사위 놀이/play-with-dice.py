arr = list(map(int, input().split()))


#공간이 7개 필요하거나
#0 번째를 1번째로 출력해야

cnt = [0] * 7 #실제 개수 추합 용도

for i in range(len(arr)):
    cnt[arr[i]] += 1 
    #arr[i]인 6에 대해 cnt[6]에 넣도록 

for i in range(1, len(cnt)):
    print("%d - %d" %(i, cnt[i]))


