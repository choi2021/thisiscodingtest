#내풀이
#1.문자열 길이체크, 길이 같을 때까지 삽입 또는 삭제
#2.같은부분 체크해서 가장 많은 경우에 다른 부분 카운트

# a=input()
# b=input()

# length_a=len(a)
# length_b=len(b)

# def check_common(a,b):
#   num=0
#   for i in range(len(a)):
#     if a[i]==b[i]:
#       num+=1
#   return num


# if length_a>length_b:
  
# elif length_a<length_b:

# else:

#책풀이: 이차원 배열을 이용한 DP

def edit_dist(str1,str2):
  n=len(str1)
  m=len(str2)

  dp=[[0]*(m+1) for _ in range(n+1)]

  for i in range(1,n+1):
    dp[i][0]=i
  for j in range(1,m+1):
    dp[0][m]=j
  
  for i in range(1,n+1):
    for j in range(1,m+1):
      if str[i-1]==str[j-1]:
        dp[i][j]=dp[i-1][j-1]
      else:
        dp[i][j]=1+min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
  
  return dp[n][m]