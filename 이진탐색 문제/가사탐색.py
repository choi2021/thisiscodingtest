## 대문자가 소문자 보다 작아

from bisect import bisect_left, bisect_right

array=[[] for i in range(10001)]
reversed_array=[[] for i in range(10001)]
words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
words.sort(key=lambda x:[len(x),x])
queries=["fro??", "????o", "fr???", "fro???", "pro?"]

def count_by_range(arr,left,right):
  left_idx=bisect_left(arr,left)
  right_idx=bisect_right(arr,right) 
  print(left_idx,right_idx)
  return right_idx-left_idx

def solution(words,queries):
  answer=[]
  for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])
  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()
  
  for q in queries:
    if q[0]!="?":
      res=count_by_range(array[len(q)],q.replace("?","a"),q.replace("?","z"))
    else:
      res=count_by_range(reversed_array[len(q)],q[::-1].replace("?","a"),q[::-1].replace("?","z"))
    answer.append(res)
  return answer

print(solution(words,queries))