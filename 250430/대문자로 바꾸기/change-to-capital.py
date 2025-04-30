#5행(가로) 3열(세로)

arr = [input().split() for i in range(5)]

for i in range(5):
    for j in range(3):
        #소 -> 대 -32
        #대 -> 소 +32
        arr[i][j] = chr(ord(arr[i][j]) - 32)
        print(arr[i][j], end = " ")
    print()
