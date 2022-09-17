# key의 1인 부분과 자물쇠의 0인 부분이 일치해야해
# key는 이동과 회전이 가능하다. 이때 맞게 할때 자물쇠 영역 내에서는 모두 key의 모든 돌기가 자물쇠와 맞물려야해

# 1. key의 돌기 수가 자물쇠의 홈 수보다 작으면 무조건 false
# 2. key의 돌기 수가 자물쇠의 홈 수랑 같거나 크면 이동, 회전시켜서 맞춰줘야해
# 하다가 포기...

# def count_item(arr,target):
#   target_count=0
#   for i in arr:
#     target_count+=i.count(target)
#   return target_count

# def rotate_arr(arr):
#   N=len(arr)
#   ret=[[0]*N for _ in range(N)]

#   for r in range(N):
#     for c in range(N):
#       ret[c][N-1-r]=arr[r][c]
#   return ret

# def solution(key, lock):
#   key_count=count_item(key,1)
#   lock_count=count_item(lock,0)
#   if key_count<lock_count:
#     return False

#책풀이: 3*3에서 생각하는게 아니라 9*9에서 생각해봐

def rotate_a_matrix_by_90_degree(a):
  n=len(a)
  m=len(a[0])
  result=[[0]*n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1]=a[i][j]
  return result

def check(new_lock):
  lock_length=len((new_lock))//3
  for i in range(lock_length,lock_length*2):
    for j in range(lock_length,lock_length*2):
      if new_lock[i][j]!=1:
        return False
  return True

def solution(key,lock):
  n=len(lock)
  m=len(key)
  new_lock=[[0]*(n*3) for _ in range(n*3)]
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n]=lock[i][j]
  
  for rotation in range(4):
    key=rotate_a_matrix_by_90_degree(key)
    for x in range(n*2):
      for y in range(n*2):
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j]+=key[i][j]
        if check(new_lock)==True:
          return True
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j]-=key[i][j]
  return False

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))