minutes=int(input())
hour=0
while(minutes>60):
  hour=hour+1
  minutes=minutes-60
print(hour,minutes)
