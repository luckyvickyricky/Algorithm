a = list()
# 입력
for _ in range(9):
    n = int(input())
    a.append(n)

diff = sum(a) - 100

for i in a[:]:
    j = diff - i
    if j in a[:] and i!=j:
        a.remove(i)
        a.remove(j)
        break

for i in a:
    print(i)