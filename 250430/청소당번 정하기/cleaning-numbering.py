#0일을 기점으로 2일마다 교실 청소
#3일마다 복도 청소
#12일마다 화장실 청소

n = int(input())
c12, c3, c2 = 0, 0, 0
for i in range(1, n + 1):
    if i % 12 == 0:
        c12 += 1 
    elif i % 3 == 0:
        c3 += 1
    elif i % 2 == 0:
        c2 += 1 

print(c2, c3, c12)