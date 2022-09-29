# from itertools import combinations

# n,m=map(int,input().split())
# balls=list(map(int,input().split()))

# combis=list(combinations(balls,2))
# result=0

# for i in combis:
#   if i[0]!=i[1]:
#     result+=1

# print(result)


# 책풀이: A가 먼저 뽑고 하나씩 증가하면서 B가 뽑을 수 있는 경우의 수를 계산해

n,m=map(int,input().split())
balls=list(map(int,input().split()))

array=[0]*11
for ball in balls:
  array[ball]+=1

result=0

for i in range(1,m+1):
  n-=array[i]
  result+=array[i]*n
print(result)