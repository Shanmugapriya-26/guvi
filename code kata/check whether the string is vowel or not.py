k=input()
l=['a','e','i','o','u','A','E','I','O','U']
if any(char in l for char in k):
  print("yes")
else:
  print("no")
