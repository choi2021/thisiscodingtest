# 내풀이: 0,1이면 더하기, 2부터는 곱하는게 더 크게 만들 수 있어

str=input()
result=0
for i in str:
  num=int(i)
  if result==0 or num<=1:
    result+=num
  else:
    result*=num
print(result)
