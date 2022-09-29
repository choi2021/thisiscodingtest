#내풀이
#1. 각 금액을 증가시켜가면서 못만드는 금액을 찾아
#2. 

from itertools import combinations

n=int(input())
coins=list(map(int,input().split()))
possible_num=[False]*(sum(coins)+1)
result=0

for i in range(1,n+1):
  for combi in list(combinations(coins,i)):
    possible_num[sum(combi)]=True

target=1
while True:
  if possible_num[target]==False:
    print(target)
    break
  target+=1