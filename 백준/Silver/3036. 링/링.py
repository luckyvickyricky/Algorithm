from collections import deque

n = int(input())

l = deque(map(int, input().split()))

# print(l)

t = l.popleft()

while l:
    b = l.popleft()
    a = t
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
    print(f"{a}/{b}")
