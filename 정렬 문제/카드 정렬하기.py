#1. N이 100000이라 O(N^2)이 되지 않게 고려
#2. 작은 것끼리 더해줘야 최소
#3. 가장 작은 것끼리 묶기 위해 항상 정렬
#이 방식으로 정리할 시 O(N^2logN)이라서 시간초과
N=int(input())
nums=[]
for i in range(N):
  nums.append(int(input()))
nums.sort()

total=0
for _ in range(N-1):
  sum=nums[0]+nums[1]
  total+=sum
  nums=nums[2:]
  nums.append(sum)
  nums.sort()


print(total)

#다른사람풀이: 항상 최소값이 나와야하니까 heap을 이용해
#heap은 삽입,삭제에 O(logn)이니까 최종적으로 O(NlogN)을 가져

import heapq

N=int(input())
q=[]
for i in range(N):
  heapq.heappush(q,int(input()))


total=0
for _ in range(N-1):
  sum=heapq.heappop(q)+heapq.heappop(q)
  total+=sum
  heapq.heappush(q,sum)




print(total)