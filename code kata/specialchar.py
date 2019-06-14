n=input()
count=0
for i in n:
  if(i.isspace()==False and i.isnumeric()==False and i.isalpha()==False):
    count=count+1
print(count)
