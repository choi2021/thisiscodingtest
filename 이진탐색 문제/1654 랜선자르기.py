#내풀이: 공유기 수를 늘려가면서 현재길이보다 긴쪽에서 쪼개서 만들어가

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
    

#책풀이: 간격을 기준으로 비교해
n,c=map(int,input().split())
arr=[]
for i in range(n):
  arr.append(int(input()))
arr.sort()

start=1
end=arr[-1]-arr[0]
result=0

while(start<=end):
  mid=(start+end)//2
  value=arr[0]
  count=1
  for i in range(1,n):
    if arr[i]>=value+mid:
      value=arr[i]
      count+=1
  if count>=c:
    start=mid+1
    result=mid
  else:
    end=mid-1