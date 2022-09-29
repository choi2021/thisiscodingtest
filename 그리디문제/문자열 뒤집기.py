s=input()
zero_count=0
one_count=0

current=s[0]
if current=="1":
  one_count+=1
else:
  zero_count+=1

for i in range(1,len(s)):
  if s[i]==current:
    continue
  else:
    if s[i]=="1":
      one_count+=1
    else:
      zero_count+=1
    current=s[i]

print(min(zero_count,one_count))

#책풀이:
data=input()
count0=0
count1=1

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

print(count0,count1)