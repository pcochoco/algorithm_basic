n = int(input())

class Student():
    def __init__(self, data):
        self.name = data[0]
        self.lang = int(data[1])
        self.eng = int(data[2])
        self.math = int(data[3])

arr = [Student(input().split()) for i in range(n)]
arr.sort(lambda x : (-x.lang, -x.eng, -x.math))

for i in arr:
    print(i.name, i.lang, i.eng, i.math)

