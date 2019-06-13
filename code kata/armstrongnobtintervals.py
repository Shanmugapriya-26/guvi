a,b=map(int,input().split())
for n in range(a+1,b):
  temp=n
  sum=0
  while(temp!=0):
    a=temp%10
    sum=sum+a**3
    temp=temp//10
  if(n==sum):
    print(n,end=' ')
