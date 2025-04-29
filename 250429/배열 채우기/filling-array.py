
#선언 
arr = [0] * 10
#n = input().split() #input().split()은 모든 입력 받음
arr = list(map(int, input().split()))
#print(arr)
cnt = 0 
#중간에 0이 입력되면 입력 종료 
for i in range(len(arr)):
   # arr[i] = input().split()
    cnt +=1
    if(arr[i] == 0):
        break
#arr[cnt - 1] = 0(마지막 입력) 
for i in range(cnt - 2, -1, -1):
    print(arr[i], end = " ")

