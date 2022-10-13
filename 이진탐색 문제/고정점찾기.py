n=int(input())
arr=list(map(int,input().split()))

def binary_search(arr,start,end):
  while start<=end:
    mid=(start+end)//2
    if arr[mid]==mid:
      return mid
    elif arr[mid]<mid:
      start=mid+1
    else:
      end=mid-1
  return -1


print(binary_search(arr,0,len(arr)-1))