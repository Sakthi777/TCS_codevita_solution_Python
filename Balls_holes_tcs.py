n=int(input())
d={}
sol={}
for i in range(n):
    d[i]=[]
h=list(map(int,input().split()))
s=int(input())
l=list(map(int,input().split()))
for i in range(s):
    for j in range(n-1,-1,-1):
        if(l[i]<=h[j] and len(d[j])<j+1):
            d[j].append(l[i])
            sol[l[i]]=j+1
            break
    else:
        sol[l[i]]=0
for  m in sol.values():
    print(m,end="")
    
