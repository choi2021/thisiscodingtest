import heapq

n=int(input())

q=[]
for i in range(n):
  heapq.heappush(q,int(input()))

result=0
sum=0
while len(q)!=1:
  sum+=heapq.heappop(q)
  sum+=heapq.heappop(q)
  heapq.heappush(q,sum)
  result+=sum
  sum=0

print(result)