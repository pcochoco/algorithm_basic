n = int(input())
arr = []

if n == 0:
    print(0)
    
while n != 0:
    #res = n % 2 
    arr.append(n % 2)
    n = n // 2
    
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = "")