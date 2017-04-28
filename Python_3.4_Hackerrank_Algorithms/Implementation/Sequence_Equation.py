
# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input().strip())
nums = [int(num) for num in input().strip().split(' ')]

for i in range(1,len(nums)+1):
    if i in nums:
        temp = (nums.index(i) + 1)
        if temp in nums:
            print(nums.index(temp) + 1) 
            

