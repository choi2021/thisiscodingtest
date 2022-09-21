# N이 100만개이므로 이미 이진탐색을 이용해보자
# Orders를 target으로 삼는 이진탐색으로 결과를 리턴하기
# n=int(input())
# data=list(map(int,input().split()))
# data.sort()
# m=int(input())
# orders=list(map(int,input().split()))

# def binary_search(array,target,start,end):
#   if start>end:
#     return "no"
#   mid=(start+end)//2
#   if array[mid]==target:
#     return "yes"
#   elif array[mid]>target:
#     return binary_search(array,target,start,mid-1)
#   else:
#     return binary_search(array,target,mid+1,end)

# for order in orders:
#   print(binary_search(data,order,0,n-1))


# 책풀이 2. 계수 정렬
# n=int(input())
# array=[0]*(1000001)

# for i in input().split():
#   array[int(i)]=1

# m=int(input())
# x=list(map(int,input().split()))

# for i in x:
#   if array[i]==1:
#     print("yes")
#   else:
#     print("no")

# 책풀이 3.set
n=int(input())
array=set(map(int,input().split()))

m=int(input())
x=list(map(int,input().split()))

for i in x:
  if i in array:
    print("yes")
  else:
    print("no")