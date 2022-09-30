n=int(input())
arr=[300,60,10]
result=[0]*3
for i in range(3):
  if n//arr[i]==0:
    continue
  result[i]=n//arr[i]
  n%=arr[i]

if n!=0:
  print(-1)
else:
  for i in range(3):
    print(result[i],end=" ")