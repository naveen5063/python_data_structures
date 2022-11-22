class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        rows = len(A)
        columns = len(B[0])
        matrix = [[0 for column in range(len(B[0]))] for row in range(len(A))]
        for i in range(rows):
            print("i loop")
            for j in range(columns):
                print("j loop")
                for k in range(len(B)):
                    print("ik", i, k, A[i][k])
                    print("kj", k, j, B[k][j])
                    #print("A[i][k]", A[i][k])
                    #print("B[k][j]",  B[k][j])
                    #print("A[i][k] * B[k][j]", A[i][k] * B[k][j])
                    matrix[i][j] += A[i][k] * B[k][j]
                    print('matrix[i][j]', matrix[i][j], A[i][k] * B[k][j])
            print("matrix", matrix)
        return matrix


# A = [[1, 2] B = [[5, 6]
#      [3, 4]]     [7, 8]]

A = [[1, 2], [3, 4]]











B = [[5, 6], [7, 8]]

A = [
  [62, -37, -49, 18, -53, 14, 51],
  [62, -52, -11, -21, -62, -44, -95],
  [20, 78, -29, -49, -17, 21, 83],
  [-99, -69, -39, -47, 19, -50, -90],
  [91, -96, 63, -23, 5, 94, 49],
  [17, 1, 16, 63, -78, -13, -100],
  [-7, 72, 16, 86, -53, 94, 85],
  [-82, 78, 96, -45, -42, 38, 34],
  [-88, 37, 12, 31, -91, 51, 23]
]
B = [
  [90, 68, 2, 54, -59],
  [78, -86, 8, -30, 24],
  [-92, 84, -62, 13, 2],
  [12, -73, -53, -91, -4],
  [74, 85, -51, -4, 37],
  [-30, -27, 10, -78, 29],
  [-96, 39, -42, 93, 78]
]


A =[
  [94, 91]
]
B = [
  [35, -52, -12, 26, -93, -61],
  [29, -20, -36, -9, 66, 15]
]
A = [[1, 2] ,
     [3, 4]]

B = [[5, 6],
    [7, 8]]
#[-1820 -926 2613 6046 -2293 ] [8136 1510 8215 1521 -15824 ] [108 -2982 2650 8971 7284 ] [278 -1188 6470 -4052 -3472 ] [-12524 21213 -4646 7911 -722 ] [5110 -12364 3759 -12611 -12262 ] [-10356 -15330 -4915 -9371 9224 ] [-18180 -4205 -2013 -1059 9282 ] [-16238 -18636 1918 -10002 5886 ]
s = Solution()
print(s.solve(A, B))