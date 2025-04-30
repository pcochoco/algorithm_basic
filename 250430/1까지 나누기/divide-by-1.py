n = int(input())
real_n = n 
cnt = 0 
res = n 
for i in range(1, n + 1):
    if real_n < 1:
        break  
    real_n = real_n // i 

    cnt += 1 

print(cnt)