n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
'''
for i in range(n): 
    print('*' * (2*i + 1))
'''

for i in range(1, n + 1): # 1~n
    for j in range(i): # 
        print("*", end = " ")
    print()

'''
for i in range(n): #0~n-1
    for j in range(i + 1): #0 / 0 1 / ...
    #n번 동안 각 줄마다 i만큼 출력 
        print("*", end = " ")
    print()
'''