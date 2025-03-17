import math

n = int(input())
e = 0
sum = 0
cnt = 0

    
for s in range(1, n+1):
    while sum < n :
        if e > n :
            break
        sum += e+1
        e += 1
    if sum == n:
        cnt += 1
    sum -= s
print(cnt)