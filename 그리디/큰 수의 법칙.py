# # 결국 사용되는 건 가장 큰 수랑 두번째 큰 수
# # n<=1000이니까 정렬가능

# n,m,k=map(int,input().split())
# data=list(map(int,input().split()))

# data.sort(reverse=True)

# count=0
# result=0
# for _ in range(m):
#   if count==k:
#     result+=data[1]
#     count=0
#     continue
#   result+=data[0]
#   count+=1

# print(result)


# #책풀이: 동일한 로직

# n,m,k=map(int,input().split())
# data=list(map(int,input().split()))

# data.sort()
# first=data[n-1]
# second=data[n-2]

# result=0

# while True:
#   for i in range(k):
#     if m==0:
#       break
#     result+=first
#     m-=1
#   if m==0:
#     break
#   result+=second
#   m-=1

# print(result)

# 시간초과 대비 더 간단하게 수열을 이용한 로직

n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=(k*first+second)*(m//(k+1))
result+=(m%(k+1))*first

print(result)