import math

a = int(input())
choice = input()

if choice == 'mm':
    b = 0
elif choice == 'cm':
    b = -1
elif choice == 'm':
    b = -3
elif choice =='km':
    b = -6

mm = a / (10 ** (0 + b))
cm = a / (10 ** (1 + b))
m = a / (10 ** (3 + b))
km = a / (10 ** (6 + b))

print(mm)
print(cm)
print(m)
print(km)