def booleanMatrix(matrix):
    r = set()
    c = set()
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                r.add(i)
                c.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in r or j in c:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0


r, c = map(int, input().strip().split())
matrix = []
for i in range(r):
    line = [int(x) for x in input().strip().split()]
    matrix.append(line)
booleanMatrix(matrix)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()
