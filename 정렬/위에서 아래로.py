N=int(input())
data=[]
for _ in range(N):
  data.append(int(input()))

data=sorted(data,reverse=True)

for j in data:
  print(j, end=" ")
