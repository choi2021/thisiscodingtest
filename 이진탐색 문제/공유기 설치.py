import sys
input=sys.stdin.readline

n,c=map(int,input().split())
arr=[]
for i in range(n):
  arr.append(int(input()))
arr.sort()

def binary_search(start,end):
  result=0
  while start<=end:
    mid=(start+end)//2
    count=1
    value=arr[0]
    for i in range(1,n):
      if value+mid<=arr[i]:
        count+=1
        value=arr[i]

    if count>=c:
      result=mid      
      start=mid+1
    else:
      end=mid-1
  return result


print(binary_search(0,arr[-1]))