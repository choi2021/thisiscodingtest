from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(graph, x, y, visited):
	q = deque([(x, y)])
	visited[x][y] = True
	graph[x][y] = 0
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m:
				if graph[nx][ny] == 1 and not visited[nx][ny]:
					graph[nx][ny] = 0
					visited[nx][ny] = True
					q.append((nx, ny))



t = int(input())

for _ in range(t):
	m, n, k = map(int, input().split())
	graph = [[0] * m for i in range(n)]
	visited = [[False] * m for i in range(n)]
	for _ in range(k):
		a, b = map(int, input().split())
		graph[b][a] = 1

	count = 0

	for i in range(n):
		for j in range(m):
			if graph[i][j] == 1:
				count += 1
				bfs(graph, i, j, visited)

	print(count)
