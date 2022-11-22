def UniquePathHelper(i, j, r, c, A, paths):
    # boundary condition or constraints
    if (i == r or j == c):
        return 0

    if (A[i][j] == 1):
        return 0

    # base case
    if (i == r - 1 and j == c - 1):
        print("base", i, r - 1, j, c - 1)
        return 1

    if (paths[i][j] != -1):
        return paths[i][j]

    return UniquePathHelper(i + 1, j, r, c, A, paths) + UniquePathHelper(i, j + 1, r, c, A, paths)


def uniquePathsWithObstacles(A):
    r, c = len(A), len(A[0])

    # create a 2D-matrix and initializing
    # with value 0

    paths = [[-1 for i in range(c)] for j in range(r)]
    print("paths", paths)

    return UniquePathHelper(0, 0, r, c, A, paths)


A = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(uniquePathsWithObstacles(A))
