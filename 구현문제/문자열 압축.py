# 내풀이
# 1. 전체 자를수 있는 길이는 len//2로 두고 자른 애들끼리 비교해서 stack에 넣어
# 2. 스택의 마지막 값과 같으면 value를 올려, 다르면 pop()하고 count를 더해서 문자열에 더해주기


from bz2 import compress
from multiprocessing.connection import answer_challenge


def solution(s):
    result=[]
    if len(s)==1:
        return 1
    for split_length in range(1,len(s)//2+1):
        arr=[s[i:i+split_length] for i in range(0, len(s), split_length) ]
        stack=[arr[0]]
        last_str=""
        count=1
        for i in range(1,len(arr)):
            if stack[-1]==arr[i]:
                count+=1
            else:
                string=stack.pop()
                if count==1:
                    last_str+=string
                else: 
                    last_str+=str(count)+string
                stack.append(arr[i])
                count=1

        string=stack.pop()
        if count==1:
            last_str+=string
        else: 
            last_str+=str(count)+string
        result.append(last_str)
        
    result.sort(key=lambda x:len(x))
    return len(result[0])


#책풀이:

def solutions(s):
  answer=len(s)
  for step in range(1,len(s)//2+1):
    compressed=""
    prev=s[0:step]
    count=1
    for j in range(step,len(s),step):
      if prev==s[j:j+step]:
        count+=1
      else:
        compressed+=str(count)+prev if count>=2 else prev
        prev=s[j:j+step]
        count=1
    compressed+=str(count)+prev if count>=2 else prev
    answer=min(answer,len(compressed))
  return answer