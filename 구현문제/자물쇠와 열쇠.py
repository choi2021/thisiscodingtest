#내풀이: n과 m이 20이하이므로 전체경우를 다 확인해봐도 가능해
#key를 돌릴때마다 전체를 이동시키면서 값을 확인해
#생각은 잘했는데 막혀버렸어.. 다시 시도하자

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def rotated(a):
  n = len(a)
  m = len(a[0])
  result = [[0]* n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

def check_graph(graph):
  length=len(graph)//3
  for i in range(length,2*length):
    for j in range(length,2*length):
      if graph[i][j]!=1:
        return False
  return True




def solution(key, lock):
  n=len(lock)
  m=len(key)
  graph=[[0]*3*n for i in range(3*n)]


  for i in range(n):
    for j in range(n):
      graph[n+i][n+j]=lock[i][j]

  for direction in range(4):
    key=rotated(key)
    for x in range(2*n):
      for y in range(2*n):
        for i in range(m):
          for j in range(m):
            graph[x+i][y+j]+=key[i][j]

        if check_graph(graph)==True:
          return True

        for i in range(m):
          for j in range(m):
            graph[x+i][y+j]-=key[i][j]

  return False

print(solution(key,lock))