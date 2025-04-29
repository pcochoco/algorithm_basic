arr = list(map(int, input().split()))
sum = 0
cnt = 0 

for i in range(len(arr)):
    if arr[i] < 250:
        sum += arr[i]
  
        cnt += 1
    else : break 
avg = sum / cnt * 1.0

print("%d %.1f" %(sum, avg))