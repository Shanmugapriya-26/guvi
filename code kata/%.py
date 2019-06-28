k=True
while True:
	n,op,m= list(map(str,input().split()))
	if (op =='/'):
	  print (int(n)/int(m))
	elif (op=='%'):
	  print (int(n) % int(m))
