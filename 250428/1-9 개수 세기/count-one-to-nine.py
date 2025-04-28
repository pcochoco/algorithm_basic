n = int(input())

arr = list(map(int, input().split())) #1 8 5 
cnt = [0 for i in range(10)] #cnt[0] = 0  ... 
 # 0 1 2 ... 9
for j in range(n):
    cnt[arr[j]] += 1 #cnt[]

for i in range(1, 10):
    print(cnt[i])