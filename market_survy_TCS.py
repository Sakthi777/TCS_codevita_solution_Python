"""
input
10
2
1 2 3 4 1 2 3 4 1 2
1 2 4 4 3 2 3 1 1 3
2 3 4 4 1 2 3 1 1 2

program
10-->no.of.qus
2-->no.of.participant
1 2 3 4 1 2 3 4 1 2--> default
1 2 4 4 3 2 3 1 1 3
2 3 4 4 1 2 3 1 1 2  two participant

most experting anwer(1,2,3,4)
first partitipant1 with defualt (print the count)
next* the highly choosen option till the  answer of the qustion is right.
if mutiple option is same than print most recent one.

fanially right ans is decided as correct
based on than ans recalculate and find who is topper.
if both are same who is first he is topper

ALGORITHM:

n=10
m=2
default=[1 2 3 4 1 2 3 4 1 2]
t=[[1 2 3 4 1 2 3 4 1 2]]
l=[[1 2 4 4 3 2 3 1 1 3],[2 3 4 4 1 2 3 1 1 2 ]]
t=[[1 2 3 4 1 2 3 4 1 2],[1 2 4 4 3 2 3 1 1 3]] find same ans 
count=6
d=[(1,1),(2,2),(3,4),(4,4),(1,3),(2,2),(3,3),(4,1),(1,1),(2,3)]
y=[1,2,4,4,3,2,3,1,1,3]=default(same or recent)
t=[[1 2 3 4 1 2 3 4 1 2],[1 2 4 4 3 2 3 1 1 3],[2 3 4 4 1 2 3 1 1 2 ]]
print(count=6)
d=
y=[1,2,4,4,1,2,3,1,1,2]

check particitant1= 0+0+1+1+1+1+1+1+1+1=8
check participant2=1+1+1+1+0+1+1+1+1+0=8
first perference to first participant so print(1,8)"""

n=int(input())
m=int(input())
default=list(map(int,input().split()))
l=[]
t=[]
t.append(default)
for i in range(m):
    l.append(list(map(int,input().split())))
for i in l:
    t.append(i)
    count=0
    for j in range(n):
        if  i[j]==default[j]:
            count+=1
    print(count)
    d=list(zip(*t))
    y=[]
    for value in d:
        value=list(reversed(value))
        for x in range(value.count('0')):
            value.remove('0')
        f=max(value,key=value.count)
        y.append(f)
default=y
topper=[]
for i in l:
    count=0
    for j in range(n):
        if i[j]==default[j]:
            count+=1
    topper.append(count)          
    w=max(topper)              
print(topper.index(w)+1,w)









                       
    











            





































