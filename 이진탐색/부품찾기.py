n=int(input())
store=list(map(int,input().split()))
store.sort()

m=int(input())
order=list(map(int,input().split()))

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target:
      return "yes"
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1
  return "no"

for i in range(m):
  print(binary_search(store,order[i],0,len(store)-1),end=" ")


n=int(input())
array=[0]*1000001

for i in input().split():
  array[int(i)]=1

m=int(input())
x=list(map(int,input().split()))

for i in x:
  if array[i]==1:
    print()