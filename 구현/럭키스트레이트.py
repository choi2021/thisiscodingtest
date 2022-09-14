# N=input()
# half=len(N)//2
# if sum(list(map(int,N[:half])))==sum(list(map(int,N[half:]))):
#   print("LUCKY")
# else:
#   print("READY")

# 책풀이: 반으로 나누는 것은 같지만 값이 같다는 것을 각자리 숫자를 더하고 빼는 로직으로 구현했어
n=input()
length=len(n)
summary=0

for i in range(length//2):
  summary+=int(n[i])

for i in range(length//2,length):
  summary-=int(n[i])

if summary==0:
  print("LUCKY")
else:
  print("READY")
