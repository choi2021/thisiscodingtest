import itertools

N=int(input())
data=list(map(int,input().split()))
d=[False]*(sum(data)+1)

for i in range(1,len(data)+1):
  for x in itertools.combinations(data,i):
    d[sum(x)]=True

for i in range(1,len(d)):
  if not d[i]:
    print(i)
    break