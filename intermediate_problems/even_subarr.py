import numpy as np
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        print(len(A))
        is_even_subarr = "N0"
        if len(A) % 2 == 0:
            print("even")
            two_split = np.array_split(A, 2)
            for arr in two_split:
                split_list = list(arr)
                print(split_list)
                if split_list[0] % 2 == 0 and split_list[-1] % 2 == 0:
                    is_even_subarr = "YES"
                    return is_even_subarr
        return is_even_subarr

A = [2, 4, 8, 6]
A = [2, 4, 8, 7, 6]
A = [ 978, 847, 95, 729, 778, 586, 188, 782, 813, 870, 871, 940, 312, 693, 580, 101, 760, 837, 564, 633, 680, 155, 241, 374, 682, 290, 850, 601, 433, 922, 773, 959, 530, 290, 990, 50, 516, 409, 868, 131, 664, 851, 721, 880, 20, 450, 745, 387, 787, 823, 392, 242, 674, 347, 65, 135, 819, 324, 651, 678, 139, 940 ]
s = Solution()
print(s.solve(A))