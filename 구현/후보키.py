relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations



def solution(relation):
  length=len(relation[0])
  data=[i for i in range(length)]
  answers=[]
  for i in range(1,length+1):
    for j in list(combinations(data,i)):
      arr=[]
      for person in relation:
        p=[]
        for idx in j:
          p.append(person[idx])
        if p not in arr:
          arr.append(p)
      if len(arr)==len(relation):
        answers.append(j)

  arr=set(answers)
  for i in range(len(answers)):
    for j in range(i+1,len(answers)):
      if len(answers[i])==len(set(answers[i])&set(answers[j])):
        arr.discard(answers[j])

  return len(arr)

print(solution(relation))

# from itertools import combinations

# def solution(relation):
#   row=len(relation)
#   col=len(relation[0])

#   candidates=[]
#   for i in range(1,col+1):
#     candidates.extend(combinations(range(col),i))
  
#   unique=[]
#   for candi in candidates:
#     tmp=[tuple([item[i] for i in candi]) for item in relation]
#     if len(set(tmp))==row:
#       unique.append(candi)
  
#   answer=set(unique)
#   for i in range(len(unique)):
#     for j in range(i+1,len(unique)):
#       if len(unique[i])==len(set(unique[i])&set(unique[j])):
#         answer.discard(unique[j])

#   return len(answer)