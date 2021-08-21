F = 15
h = 10
r = 5
Vtank = 3.14 * r ** 2 * h

t = int(input('Enter the time '))

Vwtr = F * t

if Vtank > Vwtr :
    print("Underflow condition ")
    ht = Vwtr / (3.14 * r ** 2)
    hr = h - ht
    print(f"Filled height {ht} and remaining height {hr}")
elif Vtank < Vwtr:
    print("overflow condition")
    print(f"volume of {Vwtr - Vtank}")
else:
    print("tank full")      
