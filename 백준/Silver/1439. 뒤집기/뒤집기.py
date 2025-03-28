a = input()
l = []
for i in a:
    if not l:
        l.append(i)
    elif l[-1] == i:
        continue
    else:
        l.append(i)

print(min(l.count("0"), l.count("1")))