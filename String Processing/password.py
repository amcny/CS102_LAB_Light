p = input("enter: ")
n = len(p)
if (n<8) or (n>12):
    print("not valid")
if (p[0].isalpha()==False and p[0].isdigit()==False):
    print("not valid")
spl = 0
up = 0
low = 0
digit = 0
for i in p:
    if(spl>0)and(up>0)and(low>0)and(digit>0):
        print("valid pass")
        break
    if(i.isupper()==True):
        up+=1
    if(i.islower()==True):
        low+=1
    if(i.isdigit()==True):
        digit+=1
    else:
        spl+=1