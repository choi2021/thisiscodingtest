# n=int(input())
# dp=[1]
# while len(dp)<1000:
#   temp=[]
#   for i in dp:
#     if i*2 not in dp and i*2 not in temp:
#       temp.append(i*2)
#     if i*3 not in dp and i*3 not in temp:
#       temp.append(i*3)
#     if i*5 not in dp and i*5 not in temp:
#       temp.append(i*5)
#   dp=dp+temp
# dp.sort()
# print(dp)
# print(dp[n-1])

#책풀이
n=int(input())
ugly=[0]*n
ugly[0]=1

i2=i3=i5=0
next2=next3=next5=2,3,5

for i in range(1,n):
  ugly[i]=min(next2,next3,next5)
  if ugly[i]==next2:
    i2+=1
    next2=ugly[i2]*2
  if ugly[i]==next3:
    i3+=1
    next3=ugly[i3]*3
  if ugly[i]==next5:
    i5+=1
    next5=ugly[i5]*5
