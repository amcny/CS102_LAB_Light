ls=[4,6,4,3,3,4,3,4,3,8]
s = set(ls)
lst=[]
k=3
for i in s:
    count=0
    for j in ls:
        if (i==j):
            count+=1
        if(count>k):
            lst.append(i)
            break
print(lst)