tc = int(input())

for _ in range(tc):
    s = list(input().split())
    for w in s:
        c = len(w)

        for i in range(c - 1, -1, -1):
            print(w[i], end="")
        print(" ", end="")

    print()
