from collections import deque

N = int(input())

cnt = 0


for _ in range(N):
    s = input()

    # 홀수 패스
    if len(s) % 2 == 1:
        continue

    stack = deque()
    for i in s:
        # stack 비면 넣기
        if not stack:
            stack.append(i)

        # stack check
        else:
            # 다르면 넣어
            if stack[-1] == i:
                stack.pop()
                
            # 같으면 빼
            else:
                stack.append(i)

    if not stack:
        cnt += 1


print(cnt)
