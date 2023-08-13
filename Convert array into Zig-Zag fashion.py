def zigzag(l):
    for i in range(1, len(l)):
        if i % 2 == 1 and l[i] < l[i - 1]:
            l[i], l[i - 1] = l[i - 1], l[i]
        elif i % 2 == 0 and l[i] > l[i - 1]:
            l[i], l[i - 1] = l[i - 1], l[i]
    print(l)


zigzag([9, 7, 8, 0, 6, 3, 5, 4, 2, 1])
zigzag([9, 7, 8, 0, 6, 3, 5, 4, 2])
zigzag([9, 7, 8, 0, 6, 3, 2, 1])
zigzag([97, 6, 3, 5, 4, 2, 1])
zigzag([4, 3, 7, 8, 6, 2, 1])
