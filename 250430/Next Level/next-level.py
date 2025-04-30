id, lev = input().split()
#lev = int(lev) -> int(lev)는 lev을 lev 변수에 저장해주지 않음 

class User:
    def __init__(self, id = "codetree", lev = 10):
        self.id = id
        self.lev = lev 

user = User()
print("user %s lv %d" %(user.id, user.lev))

user = User(id, int(lev))
print("user %s lv %d" %(user.id, user.lev))

