m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 1 #시작일 포함 

while not (m1 == m2 and d1 == d2): 
     
    cnt += 1
    d1 += 1  

    if d1 > num_of_days[m1]: 
        #증가했을 때 day 가 크면 
        #실제로는 month 넘어간 날짜인 것 

        m1 += 1  
        d1 = 1 
    
print(cnt)