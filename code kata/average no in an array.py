n=int(input())
k=list(map(int,input().split()))
k.sort()
if(n==len(k)):
  t=len(k)//2
print(k[t])
