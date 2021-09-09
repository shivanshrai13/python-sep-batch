

# random module 

# import random  # standard module
# from random import choice 
# # import math
# lst = [23, 34, 78, 90]

# re = choice(lst)


# print("random choice value", re)


# generate random number between the range
# 

# import random 

# # rn = random.randrange(1, 10, 3)  # 1 4 7 
# rn2 = random.randint(100000, 200000)  # 1 2
# print(rn2)


# OTP generate using random module 


# import random 
# re = random.random()
# # re = 0.6052445154304532
# otp = str(re)[-4:]
# # otp = '0.6052445154304532'
# print(otp)  # 



# guess the number 
import random 
num = random.randint(1, 100)
count = 0
while True:
    user_num = int(input("guess the number between 1 to 100: "))
    count += 1 
    if user_num == num:
        print("Right Match! Win")
        print("Winner count ", count)
        break
    elif user_num < num:
        print("Try Greater number ") 
    elif user_num > num:
        print("Try Smaller Number ") 
       










