from collections import deque
from copy import deepcopy

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
inputlist = [list(map(int, input().split())) for _ in range(n)]

for i, in_val in enumerate(inputlist):
	i += 1
	time[i] = in_val[0]
	for val in in_val[1:-1]:
		indegree[i] += 1
		graph[val].append(i)


def topology_sort():
	result = deepcopy(time)
	q = deque()

	for i in range(1, n + 1):
		if indegree[i] == 0:
			q.append(i)

	while q:
		now = q.popleft()
		for i in graph[now]:
			result[i] = max(result[i], result[now] + time[i])
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	for i in range(1, n + 1):
		print(result[i])


topology_sort()