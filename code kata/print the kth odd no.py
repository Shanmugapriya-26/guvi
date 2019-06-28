n1,n2=map(int,input().split())
lis=input().split()
l=[]
for i in lis:
  if (int(i)%2!=0):
    l.append(i)
print(l[n2-1])
