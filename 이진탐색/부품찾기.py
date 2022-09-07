import sys

#풀이 1: 이진탐색

# N=int(input())
# items=list(map(int,sys.stdin.readline().rstrip().split()))

# M=int(input())
# orders=list(map(int,sys.stdin.readline().rstrip().split()))

# def binary_search(array,target,start,end):
#   if start>end:
#     return "no"
#   mid=(start+end)//2
#   if array[mid]==target:
#     return "yes"
#   if array[mid]>target:
#     return binary_search(array,target,start,mid-1)
#   elif array[mid]<target:
#     return binary_search(array,target,mid+1,end)

# def binary_search(array,target,start,end):
#   while start<=end:
#     mid=(start+end)//2
#     if array[mid]==target:
#       return "yes"
#     elif array[mid]>target:
#       end=mid-1
#     else:
#       start=mid+1
#   return "no"

# items.sort()

# for order in orders:
#   result=binary_search(items,order,0,N-1);
#   print(result,end=" ")

# 풀이 2: 계수정렬
# n=int(input())
# array=[0]*1000001

# for i in list(map(int,sys.stdin.readline().rstrip().split())):
#   array[i]+=1

# m=int(input())
# x=list(map(int,input().split()))

# for i in x:
#   if array[i]!=0:
#     print("yes",end=" ")
#   else:
#     print("no", end=" ")

# 풀이 3: 집합이용

n=int(input())
array=set(map(int,input().split()))

m=int(input())
x=list(map(int,input().split()))

for i in x:
  if i in array:
    print("yes",end=" ")
  else:
    print("no",end=" ")