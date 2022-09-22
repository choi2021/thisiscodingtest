# 내풀이
# 1. 각 단어의 길이가 100000이하니까 순회하면서 ?를 찾는 부분을 하는데 최대 O(nlogn)으로 짜야해
# 2. words를 정렬하고 길이 먼저 비교하고, # - 1. 둘의 길이가 같아야해
# - 2. words
# - 4. 비교한 query는 dp에 저장해서 값을 저장해

# 문자열 크기비교: 대문자<소문자
# 생각은 잘했는데 접두사로 들어오면 문자열을 거꾸로 해줄 생각을 못했어


# from bisect import bisect_left,bisect_right

# words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
# words.sort(key=lambda x:(len(x),x,))

# queries=["fro??", "????o", "fr???", "fro???", "pro?"]


# n=len(queries)
# resulst=[-1]*(n)

# print("frost"<"fro???")
# print(words)
# for query in queries:
#   smallest_str=query.replace("?","A")
#   largest_str=query.replace("?","x")
#   small_start=0
#   small_end=len(words)-1
#   small_result=0
#   while small_start<=small_end:
#     small_result=(small_start+small_end)//2
#     value=words[small_result]
#     if len(value)==len(query):
#       if words[small_result]<smallest_str:
#         small_start=small_result+1
#       elif words[small_result]>smallest_str:
#         small_end=small_result-1
#     elif len(query)>len(value):
#       small_start=small_result+1
#     else:
#       small_end=small_result-1
#   large_start=0
#   large_end=len(words)-1
#   large_result=0
#   while large_start<=large_end:
#     large_result=(large_start+large_end)//2
#     value=words[large_result]
#     if len(value)==len(query):
#       if words[large_result]<largest_str:
#         large_start=large_result+1
#       elif words[large_result]>largest_str:
#         large_end=large_result-1
#     elif len(query)>len(value):
#       large_start=large_result+1
#     else:
#       large_end=large_result-1
#   print(small_result,large_result)


# 책풀이

from bisect import bisect_left,bisect_right


def count_by_range(a,left_value,right_value):
  right_index=bisect_left(a,right_value)
  left_index=bisect_right(a,left_value)
  return right_index-left_index

array=[[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]

def solution(words,queries):
  answer=[]
  for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].appned(word[::-1]) #뒤집어서 넣기

  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()
  
  for q in queries:
    if q[0]!="?":
      res=count_by_range(array[len[q],q.replace("?","a"),q.replace("?","z")])
    else:
      res=count_by_range(reversed_array[len(q)],q[::-1].replace("?","a"),q[::-1].replace("?","z"))
    answer.append(res)
  
  return answer