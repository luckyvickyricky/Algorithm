from collections import deque


def main():
    N = int(input())

    que = deque(map(int, input().split()))

    temp_stack = deque()
    temp_stack.append(que.popleft())
    result = deque([0])

    while True:
        need = result[-1] + 1

        if que and que[0] == need:
            result.append(que.popleft())
        elif temp_stack and temp_stack[-1] == need:
            result.append(temp_stack.pop())
        else:
            if que:
                temp_stack.append(que.popleft())

            else:
                return "Sad"

        if len(result) == N + 1:
            return "Nice"


print(main())
