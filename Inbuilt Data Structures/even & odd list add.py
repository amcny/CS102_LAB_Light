lst = [13,15,16,17,19,20,21]
n = len(lst)
sum=0
sum1=0
for i in range(0,n):
    if (lst[i]%2==0):
        sum=sum+1
    else:
        sum1=sum1+1
print(sum)
print(sum1)