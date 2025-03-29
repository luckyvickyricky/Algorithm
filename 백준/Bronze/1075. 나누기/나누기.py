N = int(input())
F = int(input())
N = N - (N % 100)
cnt = 0
while N % F != 0:
    cnt += 1
    N += 1

if cnt // 10 == 0:
    print(f"0{cnt}")
else:
    print(f"{cnt}")
