"""
input()/print(): standard input and output



"""

# calculator 
import time
print("Enter the first number ")
num1 = int(input())

print("Enter the second number ")
num2 = int(input())

print("""Choices for Operations 
1> Add
2> Sub
3> Div
4> Mul
""")
ch = input('Enter the choice 1/2/3/4/ ')
f = open('calc_history.txt', 'a')
if ch == '1':
    op = 'Addition'
    re = num1 + num2
elif ch == '2':
    op = "Subtraction" 
    re = num1 - num2
elif ch == '3':
    op = 'Division'
    re = num1 / num2
elif ch == '4':
    op = 'Multiplication'
    re = num1 * num2

f.write(f"{num1}\t{num2}\t{op}\t{re}\t{time.asctime()}")
          
f.close()


# file handling : Reading and writing operation with local file 

# f = open("C:\\Users\\Amirkhan\\Desktop\\Python-batch-Aug-Sep21\\sample_file.txt", "w")

# f.write("This is my file.\ncreated for sample text data")
# f.write("\nnext line")

# f.close()


# math table 
"""
1   2   3   4   5   6   7   8   9   10
1   4   6   8   10  12  14  16  18  20
.
.
.

"""

# f = open("table.txt", "w")

# Num = 10
# print()
# for i in range(1, Num+1):  # 1 2 3 4 5 6 7 8 9 10
#     for j in range(1, Num+1):
#         f.write(str(i*j)+'\t')
#     f.write("\n")
# f.close()







