st = input("enter: ")
spl = 0
up = 0
low = 0
digit = 0

for i in st:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
    elif i.isdigit():
        digit += 1
    else:
        spl += 1
print(f"Uppercase count: {up}")
print(f"Lowercase count: {low}")
print(f"Special character count: {spl}")
print(f"Digit count: {digit}")