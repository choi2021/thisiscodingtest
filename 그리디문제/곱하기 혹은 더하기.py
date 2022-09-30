# 내풀이: 0,1이면 더하기, 2부터는 곱하는게 더 크게 만들 수 있어
# 나는 들어오는 수만 고려했어

str=input()
result=0
for i in str:
  num=int(i)
  if result==0 or num<=1:
    result+=num
  else:
    result*=num
print(result)

#책풀이:
data=input()
result=int(data[0])
for i in range(1,len(data)):
  num=int(data[i])
  if num<=i or result<=i:
    result+=num
  else:
    result*=num
print(result)