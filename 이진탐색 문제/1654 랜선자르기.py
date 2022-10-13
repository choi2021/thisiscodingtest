n,c=map(int,input().split())
arr=[]
for i in range(n):
  arr.append(int(input()))
arr.sort()

def binary_search(arr,start,end):
  num=2
  max_dist=end-start
  while start<=end and num<c:
    mid=(start+end)//2
    max_dist=min(arr[mid]-arr[start],arr[end]-arr[mid],max_dist)
    num+=1
    if max_dist==arr[mid]-arr[start]:
      start=mid+1
    elif max_dist==arr[end]-arr[mid]:
      end=mid-1
  return max_dist

print(binary_search(arr,0,len(arr)-1))
    
      