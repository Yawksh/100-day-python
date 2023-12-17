height=[1,8,6,2,5,4,8,3,7]
array_truth=[]
array=[]

for i in range(len(height)-1):
    max1=0
    for j in range(i+1,len(height)):
        max1=abs(height[j]-height[i]) *abs(j-i)
        array.append(max1)
    max2 = max(array,key=lambda x: x)
    array_truth.append(max2)

    array.clear()
result=max(array_truth)
print(result)

