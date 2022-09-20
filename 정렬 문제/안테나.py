# 내풀이: 전체를 다 돌면서 거리를 계산해서 최소값을 찾아 
# N이 20000까지라 O(N^2)은 시간 초과... 

# import sys
# input=sys.stdin.readline
# N=int(input())
# houses=list(map(int,input().rstrip().split()))
# results=[]

# for i in range(len(houses)):
#   total=0
#   for j in range(len(houses)):
#     if i==j:
#       continue
#     else:
#       total+=abs(houses[i]-houses[j])
#   results.append((total,houses[i]))

# results.sort(key=lambda x:(x[0],x[1]))
# print(results[0][1])



# 책풀이
n=int(input())
data=list(map(int,input().split()))
data.sort()

print(data[(n-1)//2])