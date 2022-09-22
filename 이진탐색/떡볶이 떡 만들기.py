#1.N과 M의 크기가 엄청커=> 이진탐색을 이용하자
#2. H가 될수 있는 건 0부터 떡의 최대길이까지
#3. H가 작을수록 떡양은 많아지고, H가 길수록, 떡양이 작아져
N,M=map(int,input().split())
data=list(map(int,input().split()))




# def cut_rice_cake(target,start,end):
#   if start>end:
#     return None
#   mid=(start+end)//2
#   total=0
#   for i in data:
#     cutted=i-mid
#     if cutted<=0:
#       continue
#     total+=cutted
#   if total==target:
#     return mid
#   elif total>target:
#     return cut_rice_cake(target,mid+1,end)
#   else:
#     return cut_rice_cake(target,start,mid-1)

# result=cut_rice_cake(M,0,max(data))
# if result==None:
#   print(-1)
# else:
#   print(result)


start=0
end=max(data)
result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in data:
    if x>mid:
      total+=x-mid
  if total<M:
    end=mid-1
  else:
    result=mid
    start=mid+1

