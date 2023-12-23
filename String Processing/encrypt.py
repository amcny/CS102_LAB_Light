st = input("enter ")
res1, res2 = "",""
n=len(st)
for i in range(0,n,1):
    if (i%2==0):
        res1+=st[i]
    else:
        res2+=st[i]
print(res1+res2)