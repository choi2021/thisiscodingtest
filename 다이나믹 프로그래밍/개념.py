# 동적 계획법

# 예시 1. 피보나치 수열
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1)+fibo(x-2)

print(fibo(3))

d=[0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x]=fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(99))

d=[0]*100

# def pibo(x):
#   print("f("+str(x)+")", end=" ")
#   if x==1 or x==2:
#     return 1;
#   if d[x]!=0:
#     return d[x]
#   d[x]=pibo(x-1)+pibo(x-2)
#   return d[x]

# pibo(6)

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]

print(d[n])