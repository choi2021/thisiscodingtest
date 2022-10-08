# 1. 중위 표기식에 맞게 괄호를 넣어줘
# 2. 괄호가 필요하다는 건 계산을 먼저 해줘야해 우선순위가 높아 먼저 나와줘야해
# 3. 
str=input()
result=""
stack=[]
for i in str:
  if i.isalpha():
    result+=i
  else:
    if i=="(":
      stack.append(i)
    elif i=="*" or i=="/":
      while stack and (stack[-1]=="*" or stack[-1]=="/"):
        result+=stack.pop()
      stack.append(i)
    elif i=="+" or i=="-":
      while stack and stack[-1]!="(":
        result+=stack.pop()
      stack.append(i)
    elif i==")":
      while stack and stack[-1] !="(":
        result+=stack.pop()
      stack.pop()
while stack:
  result+=stack.pop()

print(result)