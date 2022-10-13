n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
target=list(map(int,input().split()))

def binary_sort(arr,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if arr[mid]==target:
      return 1
    elif arr[mid]<target:
      start=mid+1
    else:
      end=mid-1
  return 0

for i in target:
  print(binary_sort(arr,i,0,len(arr)-1))
