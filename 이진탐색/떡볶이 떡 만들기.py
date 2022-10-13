n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=0
start,end=0,arr[-1]
while start<=end:
  mid=(start+end)//2
  sum=0
  for i in arr:
    if i<mid:
      continue
    else:
      sum+=i-mid
  if sum>=m:
    start=mid+1
    result=mid
  else:
    end=mid-1
print(result)