n,m=map(int,input().split())

def max_common(x,y):
  for i in range(min(x,y),1,-1):
    if x%i==0 and y%i==0:
      return i
  return 1

num=max_common(n,m)
print(num)
print(num*(n//num)*(m//num))