N=int(input())
data=[]
for _ in range(N):
  A,B=input().split()
  data.append((A,int(B)))

def score_sort(student):
  return student[1]

# data=sorted(data,key=score_sort)
data=sorted(data,key=lambda student:student[1]) #lambda함수 이용
for student in data:
  print(student[0],end=" ")