from bisect import bisect_left,bisect_right

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
target=list(map(int,input().split()))

def count_by_range(arr,target):
  left_index=bisect_left(arr,target)
  right_index=bisect_right(arr,target)
  return right_index-left_index


for i in target:
  print(count_by_range(arr,i),end=" ")