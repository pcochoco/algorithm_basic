
n = int(input())
dx = [-1, 0, 0, 1] 
dy = [0, -1, 1, 0]  
#좌표상의 위 == 배열 상의 아래
dirs = ['W', 'S', 'N', 'E']
x, y = 0, 0
for i in range(n):
    dir, step = input().split()
    step = int(step)

    for j in range(len(dirs)):
        if dir == dirs[j]:
            x = x + step * dx[j]
            y = y + step * dy[j]
    
print(x, y)