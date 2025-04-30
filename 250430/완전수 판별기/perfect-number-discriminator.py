#완전수 = 자기 자신을 제외한 약수의 합이
#자신이 되는 수
#1 + 2 + 3 = 6

n = int(input())
sum = 0 
for i in range(1, n):
    if n % i == 0:
        sum += i 
if sum == n:
    print("P")
else:
    print("N")