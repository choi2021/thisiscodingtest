#1.균형잡인 문자열과 올바른 문자열을 확인하는 함수
#2.각 조건에 맞게 구성하기

def check_right_str(str):
  stack=[]
  for i in str:
    if i=="(":
      stack.append(i)
    else:
      if len(stack)==0:
        return False
      else:  
        stack.pop()
  return len(stack)==0

def check_balanced_str(str):
  num=0
  for i in str:
    if i=="(":
      num+=1
    else:
      num-=1
  return num==0

def solution(p):
  if p=="" or check_right_str(p):
    return p
  
  for i in range(1,len(p)+1):
    u=p[:i]
    v=p[i:]
    if check_balanced_str(u)==False or check_balanced_str(v)==False:
      continue
    if check_right_str(u)==True:
      return u+solution(v)
    else:
      str="("
      str+=solution(v)
      str+=")"
      deleted_u=u[1:len(u)-1]
      for i in range(len(deleted_u)):
        if deleted_u[i]==")":
          str+="("
        else:
          str+=")"
      return str

print(solution("()))((()"))

# 책풀이:

def balanced_index(p):
  count=0
  for i in range(len(p)):
    if p[i]=="(":
      count+=1
    else:
      count-=1
    if count==0:
      return i

def check_proper(p):
  count=0
  for i in p:
    if i=="(":
      count+=1
    else:
      if count==0:
        return False
      count-=1
  return True

def solution(p):
  answer=""
  if p=="":
    return answer
  index=balanced_index(p)
  u=p[:index+1]
  v=p[index+1:]
  if check_proper(u):
    answer=u+solution(v)
  else:
    answer="("
    answer+=solution(v)
    answer+=")"
    u=list(u[1:-1])
    for i in range(len(u)):
      if u[i]=="(":
        u[i]=")"
      else:
        u[i]="("
    answer+="".join(u)
  return answer