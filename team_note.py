def rotate_a_matrix_by_90_degree(a):
  n=len(a)
  m=len(a[0])
  result=[[0]*n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1]=a[i][j]
  return result

#원형으로 문제가 나오면 2배하고 일자로 바꿔버리기

#그래프에서 대각선 좌표는 (x,y) (a,b)일때, abs(y-b)==abs(x-a)

