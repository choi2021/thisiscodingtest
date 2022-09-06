# 선택정렬

from re import L


array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index=i
  for j in range(i+1,len(array)):
    if array[min_index]>array[j]:
      min_index=j
  array[i],array[min_index]=array[min_index], array[i] # 스와프

print(array)

# 스와프

array=[3,5]
array[0],array[1]=array[1],array[0]

print(array)


# 삽입정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1): #인덱스를 i부터 감소하는 방법
    if array[j]<array[j-1]:
      array[j],array[j-1]=array[j-1],array[j]
    else:
      break
print(array)

#퀵정렬
array=[5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array,start,end):
#   if start>=end:
#     return
#   pivot=start
#   left=start+1
#   right=end
#   while left<=right:
#     while left<=end and array[left]<=array[pivot]:
#       left+=1
#     while right>start and array[right]<=array[pivot]:
#       right-=1
#     if left>right:
#       array[right],array[pivot]=array[pivot],array[right]
#     else:
#       array[left],array[right]=array[right],array[left]
# quick_sort(array,0,len(array)-1)
# print(array)

array=[5,7,9,0,3,1,6,2,4,8]

#파이썬의 장점을 살린 퀵정렬
def quick_sort_py(array):
  if len(array)<=1:
    return array
  pivot=array[0]
  tail=array[1:]

  left_side=[x for x in tail if x<=pivot]
  right_side=[x for x in tail if x>pivot]

  return quick_sort_py(left_side)+[pivot]+quick_sort_py(right_side)

print(quick_sort_py(array))

# 계수 정렬

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count=[0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=" ")

# 파이썬의 라이브러리

array=[7,5,9,0,3,1,6,2,4,8]
# result=sorted(array)
# print(result)

array.sort()
print(array)

array=[("바나나",2),("사과",5),("당근",3)]
def setting(data):
  return data[1]

result=sorted(array,key=setting)
print(result)