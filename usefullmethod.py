import math
import os

pi = 3.14
x = 4
y = 6
z = 7
# print(round(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,4))
# print(math.sqrt(345))
# print(max(x,y,z))
# print(min(x,y,z))
# slicing =creating a sub string by edxxtracting elemaents from another cstring
# indefxing[]or slice()
# [start:stop::stop
indexing = '''name="yawkal fentaw"
firstname=name[0:6]
lastname=name[7:]
nickname=name[6:8:11]
print(firstname.capitalize())
print(lastname.capitalize())
print(nickname.capitalize())'''
# tuple= collection  which is ordered and unchangeable used to group together related data
student = ("Yawksh", "21", "male")
# print(student.count("Yawksh"))
mytuple = '''#print(student.index("21"))
for x in student:
    print(x)
if 'Yawksh' in student:
    print("bro is here")
    LIST=['abebe','belete','ashenafy','anargachew']
    mytuple=tuple(LIST)
print(mytuple)
LIST=list(mytuple)
LIST.insert(0,"yawkal")
mytuple=tuple(LIST)
print(mytuple)'''
sets = ''''
#set =collection which is order ,unindexed,not duplicate values
utensils={'fork','spooon','knife'}
dishes={'bowl','plate','knife','cup'}
utensils.add('napakin')
utensils.remove('spooon')
#utensils.clear()
utensils.update(dishes)
dinner_table=utensils.union(dishes)
for x in dishes:
    print(x)
print("one for loop finished")
for x in dinner_table:
    print(x)
print(dinner_table.difference(dishes))
print(dinner_table.intersection(dishes))
'''
# dictionary a changeable,unordered collection of unique key:value pairs
# fast because they use hashing , allow us to a value quickly
dictionary = '''capitals={'USA':'washigton DC','india':'new dehli','china':'Boijing','Russia':'moscow'}
#print(capitals['Russia'])
#print(capitals.get('germany'))
#print(capitals.values())
#print(capitals.items())
capitals.update({'germany':'Berlin'})
capitals.update({'USA':'Las vergas'})
capitals.pop('china')
for key,value in capitals.items():
    print(key+' '+value)'''
# function= a block of code excute when called
functoions = '''def hello(name):
    return ("hello"+' '+name+" "+"how are you doing?")
myname="yawkal"
print(hello(myname))'''
# keyword arguements = arguements preceded by an identifier  when we passs themto full
# the order of the arguements doesn;t matter ,unlike positional arguements python knows
# the name of the arguements that our function recieved
f2 = '''def hello(age,year,myname):
    x="hello"+' '+"my name is"+myname+" "+"i am "+age +" years old and "+"i am "+ year+" year SEng student"
    print(x)
    return x
hello(myname="yawksh",age="24",year="4th")
print(x)'''
# nested function calls = function calls insu=ide other function calls
# inner most inner most calls are resolved first returened the value is
# used as ardguement for the next outer function
# print(roun d(abs(float(input('Enter a whole  number: ')))))

# scope odf variables= it's the region that is recognized a variable is only available from inside the region it is created
# a globaland locally scoped verssions of a variable can be created
name = "abeba"  # global variable


def displa_num():
    name = 'yawksh'  # local variable
    return (name)


# print(displa_num())
# precedence of variables LEGB=L-local,E-Enclosing,G-Global,B-builtin
# *args= parameter thet will be pack all arguements in to a tuple
# usefull so that a function can accept varying amount of arguements
def add(*stuff):
    sum = 0
    for i in stuff:
        sum = sum + i
    return sum


x = add(2, 1, 2, 3)


# print(x)


# **kwargs= parameter thet will pack all arguements in to a dictionery
# useful so that function can accept varying amount keyword arguements

def hello(**kwargs):
    x = "hello" + ' ' + "my name is" + kwargs['myname'] + " " + "i am " + kwargs['age'] + " years old and " + "i am " + \
        kwargs['year'] + " year SEng student"
    # print(x)
    return x


hello(myname="yawksh", age="24", year="4th")

import random

x = random.randint(1, 6)
y = random.random()
# print(x)
# print(y)
mylist = ['rock', 'paper', 'scissors']
z = random.choice(mylist)
# print(z)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'D', 'j']
random.shuffle(cards)
# print(cards)
# exceptions= events detected during excution that interrupt the flow a program
exception = '''try:
    a=int(input('enter a number to  devide:'))
    b=int(input('Enter the number to devide by: '))
    result=a//b
    print(result)
except Exception:
    print("some thing went wrong")'''
# file based in python
path ='''"C:\\Users\\HP\\Desktop\\yawk\\python dev\\abc.txt"

if os.path.exists(path):
    print("that location  exists")
    if  os.path.isfile():
        print("that is a file")
    elif os.path.isdir():
        print("that is a folder")
else:
    print("that location doesn't exist")
'''

#file handling= read write and update file
try:
    text="this is your favourite language\nwork smartly yawksh"
    with open("x.txt", 'a') as file:
       print(file.write(text))
except Exception :
    print("file not found")
#f=open('z.txt','x')
#f.write("now the file is overrided")
if os.path.exists("abcde"):
  os.rmdir('abcde')
  print("succesfully deleted")
else:
    print("the folder not exists")
