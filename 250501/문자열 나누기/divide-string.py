n = int(input())

arr = input().split()
nums =''
#'12' '34' '567' ...

for i in range(len(arr)):
    nums += arr[i]

for i in range(0, len(nums), 5):
    #0~4, 5~9, ... 나머지~len(nums)-1까지
    print(nums[i:i + 5])
    

