import sys
input=sys.stdin.readline

for _ in range(int(input())):
	n, m = map(int, input().split())
	parent = [0] * (n + 1)

	for i in range(1, n + 1):
		parent[i] = i

	edges = []
	for _ in range(m):
		x, y = map(int, input().split())
		edges.append((x, y))

	print(n-1)