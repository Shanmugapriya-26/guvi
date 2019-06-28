k=list(input())
if len(k)%2==0:
    k[int(len(k)/2)] ='*'
    k[int(len(k)/2)-1]='*'
else:
    k[int(len(k)/2)] ='*'
for i in range(0,len(k)):
    print(k[i],end='')
