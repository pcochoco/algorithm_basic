cnt = 0
while(True):
    
    if cnt == 3: break
    i = int(input()) 
    #while 바로 밑에 존재하면
    #모든 줄을 입력받게 됨 
    #EOFError 발생 
    
    if i % 2 != 0:
        continue 
    else: 
        cnt += 1         
        i = i // 2 
        print(i)
    

