n=input()
l=[]
for i in n:
    if i not in l:
        l.append(i)
if n==l:
    print("Yes")
else:
    print("No")
