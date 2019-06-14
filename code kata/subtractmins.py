hr1,min1=list(map(int,input().split()))
hr2,min2=list(map(int,input().split()))
hour=abs(hr1-hr2)
minute=abs(min1-min2)
while(minute>60):
  hour=hour+1
  minute=minute-60
print(hour,minute)
