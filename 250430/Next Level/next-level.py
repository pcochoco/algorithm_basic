id, lev = input().split()
int(lev)

class User:
    def __init__(self, id = "codetree", lev = 10):
        self.id = id
        self.lev = lev 

user = User()
print("user %s lv %d" %(user.id, user.lev))

user = User("hello", 28)
print("user %s lv %d" %(user.id, user.lev))

