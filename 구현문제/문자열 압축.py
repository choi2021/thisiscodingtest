# # 내풀이
# # 1. 알맞게 문자열 자르기
# #   자를때 최소 1개부터 최대 전체 갯수의 반만큼 잘라
# # 2. 이전값과 값다면 합쳐주기
# # 3. result값중에서 가장 작은 길이 반환하기

# # 테스트에서 실패했어 

# s=input()
# result=[]

# for i in range(1,len(s)//2+1):
#   ord=i;
#   reformed_s=[]
#   target=""
#   for j in range(1,len(s) +1):
#     if j%ord==0:
#       target+=s[j-1]
#       reformed_s.append(target)
#       target=""
#     else:
#       target+=s[j-1]

#   num=1
#   string=""
#   prev=reformed_s[0]
#   for k in range(1,len(reformed_s)):
#     if prev==reformed_s[k]:
#       num+=1
#     else:
#       string+=str(num)+prev if num>1 else prev
#       prev=reformed_s[k]
#       num=1
#   string+=str(num)+prev if num>1 else prev
#   result.append(string)


#책풀이
def solutions(s):
  answer=len(s)
  for step in range(1,len(s)//+1):
    compressed=""
    prev=s[0:step]
    count=1
    for j in range(step,len(s),step): #숫자의 간격설정가능
      if prev==s[j:j+step]:
        count+=1
      else:
        compressed+=str(count)+prev if count>1 else prev
        prev=s[j:j+step]
        count=1
    compressed+=str(count)+prev if count>1 else prev
    answer=min(answer,len(compressed))
  return answer
print(solutions("aabbaccc"))

