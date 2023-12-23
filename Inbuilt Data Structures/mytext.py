fp = open("mytext.txt","r")
l = fp.read()
l = l.split()
di = {}
for i in l:
    count=0
    for j in l:
        if(i==j):
            count+=1
        di[i]=count
    for i in l:
        if(di[i]>2):
            print(di[i])