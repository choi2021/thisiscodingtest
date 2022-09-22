# 내풀이
# 1. 타겟 금액을 만들기 위해서 최소 값들을 만들어가
# 2. 못만드는 금액은 -1으로, 타겟 최소개수=타겟금액에서 화폐금액을 뺀 금액의 최소갯수+1

n,m=map(int,input().split())
coins=[]
for _ in range(n):
  coins.append(int(input()))

money=[-1]*(100)
for coin in coins:
  money[coin]=1

for i in range(min(coins),m+1):
  for coin in coins:
    if i-coin<0:
      continue
    elif i-coin==0:
      money[i]=1
    else:
      money[i]=money[i-coin]+1




print(money[m])