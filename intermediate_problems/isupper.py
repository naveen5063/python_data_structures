class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        res = []

        for i in range(0, len(A)):
            if 65 <= ord(A[i]) <= 91:
                res.append(A[i])
            elif 97 <= ord(A[i]) <= 122:
                print(A[i])
                val = ord(A[i]) - 32
                res.append(chr(val))
            else:
                res.append(A[i])
        return res

A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']
A = [ "p", "5", "p", "g", ";", "y", "j", "p", "n", "n", "#", "e", "p", "Z", "w", "J", "W", "c", "S", "W", "o", "t", "L", "p", "w", "J", "O", "R", "Y", "x", "k", "r", "x", "E", "x", "&", "Z", "l", "Y", "W", "c", "7", "z", "r", "V", "%", "l", "h", "y", "s", "k", "H", "S", "f", "a", "a", "K", "e", "t", "W", "M", "w", "g", "q", "D", "v", "P", "K", "v", "e", "h", "9", "G", "L", "{", "t", "e", "J", "m", "V", "p", "l", "f", "i", "I", "M", "i", "n", "w", "F", "9", "U", "(", "J", "w", "5", "3", "q", "c", "s" ]

s = Solution()
print(s.to_upper(A))
