array=[1,1,2,2,3,3,3,4,5,5]
for i in array:
    if array.count(i)>1:
        del array[i]
print(array)

