day, hour, min = map(int,input().split())
sum = 0 

sum += day * 24 * 60
sum += hour * 60 
sum += min 
    
total = 11 * 24 * 60 + 11 * 60 + 11 
sum = sum - total 
if sum < 0:
    print(-1)
else:
    print(sum)