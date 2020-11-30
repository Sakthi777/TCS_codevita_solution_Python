n=int(input())
f=input()
m=input()
c_r=m.count('r')
c_m=m.count('m')
l=[]
for i in f:
    l.append(i)
for i in f:
    if i=='r':
        if c_r==0:
            print(len(l),end="")
            break
        c_r-=1
        l.pop(0)
    elif i=='m':
        if c_m==0:
            print(len(l),end="")
            break
        c_m-=1
        l.pop(0)
else:
    print(0,end="")


