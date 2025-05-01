from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(R):
    global cnt
    visited[R] = cnt
    cnt += 1
    for x in sorted(link[R]):
        if not visited[x]:
            dfs(x)


N, M, R = map(int, input().split())

link = defaultdict(list)
visited = [0] * (N + 1)

# print(visited)

for _ in range(M):
    s, e = map(int, input().split())
    link[s].append(e)
    link[e].append(s)


# 순서 표현.........
cnt = 1
dfs(R)

for i in range(1, N + 1):
    print(visited[i])
