import sys
input=sys.stdin.readline


n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
end=arr[-1]


def binary_search(arr,start,end,target):
  result=0
  while start<=end:
    mid=(start+end)//2
    sum=0
    for i in arr:
      if i-mid>0:
        sum+=i-mid
    if sum>=target:   
      result=mid
      start=mid+1
    else:
      end=mid-1
  return result

print(binary_search(arr,0,end,m))
