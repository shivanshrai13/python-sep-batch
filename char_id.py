# character identification

chr = input('Enter the char ')

if 'a' <= chr <= 'z':
    print("Alphabet Lower case ")
    
elif 'A' <= chr <= 'Z':
    print("Alphabet Upper case ")

elif '0' <= chr <= '9':
    print("Digit Number ")
else:
    print("Special char ")
