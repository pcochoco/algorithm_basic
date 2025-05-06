
class Agent:
    def __init__(self, data):
        self.name = data[0]
        self.score = int(data[1])
    
agents = [Agent(input().split()) for i in range(5)]
min = agents[0]
for i in range(5):
    if agents[i].score < min.score:
        min = agents[i]

print(min.name, min.score)

 