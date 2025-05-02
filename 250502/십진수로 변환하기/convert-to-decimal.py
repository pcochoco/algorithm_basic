n = input()
sum = 0
for i in range(len(n) - 1, -1, -1):
    sum += int(n[len(n) - 1 - i]) * (2** i) 
print(sum)