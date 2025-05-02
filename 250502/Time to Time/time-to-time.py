a, b, c, d = map(int, input().split())

h, m = a, b 
cnt = 0 #흐른 시간 계산  
while True:
    if h == c and m == d: 
        break 
    #아니면 증가 
     
    cnt += 1 

    if m == 59:
        h = h + 1 
        m = 0 
    else: 
        m += 1

print(cnt)
#print("%d시 %d분부터 %d분이 흘러야 %d시 %d분이 됩니다." %(a, b, cnt, c, d))

