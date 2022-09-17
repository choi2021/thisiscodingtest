s=input()
sum=0
result=[]

for i in s:
  if i.isalpha(): #알파벳인지 확인
    result.append(i)
  else:
    sum+=int(i)

result.sort()

if sum!=0:
  result.append(str(sum))

print("".join(result))  