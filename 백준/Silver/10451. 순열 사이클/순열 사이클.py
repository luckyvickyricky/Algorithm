def recur(flag, now):
    visited[now] = 1
    now = d[now]
    if now == flag:
        return 1
    if not visited[now]:
        return recur(flag, now)


tc = int(input())

for _ in range(tc):
    N = int(input())
    l = list(map(int, input().split()))
    d = dict()
    for idx, i in enumerate(l):
        d[idx + 1] = i
    # {1: 3, 2: 2, 3: 7, 4: 8, 5: 1, 6: 4, 7: 5, 8: 6}
    cnt = 0
    visited = [0] * (N + 1)
    for now in range(1, N + 1):
        if not visited[now]:
            if recur(now, now) == 1:
                cnt += 1

    print(cnt)
