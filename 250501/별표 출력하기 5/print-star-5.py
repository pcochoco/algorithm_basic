'''
*** *** ***
** **
*
'''

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n - i):
        arr[i][j] = (n - i) * '*'
        print(arr[i][j], end = " ")
    print()