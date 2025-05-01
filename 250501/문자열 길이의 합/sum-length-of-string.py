#모든 문자열 길이의 합 
n = int(input())

words = [input() for i in range(n)]

sum = 0
cnt = 0
#주어진 문자열 중 첫번째 문자 
for word in words:

    if word[0] == 'a':
        cnt += 1 
    sum += len(word)

print(sum, cnt)

