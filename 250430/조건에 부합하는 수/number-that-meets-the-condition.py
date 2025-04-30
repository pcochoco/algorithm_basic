a = int(input())

for i in range(1, a + 1):
    if i % 2 == 0 and i % 4 != 0: #짝수이면서 4의 배수 x 
        continue 
    if i // 8 % 2== 0: #8로 나눈 몫이 짝수
        continue 
    if i % 7 < 4: 
        continue 
    print(i, end = " ")