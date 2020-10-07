n,k=(input().split())
n=int(n)
k=int(k)
l=[]
c=0
"""for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print(l)
if (k>len(l)):
    print(1)
else:
    print(l[-k])"""

# other method
for i in range(n,0,-1):
    if(n%i==0):
        c+=1
        if(c==k):
            print(i)
            break
else:
    print(1)
        
    

    
        
        
    
    
