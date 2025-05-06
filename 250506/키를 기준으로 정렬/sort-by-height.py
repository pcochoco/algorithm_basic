
class User:
    def __init__(self, data):
        self.name = data[0]
        self.height = int(data[1]) 
        self.weight = int(data[2])

n = int(input())
arr = [User(input().split()) for i in range(n)]
arr.sort(key = lambda x : x.height)

for i in arr:
    print(i.name, i.height, i.weight)
