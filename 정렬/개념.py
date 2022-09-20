# 선택정렬=가장 작은 데이터를 제일 앞과 바꿔
from turtle import right


array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
  min_index=i
  for j in range(i+1,len(array)):
    if array[min_index]>array[j]:
      min_index=j
  array[i],array[min_index]=array[min_index],array[i]

# 삽입정렬=어느정도 정렬되어있을때 좋은 알고리즘, 앞선 데이터들이 정렬되어있다는 가정으로 비교해서 작으면 앞으로 넣어줘, O(N^2)이지만 최선은 O(N)
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1]=array[j-1],array[j]
    else:
      break


# 퀵정렬=피봇을 설정하고 피봇을 기준으로 큰 데이터들과 작은 데이터들을 반복적으로 나눠

array=[7,5,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
  if start>=end:
    return
  pivot=start
  left=start+1
  right=end
  while left<=right:
    while left<=end and array[left]<=array[pivot]:
      left+=1
    while right>start and array[right]>=array[pivot]:
      right-=1
    if left>right:
      array[right],array[pivot]=array[pivot],array[right]
    else:
      array[left],array[right]=array[right],array[left]
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

def quick_sort_py(array):
  if len(array)<=1:
    return array
  pivot=array[0]
  tail=array[1:]
  left_side=[x for x in tail if x<=pivot]
  right_side=[x for x in tail if x>pivot]
  return quick_sort_py(left_side)+[pivot]+quick_sort_py(right_side)


# quick_sort(array,0,len(array)-1)
print(quick_sort_py(array))


#계수 정렬: 데이터 크기가 제한되어 정수형태로 표현할 수 있을 때
array=[7,5,9,0,3,1,6,2,4,8]
count=[0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=" ")

#파이썬 라이브러리
array=[7,5,9,0,3,1,6,2,4,8]
result=sorted(array)

array=[("바나나",2),("사과",5),("당근",3)]
def setting(data):
  return data[1]

result=sorted(array,key=setting)
print(result)