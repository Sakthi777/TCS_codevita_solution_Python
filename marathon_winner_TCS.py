"""
3
8
2 2 4 3 5 2 6 2 3
3 5 7 4 3 9 3 2 2
1 2 4 2 7 5 3 2 4

"""
from collections import Counter
n=int(input())
s=int(input())
l=[]
g=[]
p=[]
for j in range(n):
    k=list(map(int,input().split()))
    d=k[-1]
    k.pop()
    sum1=0
    w=[]
    for i in k:
        q=i*d
        sum1+=q
        w.append(sum1)
    l.append(w)
print(l)
for i in range(s):
    g.append(list(list(zip(*l))[i]))
for i in range(1,len(g),2):
    m=max(g[i])
    for j in range(len(g[i])):
        if m==g[i][j]:
            p.append(j+1)
res=dict(Counter(p))
l1=list(res.values())
l2=list(res.keys())
print(l2[l1.index(max(l1))])














                         
