class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        pf_even = self.get_even_prefix_sum(A)
        pf_odd = self.get_odd_prefix_sum(A)
        for i in range(0, len(A)):
            if i == 0:
                teven = pf_odd[len(A)-1]
                todd = pf_even[len(A)-1] - pf_even[0]
            else:
                teven = pf_even[i-1] + (pf_odd[len(A)-1] - pf_odd[i])
                todd = pf_odd[i-1] + (pf_even[len(A)-1] - pf_even[i])
            if teven == todd:
                count += 1
        return count

    @staticmethod
    def get_even_prefix_sum(A):
        pf_even = []
        pf_even.insert(0, A[0])
        for i in range(1, len(A)):
            if i % 2 == 0:
                pf_even.insert(i, pf_even[i - 1] + A[i])
            else:
                pf_even.insert(i, pf_even[i - 1])
        return pf_even

    @staticmethod
    def get_odd_prefix_sum(A):
        pf_odd = []
        pf_odd.insert(0, 0)
        for i in range(1, len(A)):
            if i % 2 != 0:
                pf_odd.insert(i, pf_odd[i - 1] + A[i])
            else:
                pf_odd.insert(i, pf_odd[i - 1])
        return pf_odd


A = [2, 1, 6, 4]
A = [1, 1, 1]
s = Solution()
print("out ",s.solve(A))
