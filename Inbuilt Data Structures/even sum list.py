lst = [13,15,16,17,19]
n = len(lst)
sum=0
for i in range(0,n):
    if (lst[i]%2==0):
        sum=sum+lst[i]
print(sum)