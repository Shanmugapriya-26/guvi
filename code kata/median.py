n=int(input())
l=list(map(int,input().split()))
l.sort()
if(n==len(l)):
  t=len(l)//2
print(l[t])
