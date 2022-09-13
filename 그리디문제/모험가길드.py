# N=int(input())
# data=list(map(int,input().split()))

# table=[0]*(N+1)
# result=0

# for num in data:
#   table[num]+=1

# for i in range(1,N+1):
#   if table[i]==0:
#     continue
#   if table[i]>=i:
#     result+=table[i]//i

# print(result)

#내 풀이는 다이나믹 프로그래밍처럼 풀었지만 책의 풀이가 더 간단해

# 풀이
N=int(input())
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