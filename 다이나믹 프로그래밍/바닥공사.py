N=int(input())
d=[0]*1000
d[0]=1
d[1]=3

for i in range(2,N):
  d[i]=d[i-2]*2+d[i-1]

print(d[N-1]%796796)