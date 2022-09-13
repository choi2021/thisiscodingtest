s=input()
zero_group=s.split("1")
zero_group=" ".join(zero_group).split()
one_group=s.split("0")
one_group=" ".join(one_group).split()


result=min(len(zero_group),len(one_group))
print(result)

# 풀이

data=input()
count0=0
count1=0

if data[0]=="1":
  count0+=1
else:
  count1+=1

for i in range(len(data)-1):
  if data[i]!=data[i+1]:
    if data[i+1]=="1":
      count0+=1
    else:
      count1+=1

print(min(count0,count1))