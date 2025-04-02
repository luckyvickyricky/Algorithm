a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# a1 == 0일때도 처리해야 함
if a1 == 0:
    print(1)
elif a1 * n0 + a0 <= c * n0 and a1<= c:
    print(1)
else:
    print(0)
