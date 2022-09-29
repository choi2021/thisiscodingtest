# #내풀이: 공포도가 x면 x명이 그룹에 있어야한다.
# # n<=100000이니까 O(n^2)이면 시간초과가 날거야
# # 가장 최소의 공포도를 가진 사람들끼리 그룹을 만들어야 최대 그룹수를 만들 수 있어

# n=int(input())
# data=list(map(int,input().split()))
# data.sort()
# result=0

# for i in range(1,data[-1]+1): # O(n^2)으로 시간초과가 날 수 있어
#   count=data.count(i)
#   if count>=i:
#     result+=count//i

# print(result)


# 책풀이: 현재그룹에 포함된 수가 확인하고 있는 공포도 보다 크거나 같으면 그룹으로

n=int(input())
data=list(map(int,input().split()))
data.sort()
result=0

count=0
for i in data:
  count+=1
  if count>=i:
    result+=1
    count=0

print(result)
