# from itertools import permutations

# N=int(input())
# nums=list(map(int,input().split()))
# operator_nums=list(map(int,input().split()))
# operators=[]

# for i in range(4):
#   for j in range(operator_nums[i]):
#     if i==0:
#       operators.append("+")
#     elif i==1:
#       operators.append("-")
#     elif i==2:
#       operators.append("*")
#     else:
#       operators.append("/")

# result=[]
# for perm in set(permutations(operators,len(operators))): #set로 중복제거
#   sum=nums[0]
#   for i in range(1,len(nums)):
#     if perm[i-1]=="+":
#       sum+=nums[i]
#     elif perm[i-1]=="-":
#       sum-=nums[i]
#     elif perm[i-1]=="*":
#       sum*=nums[i]
#     elif perm[i-1]=="/":
#       if sum<0:
#         sum=(-sum//nums[i])*-1
#         continue
#       sum=sum//nums[i]
#   result.append(sum)
# result.sort()
# print(result[-1])
# print(result[0])

#책풀이:dfs를 이용하는데 전체 경우를 찾을수 있다는게 신기..

n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

min_value=1e9
max_value=-1e9

def dfs(i,now):
  global min_value, max_value,add,sub,mul,div
  print(add,sub,mul,div)
  if i==n:
    min_value=min(min_value,now)
    max_value=max(max_value,now)
  else:
    if add>0:
      add-=1
      dfs(i+1,now+data[i])
      add+=1
    if sub>0:
      sub-=1
      dfs(i+1,now-data[i])
      sub+=1
    if mul>0:
      mul-=1
      dfs(i+1,now*data[i])
      mul+=1
    if div>0:
      div-=1
      dfs(i+1,int(now/data[i]))
      div+=1
dfs(1,data[0])


print(max_value)
print(min_value)
