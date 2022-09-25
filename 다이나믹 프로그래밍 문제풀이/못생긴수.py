#내풀이: 숫자를 증가시켜가면서 2,3,5나눠지고 값이 테이블에 있으면 추가해

# n=int(input())
# d=[1]

# num=2
# while len(d)<n:
#   if num%2==0 and num//2 in d:
#     d.append(num)
#     num+=1
#     continue
#   if num%3==0 and num//3 in d:
#     d.append(num)
#     num+=1
#     continue 
#   if num%5==0 and num//5 in d:
#     d.append(num)
#     num+=1
#     continue
#   num+=1

# print(d[n-1])

#책풀이: 인덱스를 증가시켜가면서 2,3,5를 차례로 곱해가
n=int(input())

ugly=[0]*n
ugly[0]=1

i2=i3=i5=0
next2,next3,next5=2,3,5

for i in range(1,n):
  ugly[i]=min(next2,next3,next5)
  if ugly[i]==next2:
    i2+=1
    next2=ugly[i2]*2
  if ugly[i]==next3:
    i3+=1
    next3=ugly[i3]*3
  if ugly[i]==next5:
    i5+=1
    next5=ugly[i5]*5

print(ugly[n-1])