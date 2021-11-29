#1
from typing import MutableMapping


for i in range(0, 51):
    print(i)

#2

for i in range(0, 1001):
    if i % 5 == 0:
        print(i)

#3 

for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4

sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
        print(sum)  

#5

for i in range(2018, 0, 4):
    print(i)


#6

low_num = 2
high_num = 9
mult = 3

for i in range(low_num, high_num+1):
    if i % mult == 0:
        print(i)
