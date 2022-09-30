n,k=map(int,input().split())
count=0

while True:
  if n==1:
    break;
  if n%k==0:
    n//=k
    count+=1
    continue
  n-=1
  count+=1

print(count)

#책풀이: 일일이 빼게되면 시간초과가 발생할 수 있으므로, 나눠질때까지 빼주고 나눠
n,k=map(int,input().split())
result=0

while n>=k:
  while n%k!=0:
    n-=1
    result+=1
  n//=k
  result+=1

while n>1:
  n-=1
  result+=1

print(result)

n,k=map(int,input().split())
result=0

while True:
  target=(n//k)*k
  result+=(n-target)
  n=target
  if n<k:
    break
  result+=1
  n//=k