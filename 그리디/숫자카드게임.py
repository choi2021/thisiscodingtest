# n,m=map(int,input().split())
# data=[]
# for i in range(n):
#   data.append(list(map(int,input().split())))

# mins=[]
# for row in data:
#   mins.append(min(row))
# print(max(mins))

#책풀이:훨씬 한번에 정돈된 코드
n,m=map(int,input().split())
result=0
for i in range(n):
  data=list(map(int,input().split()))
  min_value=min(data)
  result=max(result,min_value)
print(result)