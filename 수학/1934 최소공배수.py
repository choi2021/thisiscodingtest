t=int(input())

def common_deno(x,y):
  for i in range(min(x,y),1,-1):
    if x%i==0 and y%i==0:
      return i
  return 1

for i in range(t):
  a,b=map(int,input().split())
  common=common_deno(a,b)
  print(common*(a//common)*(b//common))
