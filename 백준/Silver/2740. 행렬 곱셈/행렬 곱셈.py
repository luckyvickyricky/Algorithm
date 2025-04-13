N1, M1 = map(int, input().split())

l1 = []

for _ in range(N1):
    l = list(map(int, input().split()))
    l1.append(l)


N2, M2 = map(int, input().split())

l2 = []

for _ in range(N2):
    l = list(map(int, input().split()))
    l2.append(l)


# matmul
l2_T = [list(x) for x in zip(*l2)]

for i in l1:
    for j in l2_T:
        ele = 0
        for idx in range(M1):
            ele += i[idx] * j[idx]
        print(ele, end=" ")

    print()
