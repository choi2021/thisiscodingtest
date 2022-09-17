#내풀이
#1.좌표가 중요하므로 집과 치킨집의 좌표를 담아
#2.치킨집의 수가 M보다 작으면 바로 거리 최솟값을 계산해서 넣는다
#3.M이 치킨집 수보다 크면 각치킨집에서의 거리를 계산한 후에 가장 거리가 먼 곳부터 삭제한다.

# N,M=map(int,input().split())

# data=[]
# for _ in range(N):
#   row=list(map(int,input().split())) 
#   data.append(row)

# houses=[]
# chicks=[]
# result=[]

# for i in range(N):
#   for j in range(N):
#     if data[i][j]==1:
#       houses.append((i,j))

# for i in range(N):
#   for j in range(N):
#     if data[i][j]==2:
#       chicks.append((i,j))

# def calcDist(house,chick):
#   hx,hy=house
#   cx,cy=chick
#   return abs(hx-cx)+abs(hy-cy)

# def totalChickDist(houses,chicks):
#   total=0
#   for house in houses:
#     min_dist=2*N
#     for chick in chicks:
#       dist=calcDist(house,chick)
#       if dist<min_dist:
#         min_dist=dist
#     total+=min_dist
#   return total

# if len(chicks)<=M:
#   print(totalChickDist(houses,chicks))
# else:
#   del_targets=[]
#   distances=[0]*len(chicks)
#   for i in range(len(chicks)):
#     for house in houses:
#       dist=calcDist(house,chicks[i])
#       distances[i]+=dist
  
#   while len(chicks)-len(del_targets)==M:
#     max_val=max(distances)
#     index=distances.index(max_val)
#     del_targets.append(index)
  
#   orderd_chicks=[]
#   for i in range(len(chicks)):
#     if i not in del_targets:
#       orderd_chicks.append(chicks[i])
  
#   print(totalChickDist(houses,orderd_chicks))
      
# 책풀이: 간단하게 M개의 치킨집을 골랐을 때 가장 최소가 되는 거리를 반환해

from itertools import combinations

n,m=map(int,input().split())
chicken,house= [], []

for r in range(n):
  data=list(map(int, input().split()))
  for c in range(n):
    if data[c]==1:
      house.append((r,c))
    if data[c]==2:
      chicken.append((r,c))

candidates=list(combinations(chicken,m))
def get_sum(candidate):
  result=0
  for hx,hy in house:
    temp=1e9
    for cx,cy in candidate:
      temp=min(temp,abs(hx-cx)+abs(hy-cy))
    result+=temp
  return result

result=1e9
for candidate in candidates:
  result=min(result,get_sum(candidate))

print(result)



