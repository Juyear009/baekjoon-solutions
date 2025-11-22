temp = [input() for _ in range(6)]

if 5 <= temp.count("W") <= 6:
    print(1)
elif 3 <= temp.count("W") <= 4:
    print(2)
elif 1 <= temp.count("W") <= 2:
    print(3)
else:
    print(-1)