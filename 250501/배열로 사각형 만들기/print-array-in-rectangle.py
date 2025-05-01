n = [[1 for i in range(5)] for j in range(5)]

for i in range(1, 5):
    for j in range(1, 5):
        n[i][j] = n[i-1][j] + n[i][j-1]

for i in range(5):
    for j in range(5):
        print(n[i][j], end = " ")
    print()