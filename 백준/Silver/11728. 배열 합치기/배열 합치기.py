N, M = map(int, input().split())

a = list()
for _ in range(2):
    l = list(map(int, input().split()))
    a.extend(l)

for i in sorted(a):
    print(i, end=' ')