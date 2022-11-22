class Solution:
    def isValidSudoku(self, A):
        # Row checking
        for i in range(9):
            dic = {}
            count = 0
            for j in range(9):
                if A[i][j] in dic:
                    return 0
                if A[i][j] != ".":
                    dic[A[i][j]] = 1

        #checking Column
        for i in range(9):
            dic = {}
            count = 0
            for j in range(9):
                if A[j][i] in dic:
                    return 0
                if A[j][i] != ".":
                    dic[A[j][i]] = 1

        #checking each box
        # Remember:
            # After completing each iteration we have to jump 3 to next box which
            # is there index away. That’s why increasing i and j value by 3
        for i in range(0,9,3):
            for j in range(0,9,3):
                dic = {}
                for k in range(3):
                    for l in range(3):
                        Newi = i+k      #The new box row
                        Newj = j+l      # The new box column
                        if A[Newi][Newj] in dic:
                            return 0
                        elif A[Newi][Newj] != ".":
                            dic[A[Newi][Newj]] = 1
        return 1