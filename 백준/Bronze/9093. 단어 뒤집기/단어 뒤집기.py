
tc = int(input())

for _ in range(tc):
    s = input().split()
    r_s = [w[::-1] for w in s]
    print(' '.join(r_s))