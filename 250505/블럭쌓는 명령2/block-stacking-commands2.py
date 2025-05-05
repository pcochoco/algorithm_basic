#n번칸까지 쌓인 블럭 수 
#k개의 줄동안 블럭 쌓는 명령 
n, k = map(int, input().split())
arr = [0] * (n + 1) #1~n번칸까지 
for i in range(k):
    #a ~ b까지 쌓음 
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        arr[j] += 1

max = arr[1]
for l in range(1, n + 1):
    if max < arr[l]:
        max = arr[l]
print(max)