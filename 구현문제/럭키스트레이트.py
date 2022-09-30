n=input()

former=list(map(int,n[:len(n)//2]))
latter=list(map(int,n[len(n)//2:]))

if sum(former)==sum(latter):
  print("LUCKY")
else:
  print("READY")