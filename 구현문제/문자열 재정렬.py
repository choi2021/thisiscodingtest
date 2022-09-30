

s=input()
result=[]
sum=0
for i in s:
  if i.isalpha():
    result.append(i)
  else:
    sum+=int(i)

result.sort()
result.append(sum)
for i in result:
  print(i,end="")