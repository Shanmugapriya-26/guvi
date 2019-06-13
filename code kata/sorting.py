n=int(input())
l=list(map(int,input().split()))
l.sort()
for n in range(0,len(l)):
  print(l[n],end=' ')
