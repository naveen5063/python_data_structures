class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        substr_freq_map = {}
        main_str_freq_map = {}
        count = 0

        for i in range(0, len(A)):
            if A[i] in substr_freq_map:
                substr_freq_map[A[i]] = substr_freq_map[A[i]] + 1
            else:
                substr_freq_map[A[i]] = 1

        for i in range(0, len(A)):
            if B[i] in main_str_freq_map:
                main_str_freq_map[B[i]] = main_str_freq_map[B[i]] + 1
            else:
                main_str_freq_map[B[i]] = 1

        count += self.check_freq(substr_freq_map, main_str_freq_map)
        print("count", count)

        for i in range(0, len(B)-len(A)):
            print("substr_freq_map, main_str_freq_map", substr_freq_map, main_str_freq_map)
            if B[i] in main_str_freq_map:
                print("B[i]", B[i])
                if main_str_freq_map[B[i]] == 1:
                    print("B[i] if", B[i])
                    del main_str_freq_map[B[i]]
                else:
                    main_str_freq_map[B[i]] -= 1
            if B[i+len(A)] in main_str_freq_map:
                main_str_freq_map[B[i+len(A)]] += 1
            else:
                main_str_freq_map[B[i+len(A)]] = 1
            count += self.check_freq(substr_freq_map, main_str_freq_map)
            print("count", count)
        return count

    def check_freq(self, hm1, hm2):
        print("hm1, hm2", hm1, hm2)
        #if len(hm1) == len(hm2):
        for val in hm1.keys():
            #print("hm1[val] != hm2[val]", hm1[val], hm2[val])
            if val in hm2.keys():
                if hm1[val] != hm2[val]:
                    return 0
            else:
                return 0
        else:
            return 1


A = "abc"
B = "abcbacabc"

A = "aca"
B = "acaa"

A = "p"
B = "pccdpeeooadeocdoacddapacaecb"

# A = "docp"
# B = "aoapeooeoapcpaocecddoocdcqqapeapccc"

s = Solution()
s.solve(A, B)
