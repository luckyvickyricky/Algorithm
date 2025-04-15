N = int(input())

c = 1
while True:
    if (c+1)*(c+2) > 2*N:
        break
    c += 1

print(c)