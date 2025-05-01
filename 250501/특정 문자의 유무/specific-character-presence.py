n = input()

s1 = "ee"
s2 = "ab"
f1 = False
f2 = False
for i in range(len(n)-1): #LeeBrosCode
    
    if n[i] == s1[0] and n[i + 1] == s1[1]:
        f1 = True
        print("Yes", end = " ")
        break

    

if f1 == False:
    print("No", end = " ")

for i in range(len(n)-1): #LeeBrosCode
    if n[i] == s2[0] and n[i + 1] == s2[1]:
        f2 = True
        print("Yes")
        break 
if f2 == False:
    print("No")
    
        