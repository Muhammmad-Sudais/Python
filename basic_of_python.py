# creating variables

x = 4
y = 4
print(x,y)


# casting

a = str(2)
b = float(2)
print(a,b)


# get the type 

f = 5
print(type(f))


# case-sensitive

T = 5
t = 1
print(T,t)


# Many value to multiple

num1,num2,num3 = 1, 4, 5
print(num1,num2,num3)


# one value to multiple variable

str1 = str2 = str3 = "Muhammad Sudais"
print(str1,str2, str3) 


# Global variable

def myfunc():
    global n
    n = "awesome"
myfunc()
print("Python is " + n)


# random number Generator

import random
no = random.randrange(1,19)
print(no)