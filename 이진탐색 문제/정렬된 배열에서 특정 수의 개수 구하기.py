# n,x=map(int,input().split())
# data=list(map(int,input().split()))

# start=0
# end=n-1
# count=0
# def binary_search(arr,start,end):
#   global count
#   if start>end:
#     return 
#   mid=(start+end)//2
#   if arr[mid]==x:
#     count+=1
  
#   binary_search(arr,start,mid-1)
#   binary_search(arr,mid+1,end)
  
# binary_search(data,start,end)
# if count==0:
#   print(-1)
# else:
#   print(count)

#책풀이: 정렬되어있으므로 처음 등장하는 위치와 마지막 등장하는 위치를 찾아
# def count_by_value(array,x):
#   n=len(array)

#   a=first(array,x,0,n-1)
#   if a==None:
#     return 0
#   b=last(array,x,0,n-1)
#   return b-a+1

# def first(array,target,start,end):
#   if start>end:
#     return None
#   mid=(start+end)//2
#   if (mid==0 or target>array[mid-1]) and array[mid]==target:
#     return mid
#   elif array[mid]>=target:
#     return first(array,target,start,mid-1)
#   else:
#     return first(array,target,mid+1,end)

# def last(array,target,start,end):
#   if start>end:
#     return None
#   mid=(start+end)//2
#   if (mid==0 or target<array[mid+1]) and array[mid]==target:
#     return mid
#   elif array[mid]>target:
#     return last(array,target,start,mid-1)
#   else:
#     return last(array,target,mid+1,end)

# n,x=map(int,input().split())
# data=list(map(int,input().split()))
# count=count_by_value(data,x)

# if count==0:
#   print(-1)
# else:
#   print(count)

#책풀이 2: bisect 간단하게 특정값을 가지는 원소의 개수를 구하는 것이므로
from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
  right_index=bisect_right(array,right_value)
  left_index=bisect_left(array,left_value)
  return right_index-left_index

n,x=map(int,input().split())
data=list(map(int,input().split()))
count=count_by_range(data,x,x)
if count==0:
  print(-1)
else:
  print(count)