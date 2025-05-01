a, b = map(int, input().split())
sum = 0

arr = [0 for i in range(a)]

while a > 1:
    res = a % b #나머지 
    a = a // b #몫 저장 
    
    arr[res] += 1 #나머지에 해당하는 인덱스로
    #sum += arr[res] ** 2 
    #각 arr[res] 완전히 계산하지 않고 더하면 중복 

for i in range(len(arr)):
    sum += arr[i] ** 2 

print(sum)

