#variable =a container for a value behavesas thew value thatthe container has
#first="yawksh"
#last ="fentaw"
#full_name=first+last
#print("Hello"+" "+full_name)
#print(type(full_name))
#age=23
#age+=1
#print(age)
#print("my age is"+str(age))
#print(type(age))
#human=False
#print(human)
#print(type(human))
chars=[]
give=[23,12,76,89,88]
for i in give:
    count=0
    if '0' not in str(i):
        for x in str(i):
         if i%int(x)==0:
            count+=1
        if count==len(str(i)):
             chars.append(i)
print(chars)



