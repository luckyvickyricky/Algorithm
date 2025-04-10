def fibo(N):
    l = [0] * (N + 2)
    l[0] = 1
    l[1] = 1

    for i in range(2, N + 1):
        l[i] = (l[i - 1] + l[i - 2]) % 15746
    return l[N]


N = int(input())
print(fibo(N))