# 내풀이: 조합을 이용하려 했지만 graph를 같이 이용하면서 O(n^2*13Cm)으로 시간초과

# from itertools import combinations
# n,m=map(int,input().split())
# graph=[]
# INF=int(1e9)

# for i in range(n):
#   graph.append(list(map(int,input().split())))

# chickens=[]
# houses=[]

# for i in range(n):
#   for j in range(n):
#     if graph[i][j]==1:
#       houses.append((i,j))
#     elif graph[i][j]==2:
#       chickens.append((i,j))

# candidates=list(combinations(chickens,m))



# def get_distance(graph):
#   sum=0
#   for house in houses:
#     hx,hy=house
#     min_dist=INF
#     for candidate in candidates:
#       cx,cy=candidate
#       min_dist=min(abs(cx-hx)+abs(cy-hy),min_dist)
#     sum+=min_dist
#   return sum


# result=INF
# for combi in list(combinations(chickens,m)):
#   temp=[[0]*n for _ in range(n)]
#   for chicken in combi:
#     cx,cy=chicken
#     temp[cx][cy]=2
#   result=min(get_distance(temp),result)

# print(result)


# from itertools import combinations
# n,m=map(int,input().split())
# INF=int(1e9)
# chickens=[]
# houses=[]

# for i in range(n):
#   data=list(map(int,input().split()))
#   for j in range(n):
#     if data[j]==1:
#       houses.append((i,j))
#     elif data[j]==2:
#       chickens.append((i,j))

# print(chickens)
# candidates=list(combinations(chickens,m))

# print(candidates)

# def get_distance(candidate):
#   sum=0
#   for hx,hy in houses:
#     min_dist=INF
#     for cx,cy in candidate:
#       min_dist=min(abs(cx-hx)+abs(cy-hy),min_dist)
#     sum+=min_dist
#   return sum


# result=INF
# for candidate in candidates:
#   result=min(result,get_distance(candidate))

# print(result)


# 