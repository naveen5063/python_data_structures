class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
		if B == 1:
			return [1] * len(A)

		res = []
		hash_dict = {}
		for val in range(0, B):
			arr_val = A[val]
			if arr_val in hash_dict:
				hash_dict[arr_val] += 1
			else:
				hash_dict[arr_val] = 1
		res.append(len(hash_dict))

		last_sub_array_len = len(A) - B
		i = 1
		j = B
		print("A len", len(A))
		print("last_sub_array_len", last_sub_array_len)
		while i <= last_sub_array_len:
			print("ij",i , j)
			print("has", hash_dict)
			hash_dict[A[i - 1]] -= 1
			if hash_dict[A[i - 1]] == 0:
				del hash_dict[A[i - 1]]
			#print("j",j)
			if A[j] in hash_dict:
				hash_dict[A[j]] += 1
			else:
				hash_dict[A[j]] = 1
			res.append(len(hash_dict))
			i += 1
			j += 1

		return res

# A=[1, 2, 1, 3, 4, 3] and B = 3
#  So, we return an array [2, 3, 3, 2].

A = [1, 2, 1, 3, 4, 3]
B = 3

A = [ 2, 7, 7, 81, 81 ]
B = 1

A = [ 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97 ]
B = 8

#1 1 1 1 1 1 1 1 1 1

s = Solution()
print("res", s.dNums(A, B))