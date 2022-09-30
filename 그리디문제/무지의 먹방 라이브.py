#1. 가장 낮은 음식을 먼저 나오고 나머지는 빠진만큼 감소시킨다.
# - 가장 낮은 걸 먼저 나가고 크기만큼 time에 추가
# - k값을 k//len(q)*len만큼 감소시켜

import heapq

food_times=[3, 1, 2]
k=5

def solution(food_times, k):
    if sum(food_times)<k:
      return -1
    
    q=[]
    for i in range(len(food_times)):
      heapq.heappush(q,(food_times[i],i+1))
    
    length=len(food_times)
    previous=0
    sum_value=0

    while sum_value+((q[0][0]-previous)*length)<=k:
      now=heapq.heappop(q)[0]
      sum_value+=(now-previous)*length
      length-=1
      previous=now
    
    result=sorted(q,key=lambda x:x[1])
    return result[(k-sum_value)%length][1]

    

    


print(solution(food_times,k))
