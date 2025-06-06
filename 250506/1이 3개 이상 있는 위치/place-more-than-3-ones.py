'''
관리 : x(어떤 객체의 이동)
입력 : 위치

위치에서 좌표들이 있을 때 
이 중 (2, 1)에 대해 
상하좌우에 있는 4값이 있음
1이 몇개 있는가
아니면 대각선 포함 좌표중
1이 몇개 있는가 
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sum = 0
for x in range(n): #모든 좌표에 대해 
    for y in range(n):
        cnt = 0 
        for i in range(4): #모든 방향에 대해 
            nx = x + dx[i] 
            ny = y + dy[i]
    
            if not (0 <= nx < n and 0 <= ny < n):
                continue 

            if arr[nx][ny] == 1:
                cnt += 1 #해당하는 위치에 
        if cnt >= 3: sum += 1 

print(sum)