#2행 4열
arr = [list(map(int, input().split())) for i in range(2)]
sum = 0.0
all_sum = 0.0

for i in range(2):
    sum = 0.0
    for j in range(4): 
        sum += arr[i][j] #각 행별로 
        all_sum += arr[i][j]
    print(sum / 4, end = " ") #각 4요소에 대한 평균
print()

for j in range(4):
    sum = 0.0
    for i in range(2): #각 열별로 
        sum += arr[i][j] 
    print(sum / 2, end = " ")
print()

print("%.1f" %(all_sum / 8)) #전체 8 요소 
    


