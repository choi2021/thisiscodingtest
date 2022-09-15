# 내풀이: 콤비네이션을 사용해서 시간복잡도가 높아 

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


# 책풀이: 훨씬 간단하게 정리될 수 있어 
n=int(input())
data=list(map(int,input().split()))  
data.sort()

target=1
for x in data:
  if target<x:
    break
  target+=x

print(target)