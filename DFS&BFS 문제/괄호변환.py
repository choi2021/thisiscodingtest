p="()))((()"

def balanced(p):
  num=0
  for i in range(len(p)):
    if p[i]==")":
      num-=1
    else:
      num+=1
    if num==0:
      return i

def proper(p):
  num=0
  for i in range(len(p)):
    if p[i]=="(":
      num+=1
    else:
      if num==0:
        return False
      num-=1
  return True


def solution(p):
  if p=="":
    return ""
  index=balanced(p)
  u=p[:index+1]
  v=p[index+1:]
  if proper(u):
    return u+solution(v)
  else:
    answer="("
    answer+=solution(v)
    answer+=")"
    u=u[1:-1]
    for i in u:
      if i==")":
        answer+="("
      else:
        answer+=")"
    return answer

print(solution(p))