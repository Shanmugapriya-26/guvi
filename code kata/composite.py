k=int(input())
if(k>1):
  for i in range (2,k):
    if(k%i==0):
      print("yes")
      break
  else:
    print("no")
else:
  print("yes")
