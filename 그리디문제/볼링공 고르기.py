# # O(N^2)의 시간 복잡도를 갖는 내풀이

# N,M=map(int,input().split())
# data=list(map(int,input().split()))

# result=[]

# for i in range(len(data)-1):
#   for j in range(i+1,len(data)):
#       if data[i]!=data[j]:
#         result.append((i,j))

# print(len(result))

# 책 풀이: 먼저 고른 볼링공의 무게의 볼링공을 제외한 나머지를 더해줘

N,M=map(int,input().split())
data=list(map(int,input().split()))

array=[0]*11

for i in data:
  array[i]+=1

result=0

for i in range(1,M+1):
  N-=array[i]
  result+=array[i]*N

print(result)