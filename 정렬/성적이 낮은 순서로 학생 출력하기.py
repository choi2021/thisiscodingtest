N=int(input())
result=[]
for i in range(N):
  name,score=input().split()
  result.append((name,int(score)))

result=sorted(result,key=lambda x:x[1])

for i in range(N):
  print(result[i][0],end=" ")