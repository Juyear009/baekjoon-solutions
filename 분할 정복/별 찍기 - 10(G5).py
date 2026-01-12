def star(n):
    if n == 1:
        return ["*"]

    prev = star(n // 3)
    res = []

    for i in range(3):
        for line in prev:
            if i == 1:
                res.append(line + " " * (n // 3) + line)
            else:
                res.append(line * 3)

    return res


N = int(input())
print("\n".join(star(N)))
