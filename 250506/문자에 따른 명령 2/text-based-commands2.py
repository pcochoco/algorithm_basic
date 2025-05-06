dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
dir_num = 1 #북쪽 바라보는 상태 
#배열은 좌표와 반대 방향

#직진 
n = input()
for i in range(len(n)):

    if n[i] == 'L':
        #우회전
        dir_num = (dir_num + 1) % 4 

    elif n[i] == 'R':
        #좌회전 - 음수에 모듈러 동작 예상 x
        #+4로 결과를 양수화한 다음 모듈러
        dir_num = (dir_num - 1 + 4) % 4
    elif n[i] == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)