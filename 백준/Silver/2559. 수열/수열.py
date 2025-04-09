

N, K = map(int, input().split())


l = list(map(int, input().split()))

temp = sum(l[:K])
max_ = temp

for i in range(0, N - K):
    # print(i + K)
    temp -= l[i]
    temp += l[i + K]
    max_ = max(max_, temp)

print(max_)