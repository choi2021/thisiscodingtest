N=int(input())
result=[]
for i in range(N):
  result.append(int(input()))

result.sort(reverse=True)
for i in range(N):
  print(result[i],end=" ")