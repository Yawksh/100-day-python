a='''nums = [3,2,4]
target = 6
index = []
for i in range(len(nums)-1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            index.append(i)
            index.append(j)
            break
print(index)
'''
x=str(123)
y=x[::-1]
print(y)

