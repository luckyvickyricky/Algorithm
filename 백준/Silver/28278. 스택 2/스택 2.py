from collections import deque
import sys

input = sys.stdin.readline


TC = int(input())


que = deque()
for _ in range(TC):
    a = input()
    if len(a) > 2:
        a, b = map(int, a.split())
        que.append(b)
        continue

    a = int(a)

    if a == 2:
        if que:
            print(que.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(que))
    elif a == 4:
        if que:
            print(0)
        else:
            print(1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)
