
class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height 
        self.weight = weight

n = int(input())
arr = [input().split() for i in range(5)]
#[lee, 167, 40], ... 
#users = [[0 for i in range(3)] for i in range(5)] 
users = []
for i in range(n):
    users.append(User(arr[i][0], arr[i][1], int(arr[i][2]))) 

users.sort(key = lambda x : x.height)
for user in users:
    print(user.name, user.height, user.weight) #users[i].name과 같은 접근 가능 
