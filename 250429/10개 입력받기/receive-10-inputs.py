arr = []
cnt = 0 
sum = 0 
avg = 1.0
for i in map(int, input().split()):
    if(i == 0):
        break
    arr.append(i)

    cnt += 1

for i in range(cnt):
    sum += arr[i]
 
avg = sum / cnt * 1.0

print("%d %.1f" %(sum, avg))

