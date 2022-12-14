from bisect import bisect_left,bisect_right

n,x=map(int,input().split())
arr=list(map(int,input().split()))

def count_by_range(arr,target):
  left_index=bisect_left(arr,target)
  right_index=bisect_right(arr,target)
  return right_index-left_index


result=count_by_range(arr,x)
if result==0:
  print(-1)
else:
  print(result)