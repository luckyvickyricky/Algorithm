def sol(n):

    for i in range(n // 5, -1, -1):
        least = N - i * 5
        if least == 0 or least % 2 == 0:
            return i + least // 2

    return -1


N = int(input())
print(sol(N))