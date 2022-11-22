# Function to run the Floyd–Warshall algorithm
def floydWarshall(adjMatrix):
    n = len(adjMatrix)
    cost = adjMatrix.copy()

    for v in range(n):
        for u in range(n):
            if adjMatrix[v][u] == -1:
                adjMatrix[v][u] = float('inf')

    # run Floyd–Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # print("cost[v][k] + cost[k][u] < cost[v][u]", cost[v][k] ,cost[k][u] , cost[v][u])
                # if cost[v][k] != -1 and cost[k][u] != -1: \
                # and (cost[v][k] + cost[k][u] < cost[v][u]):
                print("values", v, u, "--", v, k, "---", k, u)
                print("cost", cost[v][u], cost[v][k] + cost[k][u])
                cost[v][u] = min(cost[v][k] + cost[k][u], cost[v][u])
        print("cost", cost)

    # for v in range(n):
    #     for u in range(n):
    #         if cost[v][u] == float('inf'):
    #             cost[v][u] = -1
    return cost


if __name__ == '__main__':
    # define infinity
    I = float('inf')

    # given adjacency representation of the matrix
    adjMatrix = [
        [0, I, -2, I],
        [4, 0, 3, I],
        [I, I, 0, 2],
        [I, -1, I, 0]
    ]
    adjMatrix = [
        [0, 5, -1, 10],
        [-1, 0, 3, -1],
        [-1, -1, 0, 1],
        [-1, -1, -1, 0]
    ]
    # adjMatrix = [
    #     [0, 5, I, 10],
    #     [I, 0, 3, I],
    #     [I, I, 0, 1],
    #     [I, I, I, 0]
    # ]

    adjMatrix = [[0, 50, 39],
                 [I, 0, 1],
                 [I, 10, 0]]

    # Run Floyd–Warshall algorithm
    print(floydWarshall(adjMatrix))
