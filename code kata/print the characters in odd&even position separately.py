n=input()
n1,n2 = "", ""
for i in range(0,len(n),2):
	  n1=n1+n[i]
for i in range(1,len(n),2):
	  n2=n2+n[i]
print(n1,n2)
