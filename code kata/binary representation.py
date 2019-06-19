s=int(input())
s=str(s)
t=0
for i in range(0,len(s)):
  if(s[i]=='0' or s[i]=='1'):
    t=1
  else:
    t=0
    break
if(t==1):
  print("yes")
else:
  print("no")
