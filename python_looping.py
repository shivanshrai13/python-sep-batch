# looping in Python


"""
1. for loop
2. while loop 
"""


##for i in range(1, 11):
##    print("Hello")



"""

*
* *
* * *
* * * *
* * * * *


1
1 2
3 4 5
"""


### factorial of given number 
##num = int(input('Enter the number '))
##s = 1
##for i in range(1, num+1):
##    s = s * i
##print(s)
##    

# logic for the prime number

num = 5
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print('number is prime ')
else:
    print('Number is not prime ')






















