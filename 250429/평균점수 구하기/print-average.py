arr = list(map(float, input().split()))
avg = 0.0
for i in range(len(arr)):
    avg += arr[i]

avg = avg/(len(arr))
print("%.1f" %avg)