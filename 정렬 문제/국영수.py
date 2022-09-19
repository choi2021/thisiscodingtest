#내풀이: 일일히 다해버림.. 파이썬 문법에 익숙해지자

# N=int(input())
# scores=[]

# for _ in range(N):
#   name,kr,en,math=input().split()
#   scores.append({"name":name,"kr":int(kr),"en":int(en), "math":int(math)})

# for i in range(N):
#   min_kr=i
#   for j in range(1,N): 

#     if scores[min_kr]["kr"]<scores[j]["kr"]:
#       scores[min_kr],scores[j]=scores[j],scores[min_kr]
#       min_kr=j
#     elif scores[i]["kr"]==scores[j]["kr"]:
#       if scores[i]["en"]<scores[j]["en"]:
#         scores[i],scores[j]=scores[j],scores[i]
#         continue
#       elif scores[i]["en"]==scores[j]["en"]:
#         if scores[i]["math"]>scores[j]["math"]:
#           scores[i],scores[j]=scores[j],scores[i]
#           continue
#         elif scores[i]["math"]==scores[j]["math"]:
#           arr=[scores[i]["name"],scores[j]["name"]]
#           arr.sort()
#           if arr[0]==scores[j]["name"]:
#             scores[i],scores[j]=scores[j],scores[i]
#             continue

# for score in scores:
#   print(score["name"])

# 책풀이


N=int(input())
scores=[]

for _ in range(N):
  scores.append(input().split())
scores.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for score in scores:
  print(score[0])