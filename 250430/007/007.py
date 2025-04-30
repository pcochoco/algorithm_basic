secret_code, meeting_point, time = input().split()
time = int(time) #형변환 

class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
spy = Spy(secret_code, meeting_point, time)
print("secret code : %s\nmeeting point : %s\ntime : %d" %(spy.secret_code, spy.meeting_point, spy.time))