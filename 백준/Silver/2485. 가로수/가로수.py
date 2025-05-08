import math

N = int(input())

l = []
l_gap = []

a = int(input())
l.append(a)
for _ in range(N - 1):
    b = int(input())
    l.append(b)
    l_gap.append(b - a)
    a = b

gcd = math.gcd(*l_gap)

ans = 0
for i in l_gap:
    ans += i // gcd - 1

print(ans)
