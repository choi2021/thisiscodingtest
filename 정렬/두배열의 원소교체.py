n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
num=0
while(num<k):
    if b[num]>a[num]:
      b[num],a[num]=a[num],b[num]
      num+=1
    else:
      break



print(sum(a))