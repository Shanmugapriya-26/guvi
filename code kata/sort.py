n=int(input())
k=list(map(int,input().split()))
k.sort()
for n in range(0,len(k)):
  print(k[n],end=' ')
