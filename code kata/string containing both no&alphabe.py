n=input()
b=0
a=0
for i in n:
    if(i.isalpha()==True):
        a=a+1
    elif(i.isdigit()==True):
        b=b+1
if(a>0 and b>0):
    print("Yes")
else:
    print("No")

