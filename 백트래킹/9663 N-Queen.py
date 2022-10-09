n=int(input())

rows=[0]*n

def promising(x):
  for i in range(x):
    if rows[i]==rows[x] or abs(i-x)==abs(rows[i]-rows[x]):
      return False
  return True

result=0
def put_queens(x):
  global result
  if x==n:
    result+=1
    return
  for i in range(n):
    rows[x]=i
    if promising(x):
      put_queens(x+1)

put_queens(0)
print(result)