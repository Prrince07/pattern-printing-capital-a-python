rows = 5
for i in range(rows):
    for j in range((rows - i) - 1):
        print(" ", end="")
    for k in range((2 * i) + 1):
        if k == 0 or k == (2 * i) or i == rows // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
