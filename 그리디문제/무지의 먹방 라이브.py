#내풀이는 정확성, 효율성에서 모두 실패..
# 그이유로 빈 음식이 있으면 계속해서 array를 돌아줘야해

def solution(food_times, k):
    order=0
    time=0
    table_length=len(food_times)
    while time!=k:
        if  food_times[order%table_length]!=0:
            food_times[order%table_length]-=1
            order+=1
            time+=1
        else:
            order+=1
    return order%table_length+1


print(solution([2,2,2],3))

#책풀이

import heapq

def solution2(food_items,k):
  if sum(food_items)<=k: #K보다 같거나 작을 경우에는 무조건 -1 반환
    return -1
  q=[]
  for i in range(len(food_items)):
    heapq.heappush(q,(food_items[i],i+1)) # 1이상의 값만 넣어두기 위해서
  
  sum_value=0
  previous=0
  length=len(food_items)

  while sum_value+((q[0][0]-previous)*length)<=k: #가장 작은 값을 먼저 제거해가는 로직을 위해 하나씩 제거하려면 결국 그만큼의 순환을 돌아야하므로 q[0][0]-previous라는 로직이 들어가
    now=heapq.heappop(q)[0]
    sum_value+=(now-previous)*length #제거할 값의 시간을 더해둬
    length-=1 # 제거했으므로 길이는 줄여
    previous=now 
  result=sorted(q,key=lambda x:x[1]) #순서를 번호가 가장작은 순서대로 정리
  return result[(k-sum_value)%length][1] #남은 음식들 내에서 순서를 찾아

solution2([3,1,2],5)