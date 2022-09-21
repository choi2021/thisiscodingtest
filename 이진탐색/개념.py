#순차탐색: 일일이 데이터를 비교하고 찾아, 시간만 충분하면 무조건 찾을 수 있어 O(N)


# def sequential_search(n,target,array):
#   for i in range(n):
#     if array[i]==target:
#       return i+1

# input_data=input().split()
# n=int(input_data[0])
# target=input_data[1]
# array=input().split()
# print(sequential_search(n,target,array))

#이진 탐색: 배열 내부가 정렬이 되어있어야해, O(logN)

def binary_search(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if array[mid]==target:
    return mid
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

n,target=list(map(int,input().split()))

array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)
if result==None:
  print("원소가 없습니다")
else:
  print(result)