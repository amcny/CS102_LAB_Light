n = int(input("enter: "))
check = n-5
for i in range(1,6):
    print(i*"*")
for i in range(4):
    print(check*"*")
    check = check-1