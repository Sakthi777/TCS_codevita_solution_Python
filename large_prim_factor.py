n=int(input())
max1=0
for i in range(2,(n//2)+1
               ):
    while(n%i==0):
        max1=i
        n=n//i
print(max1)
