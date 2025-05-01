arr = ["apple", "banana", "grape", "blueberry", "orange"]

n = input()
cnt = 0 
for word in arr: #모든 word들에 대해 
    
    if n == word[2] or n == word[3]:
    #apple 에 a p p l e 
        cnt += 1 
        print(word)
print(cnt)

