n=int(input())
cards=list(map(int,input().split()))
m=int(input())
target_cards=list(map(int,input().split()))

deck={}
for i in target_cards:
  deck[i]=0
  
for i in cards:
  deck[i]=1
  
for card in target_cards:
  if deck[card]==1:
    print(1, end=" ")
  else:
    print(0, end=" ")