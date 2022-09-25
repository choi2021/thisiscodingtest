# #내풀이
# #1.내림차순으로 정렬
# #2.병사의 수는 최대한=최대한 작게 감소시켜가야해
# #3.앞에서 내림차로 정리되어있으면 그대로 이용해도 돼


# n=int(input())
# soldiers=list(map(int,input().split()))

# d=[0]*(n)
# arr=[]
# result=0

# if soldiers[0]>soldiers[1]:
#   arr.append(soldiers[0])
#   arr.append(soldiers[1])
# else:
#   result+=1
#   d[1]=result
#   arr.append(soldiers[1])

# for i in range(2,n):
#   if soldiers[i]<soldiers[i-1]:
#     arr.append(soldiers[i])
#     d[i]=result
#   else:
#     if soldiers[i]>soldiers[i-2]:
#       result+=1
#       d[i]=result
#       continue
#     elif soldiers[i]<soldiers[i-2]
#       diff1=soldiers[i-2]-soldiers[i-1]
#       diff2=soldiers[i-2]-soldiers[i]
#       if diff1<diff2:
#         result+=1
#         d[i]=result
#         continue
#       else:
#         arr.pop()
#         arr.append(soldiers[i])
#         result+=1
#         d[i]=result

# print(d[n-1])


# 책풀이: LIS로 알려진 전형적인 다이나믹 프로그래밍 문제
# LIS는 가장 긴 오름차순 부분수열
# 0<=j<i 에 대해 D[i]=max(D[i],D[j]+1) if array[j]<array[i]
# D[j]=array[j]를 마지막으로 가지는 값이야

n=int(input())
array=list(map(int,input().split()))
array.reverse()

dp=[1]*n

for i in range(1,n):
  for j in range(0,i):
    if array[j]<array[i]:
      dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))
