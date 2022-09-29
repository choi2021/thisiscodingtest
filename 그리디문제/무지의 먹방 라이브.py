# food items를 돌면서 줄여나가 그냥 roop를 돌면 시간초과
# food times를 다합친거보다 k가 크면 무조건 -1
# 작은 거부터 제거하면서 줄여나가는게 제일 좋지 않을까
# 전체를 한바퀴 돈다고 생각하고 하나씩 제거해
# 하나씩 제거하다보니 효율성문제 + 런타임 에러도 16,19,23에 나타나 

from collections import deque


def solution(food_times, k):
    if sum(food_times)<k:
        return -1

    q=deque()
    for i in range(len(food_times)):
      q.append((food_times[i],i))
    
    while k!=0: 
      min_time=min(q)[0]
      print(q,min_time)
      length=len(q)
      if k-min_time*length<0:
        break
      k-=min_time*length
      for i in range(length):
        time,index=q.popleft()
        if time>min_time:
          time-=min_time
          q.append((time,index))


    while k!=0:
      time,index=q.popleft()
      time-=1
      q.append((time,index))
      k-=1
    
    return q[0][1]+1
    
    


food_times=[4,1,1,5]
k=4

print(solution(food_times,k))
    
    

# 책풀이: heap을 이용해서 가장 작은 시간의 음식을 내보내고 그만큼 시간을 줄여가면서

import heapq
def solution(food_times,k):
  answer=0
  if sum(food_times)<=k:
    return -1
  q=[]
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))
  n=len(food_times)
  last_food=0

  while k -(q[0][0]-last_food)*n<=k:
    curr=heapq.heappop(q)[0]
    k-=(curr-last_food)*n
    n-=1
    last_food=curr

  q.sort(key=lambda x:x[1])
  return q[k%n][1]