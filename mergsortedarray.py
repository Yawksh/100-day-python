# array1=[1,2,4,5,7]
# array2=[2,3,4,5,6,8]
# array2.extend(array1)
# array2.sort()
# array2=reversed
# print(array2)

# max_size=max(len(array2) , len(array1))
# min_size=min(len(array2) , len(array1))
# array3=[]
# for i in range(min_size):
#     if array1[i]<=array2[i]:
#         array3.append(array1[i])
#         array3.append(array2[i])
#     else:
#         array3.append(array2[i])
#         array3.append(array1[i])
# for j in range(min_size,max_size)
target=9
nums=[1,2,5,8,9,9]
nums.sort()
left = 0
right = len(nums)
found = 0
while (found == 0 and right != left):
    mid = (left + right) // 2
    if target == nums[mid]:
        found = 1

    elif target < nums[mid]:
        right = mid-1
    elif target > nums[mid]:
        left = mid+1

if found==1:
    index1=nums.index(mid)
    print(index1)
else:
    print(-1)

