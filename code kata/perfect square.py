import math
N,M=map(int,input().split())
t=N*M
n=math.sqrt(t)
if(n-math.floor(n)==0):
  print("yes")
else:
  print("no")
