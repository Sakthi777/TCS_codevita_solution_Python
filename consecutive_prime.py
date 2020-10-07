n=int(input())
l=[]
count=0
for j in range(2,n+1):
    for i in range(2,(j//2)+1):
        if(j%i==0):
            break
    else:
        l.append(j)
for i in range(1,len(l)):
    sum1=0
    for j in l:
        sum1+=j
        if sum1==l[i]:
            count+=1
        if sum1>l[i]:
            break
print(count)
