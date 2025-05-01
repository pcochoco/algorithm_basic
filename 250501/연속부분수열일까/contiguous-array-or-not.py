n1,n2 = map(int, input().split())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
k = False
for i in range(len(a1) - 1):
    if k == True: break
    for j in range(len(a2) - 1):
        if a1[i] == a2[j] and a1[i + 1] == a2[j + 1]:
            print("Yes")
            k = True 
            break

if k == False:
    print("No")