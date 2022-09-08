N,M=list(map(int,input().split()))
money=[]

d=[-1]*10001

for i in range(N):
  money.append(int(input()))

for i in range(1,M+1):
    if min(money)>i:
      continue
    if i in money:
      d[i]=1
      continue
    min_val=10000
    for unit in money:
      if i-unit<0 or d[i-unit]<0:
        continue
      if d[i-unit]+1<min_val:
        min_val=d[i-unit]+1
    if min_val!=10000:
      d[i]=min_val

print(d[M])


