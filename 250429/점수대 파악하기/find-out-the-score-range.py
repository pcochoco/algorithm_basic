arr = [] 
cnt = [0] * 11
for i in map(int, input().split()):
    if i == 0:
        break 
    arr.append(i)

for i in range(len(arr)):
    cnt[arr[i]//10] += 1

for i in range(len(cnt) - 1, 0, -1):
    print("%d - %d" %(i * 10, cnt[i]))