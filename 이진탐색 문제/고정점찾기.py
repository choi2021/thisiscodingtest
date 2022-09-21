# 내풀이: 난 다 찾아버렸어

n=int(input())
arr=list(map(int,input().split()))

start=0
end=n-1
result=-1
# def fixed_search(arr,start,end):
#   global result
#   if start>end:
#     return None
#   mid=(start+end)//2
#   if arr[mid]==mid:
#     result=mid
#   fixed_search(arr,start,mid-1)
#   fixed_search(arr,mid+1,end)



def fixed_search(arr,start,end):
  global result
  if start>end:
    return None
  mid=(start+end)//2
  if arr[mid]==mid:
    result=mid
  elif arr[mid]<mid:
    fixed_search(arr,mid+1,end)
  else:
    fixed_search(arr,start,mid-1)
fixed_search(arr,start,end)

print(result)